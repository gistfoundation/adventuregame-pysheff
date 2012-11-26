"""(0, 1)"""

from agps.utils import action_prompt, move, take_words

scene_contents = {'berries':1}

def take_berries(inventory):
    if scene_contents['berries'] > 0:
        scene_contents['berries'] -= 1
        inventory['berries'] += 1
        print("Reaching up, you pick the berries.")
    else:
        print("There are no berries here.")

def enter(name, inventory):
    print("The path crosses a small stream.")
    if scene_contents['berries']:
        print("There are some berries hanging from a tree. They look edible. "
              "If you're hungry enough, anyway.")
    print()
    while True:
        action = action_prompt()
        if action[0] is move:
            return action[1]
        if (action[0] in take_words) and ('berries' in action):
            take_berries(inventory)
        else:
            print("Sorry, I don't understand.")
