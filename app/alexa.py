from app import ask
from flask_ask import statement, question, session as ask_session
from .models import Pokes



@ask.launch
def start_skill():
    welcome_message = 'Hello, which Pokemon would you like to catch today?'
    reprompt_text = 'if you give the name of a Pokemon I will tell you the best recipe ' \
                    'to use to catch them'
    return question(welcome_message).reprompt(reprompt_text)


@ask.intent('PokeIntent')
def find_recipe(Pokemon):
    Pokemon = Pokemon.capitalize()
    poke_query = Pokes.query.filter_by(name=Pokemon).first()
    if poke_query == None:
        speech_output = question('Sorry I could not find {}, want to try a different'
                        ' pokemon?'.format(Pokemon))
        ask_session.attributes['last_speech'] = ask_session.attributes.get['response']['outputSpeech']
        return speech_output
    if poke_query.attracted == False:
        return question('Sorry, {} , would you like to try another pokemon'
                        .format(poke_query.info))
    else:
        return statement('For {}, {}'.format(poke_query.name, poke_query.info))


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)