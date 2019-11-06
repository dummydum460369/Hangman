from Static_Resources import *


class hangman:
    def __init__(self, word, tries):
        self.word = word
        self.tries = tries
        self.word_list = [str(x) for x in word]
        self.empty_list = ['-' if i == '-' else '_' for i in self.word_list]
        self.letter_set = {str(x) for x in word}

    def replace_empty(self, letter):
        for i in range(len(self.word_list)):
            if letter == self.word_list[i].upper() or letter == self.word_list[i].lower():
                self.empty_list[i] = self.word_list[i]

    def evaluate(self, letter):
        start = self.empty_list.copy()
        self.replace_empty(letter)

        if self.empty_list == start:
            self.tries -= 1
            return False
        else:
            return True

    def check_win(self):
        if self.empty_list == self.word_list:
            return True
        else:
            return False

    def display_known_word(self):
        known_word = ''
        for a in self.empty_list:
            known_word += a + ' '
        return known_word


class Round:
    def __init__(self, word, tries, player_name=None, min_time=120):
        self.word_info = hangman(word, tries)
        self.player = player_name.title() if player_name else player_name
        self.time = min_time
        self.tried_words = []

    def test_round(self):
        if self.word_info.tries < 1:
            print('U lose')
            print('The word was', self.word_info.word)
            return False
        guess = input(str(self.word_info.display_known_word()) + '\nType your guess:')
        while input_check(self, guess) != 'Good':
            print(input_check(self, guess))
            guess = input('Type again:')

        if self.word_info.evaluate(guess):
            print('Correct!')
        else:
            print('Wrong')
        if self.word_info.check_win():
            print('You Win')
            print('The word was', self.word_info.word)
            return False
        return True

    def start_round(self, interface='Python', Input=None, prompt=None, out_cond=None, out_word=None):
        Input = input if not Input else Input
        prompt = print if not prompt else prompt
        out_cond = print if not out_cond else out_cond
        out_word = print if not out_word else out_word
        if interface:
            pass

        if self.word_info.tries < 1:
            out_cond('You LOSE! :(\nThe word was', self.word_info.word)
            return False
        out_word(self.word_info.display_known_word())
        prompt('Enter your guess:')
        guess = Input()
        while input_check(self, guess) != 'Good':
            out_cond(input_check(self, guess))
            guess = Input()

        if self.word_info.evaluate(guess):
            out_cond('CORRECT!')
        else:
            out_cond('WRONG')

        if self.word_info.check_win():
            out_cond('You WIN! UWU\nThe word was', self.word_info.word)
            return False
        return True


class game:
    def __init__(self, interface='Python', Input=None, prompt=None, out_cond=None, out_word=None):
        self.Input = input if not Input else Input
        self.prompt = print if not prompt else prompt
        self.out_cond = print if not out_cond else out_cond
        self.out_word = print if not out_word else out_word
        if interface:
            pass
