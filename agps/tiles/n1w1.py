"""(-1, 1)"""

from agps.utils import action_prompt, move, take_words

scene_contents = {'boat':1}

def enter(name, inventory):
    print("The beach continues. Small waves lap at the "
          "sand. Ahead of you, the ocean stretches as far as you can see.")
    if scene_contents.get('boat'):
        print("There is a small boat high up on the sand")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] in take_words and 'boat' in action:
            pick_up_boat(inventory)
        elif action[0] is move:
            if action[1][0] == 'w' and not inventory['boat']:
                print("you've forgotten how to swim")
            else:
                return action[1]
        else:
            print("Sorry, I don't understand.")


def pick_up_boat(inventory):
    if scene_contents['boat'] > 0:
        inventory['boat'] += 1
        scene_contents['boat'] -= 1
        print("You put the boat in your bag. It's a very big bag")
    else:
        print("You already collected the boat.")
