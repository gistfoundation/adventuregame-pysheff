"""(1, 1)"""

from agps.utils import action_prompt, move, take_words, drop_words, look_words
import sys
import time

scene_contents = {'duck':1,
                  'stick':1,
                  'entrails':0,
                  'golden key':1,
                  }

def take_duck(inventory = None):
    if scene_contents['duck'] == 1:
        print("The duck nips at your hand. Careful, you might get a disease")
        scene_contents['duck'] += 1
    elif scene_contents['duck'] > 1:
        print("You contract bird flu.")
        sys.exit(-1)
    else:
        print("There is a dead duck here.. its entrails are spread all over the place")

def take_stick(inventory = None):
    if scene_contents['stick'] == 1:
        print("You pick up the stick.")
        scene_contents['stick'] -= 1
        inventory['stick'] += 1
    else:
        print("What stick?")

def drop_berries(inventory):
    if inventory['berries'] > 0:
        print("You drop the berries on the ground")
        inventory['berries'] -= 1
        time.sleep(1)
        print("Duck looks over with a curious glint in it's eye")
        time.sleep(1)
        print("The duck waddles over to the berries")
        time.sleep(1)
        print("Duck eats berries. It looks quite bloated")
        time.sleep(1)
        print("Duck explodes in shower of feathers and entrails")
        print("You see something shiny in the goo")
        scene_contents['duck'] -= 1
        scene_contents['entrails'] += 1
    else:
        print("What berries?")

def look_goo(inventory):
    print("You see a key encrusted in duck bits")

def take_key(inventory):
    if scene_contents['entrails'] > 0 and scene_contents['golden key'] > 0:
        if inventory['stick'] > 0:
            print("You take the key using the stick to poke it free of the goo")
            print("The stick dissolves")
            inventory['stick'] -= 1
            inventory['golden key'] += 1
            scene_contents['golden key'] -= 1
        else:
            print("You wouldn't want to touch that with your bare hands!")
    else:
        print("What key?")

def enter(name, inventory):
    print("You encounter a pond")
    if scene_contents['duck']:
        print("There is a duck in the pond. It looks a bit peaky")
    if scene_contents['stick']:
        print("There is a hefty stick lying on the ground.")
    if scene_contents['entrails']:
        print("The place is covered in duck goo. Don't slip!")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            return action[1]
        if (action[0] in take_words) and ('duck' in action):
            take_duck(inventory)
        elif (action[0] in take_words) and ('stick' in action):
            take_stick(inventory)
        elif (action[0] in drop_words) and ('berries' in action):
            drop_berries(inventory)
        elif (action[0] in look_words) and ('goo' in action or 'entrails' in action):
            look_goo(inventory)
        elif (action[0] in take_words) and ('key' in action):
            take_key(inventory)
        else:
            print("Sorry, I don't understand.")
