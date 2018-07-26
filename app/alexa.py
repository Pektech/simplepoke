from app import ask
from flask_ask import statement, question, session as ask_session
from .models import Pokes




@ask.launch
def start_skill():
    welcome_message = 'Hello, which Pokemon would you like to catch today?'
    reprompt_text = 'if you give the name of a Pokemon I will tell you the best recipe ' \
                    'to use to catch them'
    ask_session.attributes['last_speech'] = reprompt_text
    return question(welcome_message).reprompt(reprompt_text)


@ask.intent('PokeIntent')
def find_recipe(Pokemon):
    Pokemon = Pokemon.capitalize()
    poke_query = Pokes.query.filter_by(name=Pokemon).first()
    if poke_query == None:
        speech_output = 'Sorry I could not find {}, want to try a different' \
                        ' pokemon?'.format(Pokemon)
        ask_session.attributes['last_speech'] = speech_output
        return question(speech_output)
    if poke_query.attracted == False:
        speech_output = 'Sorry, {} , would you like to try another pokemon' \
                        .format(poke_query.info)
        ask_session.attributes['last_speech'] = speech_output
        return question(speech_output)
    else:
        speech_output = 'For {}, {}'.format(poke_query.name, poke_query.info)
        ask_session.attributes['last_speech'] = speech_output
        return question(speech_output)


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)