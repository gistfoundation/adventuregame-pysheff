move = object()
move_directions = {'n','e','s','w','north','east','south','west'}
move_words = {'move','walk','go'}
give_words = {'give', 'feed', 'present'}
use_words = {'eat', 'use', 'wear'}
fight_words = {'fight', 'kill', 'hit', 'attack'}
prepositions = {'up', 'down', 'on', 'under', 'in', 'at', 'to'}

drop_words = {'drop'}
look_words = {'look', 'inspect', 'examine'}
inventory_names = {'inventory', 'possessions', 'belongings', 'bag'}

def action_prompt(inventory):
    """Prompts for an action, splits it into words, and removes any prepositions.
    
    movement actions will be represented by the move token object in this module,
    followed by a one-letter direction.
    """
    action = []
    while len(action) == 0:
        action = input('> ').lower().split()
    for prep in prepositions.intersection(action):
        action.remove(prep)
    if len(action) == 2 and (action[0] in look_words) and (action[1] in inventory_names):
        print("You have:")
        for item, n in inventory.most_common():
            print(item, '(%d)' % n)
        return action_prompt(inventory)
    if len(action) == 2 and (action[0] in move_words) and (action[1] in move_directions):
        return (move, action[1][0])
    return action

take_words = {'pick', 'take', 'get', 'collect'}
