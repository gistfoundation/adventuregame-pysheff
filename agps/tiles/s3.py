from agps.utils import action_prompt, move, take_words, give_words, use_words, fight_words
from random import random
from sys import exit

scene_contents = {'warrior':1, "sword":1}

def fight_warrior(inventory):
    if inventory["sword"] > 0:
        if random() > 0.5:
            print ("You kill the warrior and pick up the golden key")
            inventory["golden key"] += 1
        else:
            print ("The warrior kills you and the rhinoceros returns to eat your corpse.")
            exit(1)
    else:
        print ("You don't have a sword! The warrior kills you and the rhinoceros returns to eat your corpse.")
        exit(1)

def enter(name, inventory):
    print("In this room awaits a menacing warrior guarding a golden key. There is a sword on the floor")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        if action[0] in take_words and 'sword' in action:
            inventory["sword"] += 1
        elif action[0] in fight_words and 'warrior' in action:
            fight_warrior(inventory)
        else:
            print("Sorry, I don't understand.")
