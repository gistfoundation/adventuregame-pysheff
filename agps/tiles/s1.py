"""(0, 1)"""

from agps.utils import action_prompt, move

def enter(name, inventory):
    print("You push through the undergrowth - there's hardly a path here at all.")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        else:
            print("Sorry, I don't understand.")
