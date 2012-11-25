from collections import Counter
from .tiles import grid
from .tiles.start import GameWon

def process_move(move):
    move = move.upper()
    if move == 'N':
        return (0, 1)
    if move == 'S':
        return (0, -1)
    if move == 'W':
        return (-1, 0)
    if move == 'E':
        return (1, 0)
    print("Move %s not recognised" % move)
    return (0, 0)

def main():
    name = input("What is your name? ")
    inventory = Counter()
    x, y = 0, 0
    
    try:
        while True:
            tile = grid[x,y]
            move = tile.enter(name, inventory)
            dx, dy = process_move(move)
            new_locn = x+dx, y+dy
            if new_locn in grid:
                x, y = new_locn
            else:
                print("The undergrowth in that direction is impenetrable. "
                      "You turn back.")
                print()
            
    except GameWon:
        print("Congratulations!")
