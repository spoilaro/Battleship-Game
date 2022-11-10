# DESIGN DOC for Battleship game

## What?

Battleship game implemented in Python(3). The game has an AI that the player plays against.

## Rules

- 10x10 grid
- Ships available: 2, 3, 3, 4, 5
- At the beginning both players (P1 & P2) set up their ships
- Ships can be placed vertically, horizontally
- Ships _must_ not overlap
- Starting player is chosen randomly
- Game consists rounds:
  - On each turn players choose cell from the opponent's board and the game tells if it was a hit.
  - If all the cells of a ship are hit, the ship sinks.
- The last player with remaining ships wins

## Entities

_Game_
The main game object which contains the game state and main game loop.

_Player_
There are two players in the game. One (P1) is controlled by an actual human being and the another one (P2) is controlled by an algorithm (AI).
Player actions:

- [ ] Set up
- [ ] Select cell
- [ ] Fire a shot
- [ ] End turn

_Ship_
Ship contains cells and it's state is either OK or DESTROYED.

## AI Algorithm

[Propability Density Functions](https://www.datagenetics.com/blog/december32011/)

## Testing

Unit tests are in `tests/` directory. TODO: More explaning
_Game_

- [ ] Test game loop
