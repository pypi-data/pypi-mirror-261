import math


def order_of_magnitude(x: float) -> int:
    if x == 0:
        return 0

    return math.floor(math.log10(abs(x)))


def order_of_magnitude_binary(x: int) -> int:
    x = abs(x)
    order = 0

    while x:
        x = x >> 1
        order += 1

    return order


def is_power_of_2(x: int) -> bool:
    """https://graphics.stanford.edu/%7Eseander/bithacks.html#DetermineIfPowerOf2"""
    return x != 0 and (x & (x - 1)) == 0


def is_power_of_2_abs(x: int) -> bool:
    return is_power_of_2(abs(x))


def clip[N: int | float](value, lo: N = 0, hi: N = 1) -> N:
    """Clips (saturates) the value"""
    return max(lo, min(hi, value))
