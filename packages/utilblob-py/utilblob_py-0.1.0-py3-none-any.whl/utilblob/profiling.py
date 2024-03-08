import time
import math
from typing import IO

TimeF64 = float
SecInt = int
MsInt = int


def time_to_sec_ms(t: TimeF64) -> tuple[SecInt, MsInt]:
    ms, sec = math.modf(round(t, 3))
    return int(sec), int(1000 * ms)


def fmt_time(t: TimeF64) -> str:
    sec, ms = time_to_sec_ms(t)
    hms = time.strftime("%H:%M:%S", time.gmtime(sec))
    return f"{hms}.{ms:0>3}"


class TimeTracker:
    __slots__ = ("_t0",)

    def __init__(self) -> None:
        self._t0 = float("NaN")

    def start(self) -> TimeF64:
        t0 = time.time()
        self._t0 = t0
        return t0

    def tick(self) -> float:
        return time.time() - self._t0

    def get_t0(self) -> float:
        return self._t0


class ExecTimeNotifier:
    __slots__ = ("tracker", "out")

    def __init__(
        self, tracker: TimeTracker | None = None, out: IO | None = None
    ) -> None:
        self.tracker = tracker or TimeTracker()
        self.tracker.start()
        self.out = out

    def __call__(self, out: IO | None = None) -> None:
        """Print elapsed time"""
        elapsed_time = self.tracker.tick()
        print(f"[Time elapsed: {fmt_time(elapsed_time)}]", file=(out or self.out))

    def start(self) -> None:
        self.tracker.start()

    def notify(self) -> None:
        """Print elapsed time"""
        self()
