"""Sea"""

from agps.utils import action_prompt, move, take_words


def enter(name, inventory):
    print("You are in a boat on the sea YEY sea...")
    print("You can see a dolphins to the west")
    print("You can see a island to the north")
    print("You can see a wreck to the south")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            if action[1][0] == 'w':
                print("The dolphins are further to the west")
            else:
                return action[1]
