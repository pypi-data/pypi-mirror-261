from datetime import datetime
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..run import InputMode, Run, RunStatus, save_run
from ..runs import RunInfo
from ..shape import Shape
from ..store import ShapeInfo
from .state import state

router = APIRouter()


class SimpleShapeInfo(BaseModel):
    id: str
    name: str | None
    filename: str
    created_at: datetime
    updated_at: datetime


class ResponseShapes(BaseModel):
    shapes: list[SimpleShapeInfo]


@router.get("", description="List of shapes")
def read_shapes() -> ResponseShapes:
    shape_store = state.shape_store
    shape_infos = shape_store.list()
    simple_shape_infos = [
        SimpleShapeInfo(**shape.dict()) for shape in shape_infos if shape is not None
    ]
    return ResponseShapes(shapes=simple_shape_infos)


class ResponseShape(BaseModel):
    shape: ShapeInfo


@router.get("/{shape_id}")
def read_shape(shape_id: str):
    shape_store = state.shape_store
    shape_store.refresh()
    shape_info = shape_store.get_by_id(shape_id)
    if shape_info is None:
        raise HTTPException(status_code=404, detail="Shape not found")
    # TODO: Use ResponseShape, Problem with multiple version of pydantic
    return {"shape": shape_info}


class RequsetRun(BaseModel):
    data: list | dict


class ResponseRun(BaseModel):
    run_id: str
    run_status: RunStatus
    outputs: list | dict


class ResponseRunFailed(BaseModel):
    run_id: str
    run_status: Literal[RunStatus.FAILED]
    error: str
    outputs: list | dict | None


class RunFailedException(Exception):
    def __init__(self, body: ResponseRunFailed):
        self.body = body


@router.post(
    "/{shape_id}/run",
    responses={542: {"model": ResponseRunFailed, "description": "Run failed"}},
)
def shape_data(shape_id: str, body: RequsetRun) -> ResponseRun:
    shape_store = state.shape_store
    shape_store.refresh()
    shape_info = shape_store.get_by_id(shape_id)
    if shape_info is None:
        raise HTTPException(status_code=404, detail="Shape not found")

    shape = Shape().load(shape_info.content)
    runner = state.runner
    runner.store.refresh()

    run = Run(shape=shape, input_mode=InputMode.API)

    data = body.data
    if isinstance(data, dict):
        data = [data]

    run_res = runner.process(lines=data, run=run, return_outputs=True)

    save_run(run_res, state.run_store.path, quiet=True)

    if run_res.outputs is not None and len(run_res.outputs) == 1:
        outputs = run_res.outputs[0]
    else:
        outputs = run_res.outputs

    if run_res.status == RunStatus.FAILED:
        response = ResponseRunFailed(
            run_id=run_res.id,
            run_status=run_res.status,
            error="Run failed",
            outputs=outputs,
        )
        raise RunFailedException(body=response)

    return ResponseRun(run_id=run_res.id, run_status=run_res.status, outputs=outputs)


class ResponseRuns(BaseModel):
    runs: list[RunInfo]


@router.get("/{shape_id}/runs", description="List of runs for a shape")
def read_runs(shape_id: str) -> ResponseRuns:
    state.shape_store.refresh()
    shape_info = state.shape_store.get_by_id(shape_id)
    if shape_info is None:
        raise HTTPException(status_code=404, detail="Shape not found")

    runs = state.run_store.list()
    shape_runs = [run for run in runs if run.shape_id == shape_id]
    # sort by most recent created first
    shape_runs.sort(key=lambda x: x.created_at, reverse=True)
    return ResponseRuns(runs=shape_runs)
