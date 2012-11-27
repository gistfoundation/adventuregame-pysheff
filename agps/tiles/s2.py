"""(0, 1)"""

from agps.utils import action_prompt, move, take_words, give_words, use_words, fight_words
from random import random

scene_contents = {'rhinoceros':1}

def feed_berries_to_rhino(inventory):
    if "rhinoceros" not in scene_contents:
        print ("Rhinoceros? What rhinoceros?")
        return

    if inventory['berries'] > 0:
        print ("The rhino eats the berries and runs away!")
        del scene_contents["rhinoceros"]
    else:
        print ("The rhinoceros senses you don't have any berries and becomes even angrier!")

def enter(name, inventory):
    print("Oh no! You've wandered into a swamp that looks like a wild animal's lair!")
    if 'rhinoceros' in scene_contents:
        print("You spot an angry rhino. It spots you and begins to slosh and roar.")
    if random() > 0.5:
        print('Maybe the rhino is hungry')
    else:
        print('Maybe you can scare the rhino away')
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        if action[0] in give_words and 'berries' in action and ('rhino' in action or 'rhinoceros' in action):
            feed_berries_to_rhino(inventory)
        elif action[0] in fight_words and ('rhino' in action or 'rhinoceros' in action):
            print ("Fight a rhino? Are you insane?")
        else:
            print("Sorry, I don't understand.")
