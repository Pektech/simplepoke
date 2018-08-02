from app import ask
from flask_ask import statement, question
from flask_ask import session as ask_session, request as ask_request
from .models import Pokes
from .conversation import rand_start, rand_make




@ask.launch
def start_skill():
    welcome_message = 'Hello, which Pokemon would you like to catch today?'
    reprompt_text = 'if you give me the name of a Pokemon I will tell you the best recipe ' \
                    'to use to catch them'
    ask_session.attributes['last_speech'] = reprompt_text
    return question(welcome_message).reprompt(reprompt_text)


@ask.intent('PokeIntent')
def find_recipe(Pokemon):
    Pokemon = Pokemon.capitalize()
    poke_query = Pokes.query.filter_by(name=Pokemon).first()
    start_choice = rand_start()
    make_choice = rand_make()
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

        speech_output = ' {} {} {} {}. '.format(start_choice,
                                                poke_query.recipe_type,
                                                make_choice,
                                                poke_query.info)
        ask_session.attributes['last_speech'] = speech_output
        return statement(speech_output)


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)


@ask.intent('AMAZON.HelpIntent')
def help():
    return question('if you say a pokemon name I will find you a recipe')


@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def cancel():
    return statement('Good bye')

@ask.intent('AMAZON.YesIntent')
def yes():
    repeat_speech = ask_session.attributes['last_speech']
    return question('Not really a yes question. ' + repeat_speech)