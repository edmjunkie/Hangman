# Name: Ibrahim Stamili
# MIT Username: N/A
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print "Loading word list from file..."
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r', 0)
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = split(line)
	print "  ", len(wordlist), "words loaded."
	print 'Enter play_hangman() to play a game of hangman!'
	print 'Enter \033[0m \033[93m guess \033[0m at any time to guess the entire word instead of one letter - warning you\'ll lose 2 lives if you get it wrong'
	return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = '' # Change this 
letters_guessed = []
mistakes_made = 0

# From part 3b:
def word_guessed():
	'''
	Returns True if the player has successfully guessed the word,
	and False otherwise.
	'''
	global secret_word
	global letters_guessed
	secret_word_len = len(secret_word)
	count = 0
	for i in secret_word:
		if i in letters_guessed:
			count += 1
	if count == secret_word_len:
		return True
	else:
		return False

		
		
def print_guessed():
	'''
	Returns a string that contains the word with a dash "-" in
	place of letters not guessed yet. 
	'''
	global secret_word
	global letters_guessed
	
	secret_word_list = list(secret_word)
	
	for i in range(len(secret_word_list)):
		if secret_word_list[i] in letters_guessed:
			continue
		else:
			secret_word_list[i] = '-'
	
	return lower(' '.join(secret_word_list))
	

def play_hangman():
	# Actually play the hangman game
	global secret_word
	global letters_guessed
	global MAX_GUESSES
	
	# Put the mistakes_made variable here, since you'll only use it in this function
	mistakes_made = 0
	
	games_played = 0
	games_won = 0
	go_again = 'y'
	
	while True:
		if go_again == 'y' or go_again == 'yes':
			lives_left = MAX_GUESSES
			secret_word  = get_word()
			all_guessed = False
			del letters_guessed[:]
			
			games_played += 1
			print 'Game', games_played
			
			while lives_left > 0:
				print_hangman_image(MAX_GUESSES - lives_left), '\n\n'
				print 'Lives left:', lives_left
				print 'guess the word'
				curr_guess = print_guessed()
				print curr_guess
				
				letter = raw_input('>> ')
				letter = letter.lower()
				
				#player chooses to guess entire word
				if letter == 'guess':
					word_guess = raw_input('what\'s the word? ')
					if word_guess == secret_word:
						all_guessed == True
						break
					else:
						print 'sorry that\'s not the word'
						lives_left -= 2
						continue

				if letter in curr_guess:
					print letter, 'has already been guessed'
					lives_left -= 1
					
				elif not letter in secret_word:
					print letter, 'is not in the word'
					lives_left -= 1
				else:
					print 'congratulations! you guessed correctly'
					letters_guessed.append(letter)
					all_guessed = word_guessed()
					if all_guessed:
						print 'congratulations! you win!'
						print 'the word was', secret_word
						games_won += 1
						go_again = raw_input('go again (y/n)?  ' )
						go_again = go_again.lower()
						break
						
			if not all_guessed:
				print_hangman_image(6)
				print 'out of lives, better luck next time'
				print 'the word was', secret_word
				go_again = raw_input('go again (y/n)?  ' )
				go_again = go_again.lower()
			
		elif go_again == 'n' or go_again == 'no':
			print 'you played', games_played, 'and won', games_won
			print 'thank you for playing'
			break
			
		else:
			print 'invalid option'
			go_again = raw_input('go again (y/n)?  ' )
			go_again = go_again.lower()
			continue
		
		
	
	return None

play_hangman()
    
