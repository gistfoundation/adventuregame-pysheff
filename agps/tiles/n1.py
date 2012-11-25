"""(0, 1)"""

from agps.utils import action_prompt, move

def enter(name, inventory):
    print("A path runs through dense jungle. To the north, you can see the "
          "entrance to a cave.")
    print()
    while True:
        action = action_prompt()
        if action[0] is move:
            return action[1]
        else:
            print("Sorry, I don't understand.")
