from dataclasses import dataclass
from enum import Enum
import numpy as np
from typing import Any, Optional


class ShipState(Enum):
    FLOATING = 0
    DESTROYED = 1
    SAFE = 2


class Printing:

    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


@dataclass
class Position:
    x: int
    y: int
    hit: bool | None = None


@dataclass
class Ship:
    hits: int
    state: ShipState
    size: int
    id: int


@dataclass
class Config():
    available_ships: list[int]
    grid_size: int
    game_version: str
    player_count: int


@dataclass
class PlayerData:
    grid: Any
    pre_filled_grid: bool | None
    available_ships: list[int] | None
