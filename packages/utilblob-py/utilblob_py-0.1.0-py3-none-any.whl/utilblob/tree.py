from collections.abc import Iterable
from collections import defaultdict
import typing
from copy import copy
from collections.abc import Generator, Hashable, Sequence, Mapping
from dataclasses import dataclass
from typing import Any, TypeVar, Union
from enum import Enum, auto


K = TypeVar("K", bound=Hashable)
V = TypeVar("V")

TreeMapping = Mapping[K, Union["TreeMapping", V]]
TreeDict = dict[K, Union["TreeDict", V]]
TreeDefaultDict = defaultdict[K, Union["TreeDefaultDict", V]]
MultiTreeMapping = Mapping[
    K, Union[list[V], "MultiTreeMapping", list["MultiTreeMapping"]]
]
BranchKeys = tuple[K, ...]


class WalkStrategy(Enum):
    DFS = auto()
    BFS = auto()


@dataclass(frozen=True, slots=True)
class UnknownWalkStrategyError(Exception):
    strategy: Any


def walk_bfs(t: TreeMapping[K, V]):
    node_stack = list(t.items())

    while node_stack:
        k, v = node_stack.pop()
        yield k, v

        if isinstance(v, Mapping):
            node_stack.extend(v.items())  # type: ignore


def walk_dfs(t: TreeMapping[K, V]):
    node_stack = list(t.items())

    while node_stack:
        k, v = node_stack.pop()

        yield k, v

        if isinstance(v, Mapping):
            node_stack.insert(0, v)  # type: ignore


def walk_bfs_parent(
    t: TreeMapping[K, V],
) -> Generator[tuple[TreeMapping[K, V], K, V], None, None]:
    """
    Does not yield the root node.
    """

    parent_stack = [t]

    while parent_stack:
        parent = parent_stack.pop()
        node_stack = list(parent.items())

        while node_stack:
            k, v = node_stack.pop()

            yield parent, k, v  # type: ignore

            if isinstance(v, Mapping):
                parent_stack.append(v)  # type: ignore
                node_stack.extend(v.items())  # type: ignore


def walk_bfs_branch(t: TreeMapping[K, V]):
    parent_stack: list[tuple[TreeMapping[K, V], BranchKeys[K]]] = [(t, ())]

    while parent_stack:
        parent, ancestors = parent_stack.pop()

        node_stack = list(parent.items())

        while node_stack:
            k, v = node_stack.pop()

            node_ancestors = (*ancestors, k)

            yield node_ancestors, v

            if isinstance(v, Mapping):
                parent_stack.append((v, node_ancestors))  # type: ignore
                node_stack.extend(v.items())  # type: ignore


def walk_bfs_parents(t: TreeMapping[K, V]):
    parent_stack = [(t, [])]

    while parent_stack:
        parent, ancestors = parent_stack.pop()

        node_stack = list(parent.items())

        while node_stack:
            k, v = node_stack.pop()

            node_ancestors = [parent, *ancestors]

            yield k, v, copy(node_ancestors)

            if isinstance(v, Mapping):
                parent_stack.append((v, node_ancestors))  # type: ignore
                node_stack.extend(v.items())  # type: ignore


def _dispatch_walker(strategy: WalkStrategy):
    match strategy:
        case WalkStrategy.BFS:
            return walk_bfs
        case WalkStrategy.DFS:
            return walk_dfs
        case _:
            raise UnknownWalkStrategyError(strategy)


def walk(t: TreeMapping[K, V], strategy: WalkStrategy = WalkStrategy.BFS):
    yield from _dispatch_walker(strategy)(t)


def getitem(t: TreeMapping[K, V], keys: Iterable[K]) -> V | TreeMapping[K, V]:
    cur_node = t

    # set branch
    for k in keys:
        cur_node = cur_node[k]  # type: ignore

    return cur_node  # type: ignore


def assign_leaf(d: TreeMapping[K, V], keys: Sequence[K], value: V) -> None:
    last_node = getitem(d, keys[:-1])
    last_node[keys[-1]] = value  # type: ignore


def _append_unique(coll, elem):
    if elem in coll:
        return

    coll.append(elem)


def assign_multitree_leaf(
    d: MultiTreeMapping[K, V], keys: Sequence[K], value: V
) -> None:
    last_node = getitem(d, keys[:-1])
    multileaf: list[V] = last_node[keys[-1]]  # type: ignore

    if isinstance(multileaf, list):
        _append_unique(multileaf, value)
    else:
        last_node[keys[-1]] = [last_node[keys[-1]], value]  # type: ignore


def defaultdict_to_dict_tree(ddt: TreeDefaultDict[K, V]) -> TreeDict[K, V]:
    d = dict(ddt)

    for branch_keys, v in walk_bfs_branch(d):
        if isinstance(v, defaultdict):
            assign_leaf(d, branch_keys, dict(v))

    return typing.cast(TreeDict[K, V], d)


def defaultdict_stiffen(ddt: TreeDefaultDict[K, V]) -> None:
    ddt.default_factory = None

    for _, v in walk_bfs(ddt):
        if isinstance(v, defaultdict):
            v.default_factory = None
