from ..runner import Runner
from ..runs import RunStore
from ..store import ShapeStore


class State:
    run_store: RunStore
    shape_store: ShapeStore
    runner: Runner


state = State()
