import random

def get_response(message: str) -> str:
    p_message = message.lower()
    compliments = ["Colors seem brighter when you're around", "You are making a big difference", "You are gorgeous", "The people you love are lucky to have you in their lives", "Look at you shining like the brightest star", "There's ordinary, and then there's you"]

    if p_message == 'hello':
        return 'Hey dumb dumb!'

    if p_message == 'i love you':
        return 'Shaif said: I LOVEE YOUUU <333'

    if p_message == 'compliment me':
        return str(random.choice(compliments))

    if message == 'roll':
        return 'You rolled: ' + str(random.randint(1, 20))

    if p_message == '*help':
        return '`List of commands: ' \
               'hello, ' \
               'compliment me, ' \
               'i love you, ' \
               'roll`'

    return 'I did not understand what you wrote. Try typing "*help".'
