"""(0, 0) - the square where the game starts and ends."""

from agps.utils import action_prompt, move, take_words

class GameWon(Exception):
    """Abuse exception handling to escape the game loop when we finish."""
    pass

scene_contents = dict(keys_used = 0,
                      rope = 1,
                      )

def use_key(inventory):
    if inventory['golden key'] > 0:
        inventory['golden key'] -= 1
        scene_contents['keys_used'] += 1
        if scene_contents['keys_used'] == 4:
            raise GameWon
        print("You put the key in and turn it carefully. "
              "%s more to go." % 4 - scene_contents['keys_used'])
    else:
        print("You don't have a golden key to use.")
use = {'use', 'insert'}

def pick_up_rope(inventory):
    if scene_contents['rope'] > 0:
        inventory['rope'] += 1
        scene_contents['rope'] -= 1
        print("You put the rope in your bag. That could come in useful.")
    else:
        print("You already collected the rope.")

def enter(name, inventory):
    print("You are in a sizeable clearing in the forest. At your feet, you see "
          "a mysterious trap door, with four golden keyholes. Paths lead off "
          "in four directions, which your unerring sense of direction tells you "
          "correspond to the four compass points.")
    if scene_contents.get('rope'):
        print("A short length of rope is lying on the floor.")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        if (action[0] in use) and ('key' in action):
            use_key(inventory)
        elif (action[0] in take_words) and ('rope' in action):
            pick_up_rope(inventory)
        else:
            print("Sorry, I don't understand.")
