import time


def time_ms() -> float:
    return 1e-3 * time.time_ns()
