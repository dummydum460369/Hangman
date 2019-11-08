from random_word import *
from time import *
import sys


def get_random_word(min_length=None, max_length=None):
    word = RandomWords()
    if not min_length:
        min_length = 0
    try:
        if max_length:
            return word.get_random_word(minLength=min_length, maxLength=max_length, hasDictionaryDef='true',
                                        includePartOfSpeech="noun,verb")
        else:
            return word.get_random_word(minLength=min_length, hasDictionaryDef='true',
                                        includePartOfSpeech="noun,verb")
    except:
        return get_random_word(min_length, max_length)


def input_check(Round, word):
    if len(word) != 1:
        return 'Enter just one alphabet'
    if not word.isalpha():
        return 'Enter an Alphabet only'
    if word in Round.tried_words:
        return 'You already tried it'
    Round.tried_words.append(word)
    return 'Good'


def printer(stuff):
    sys.stdout.write("\r\x1b[K" + stuff.__str__())
    sys.stdout.flush()


def intro():
    word = '---HANGMAN---'
    word_list = [x for x in word]
    start = time()
    index = 0
    frontspace = 0
    enterkeys = 0

    while time() - start < 10:
        dispword = ''
        for i in range(0, 13):
            if i == index:
                dispword += ' '
            elif i == index - 1 or i == index + 1:
                dispword += r'|'
            else:
                dispword += word_list[i]
        frontspace = frontspace + 2 if frontspace < 6 else 0
        enterkeys = enterkeys + 3 if enterkeys < 6 else 0
        if time() - start < 2:
            printer(word)
        else:
            printer(dispword)
        index = index + 1 if index < 12 else 0
        sleep(1 / 8)
