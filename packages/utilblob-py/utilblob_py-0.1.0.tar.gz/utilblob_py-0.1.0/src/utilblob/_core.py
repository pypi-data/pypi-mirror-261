def resolve_one_or_more[T](x_or_xs: T | tuple[T, ...]) -> tuple[T, ...]:
    return x_or_xs if isinstance(x_or_xs, tuple) else (x_or_xs,)
