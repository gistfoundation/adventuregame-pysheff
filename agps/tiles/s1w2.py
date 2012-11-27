from agps.utils import action_prompt, move, take_words, look_words


scene_contents = {'golden key':1}

def enter(name, inventory):
    print("There is a wreck sticking out of the sea")
    print("There is a barrel floating inside the hull of the ex-boat")
    print("You can see a dolphins to the west")
    print("You can see a island far to the north")
    print()
    while True:
        action = action_prompt(inventory)
        if action[0] is move:
            if action[1][0] == 'w':
                print("The dolphins are further to the west")
            else:
                return action[1]
        if action[0] in look_words:
            if action[1] == 'wreck':
                if inventory['rope']:
                    print("You climb down rope and search the barrel")
                    pick_up_key(inventory)
                else:
                    print("You can see a barrel but can't reach it")
        else:
            print("Sorry, I don't understand.")


def pick_up_key(inventory):
    if scene_contents['golden key'] > 0:
        inventory['golden key'] += 1
        scene_contents['golden key'] -= 1
        print("You put the key in your bag, you're one step closer to opening the door")
    else:
        print("You already collected the key here.")
