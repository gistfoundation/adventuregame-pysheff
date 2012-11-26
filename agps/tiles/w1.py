"""(0, 1)"""

from agps.utils import action_prompt, move

def enter(name, inventory):
    print("The trees open out onto a beautiful beach. Small waves lap at the "
          "sand. Ahead of you, the ocean stretches as far as you can see.")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        else:
            print("Sorry, I don't understand.")
