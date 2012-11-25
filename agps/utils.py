move = object()
move_directions = {'n','e','s','w','north','east','south','west'}
move_words = {'move','walk','go'}
prepositions = {'up', 'down', 'on', 'under', 'in', 'at', 'to'}

def action_prompt():
    """Prompts for an action, splits it into words, and removes any prepositions.
    
    movement actions will be represented by the move token object in this module,
    followed by a one-letter direction.
    """
    action = input('> ').lower().split()
    for prep in prepositions.intersection(action):
        action.remove(prep)
    if len(action) == 2 and (action[0] in move_words) and (action[1] in move_directions):
        return (move, action[1][0])
    return action

take_words = {'pick', 'take', 'get', 'collect'}
