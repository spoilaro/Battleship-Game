from dataclasses import dataclass
from enum import Enum
import numpy as np
from typing import Any


class ShipState(Enum):
    FLOATING = 0
    DESTROYED = 1
    SAFE = 2


@dataclass
class Position:
    x: int
    y: int
    hit: bool


@dataclass
class Ship:
    cells: list[Position] | None
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
    id: int
    available_ships: list[int]
