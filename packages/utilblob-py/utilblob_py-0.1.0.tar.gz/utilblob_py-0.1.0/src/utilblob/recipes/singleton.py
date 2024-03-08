from dataclasses import dataclass, field
from functools import lru_cache
from typing import Self


@dataclass
class Singleton:
    """
    This does not work well with dataclasses
    """

    _instance: Self | None = field(init=False, default=None)

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(*args, **kwargs)
        return cls._instance


class SingletonMeta(type):
    """
    Dataclass-proof.

    CAREFUL: object might be reinitialized, you can add a wrapper around
    __init__ in __new__ method that checks whether it has been initialized
    or just add a custom initialization classmethod.
    """

    # _Self needed for metaclass, since type[Self] does not work
    def __call__[_Self](cls: type[_Self], *args, **kwargs) -> _Self:
        # ensure unique attribute name
        instance_attr = SingletonMeta._mangle_instance_attr_name(cls)

        if (instance := getattr(cls, instance_attr, None)) is None:
            instance = super().__call__(*args, **kwargs)

            setattr(cls, instance_attr, instance)

        return instance

    def get_instance[_Self](cls: type[_Self]) -> _Self | None:
        return getattr(cls, SingletonMeta._mangle_instance_attr_name(cls), None)

    @staticmethod
    @lru_cache
    def _mangle_instance_attr_name(cls_obj: type) -> str:
        return f"_{cls_obj.__name__}_{id(cls_obj)}_instance"


class Singleton2(metaclass=SingletonMeta):
    def print_id(self):
        print(id(self))
