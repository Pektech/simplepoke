import random


start = ['Hmm try the ', 'I would suggest the ', 'Make the ',
         'let me ask google... okay. use the ', 'For best results use the ',
         'I recommend the ', 'Oh I know this one, use the ']

make = [' which uses ', '. It combines ', '. It is made with ',
        ' using locally sourced ingredients. ', ' using ']

def rand_start():
    start_choice = random.choice(start)
    return start_choice

def rand_make():
    make_choice = random.choice(make)
    return make_choice