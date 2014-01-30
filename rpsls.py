# Rock-paper-scissors-lizard-Spock template

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import math
import random

# helper functions

def number_to_name(number):
	# convert number to a name using if/elif/else
	# don't forget to return the result!
	
	if number == 0:
		number = str('rock')
		
	elif number == 1:
		number = str('Spock')
		
	elif number == 2:
		number = str('paper')
		
	elif number == 3:
		number = str('lizard')
		
	elif number == 4:
		number = str('scissors')
		
	else:
		print 'Dude, that is not a valid input.'
		
	return number
	
def name_to_number(name):
	# convert name to number using if/elif/else
	# don't forget to return the result!
	
	if name == 'rock':
		name = int(0)
		
	elif name == 'Spock':
		name = int(1)
		
	elif name == 'Paper':
		name = int(2)
		
	elif name == 'lizard':
		name = int(3)
		
	elif name == 'scissors':
		name = int(4)
		
	else:
		print 'The name of the game is rock, paper, scissors, lizard, Spock.'
		
def rpsls(name):
	# fill in your code below
	# convert name to player_number using name_to_number
	player_number = name_to_number(name)
	
	# compute random guess for comp_number using random.randrange()
	difference = (player_number - computer_number) % 5
	
	# use if/elif/else to determine winner
	if difference > 2.1:
		result = 'You lose :('
		
	elif difference == 0:
		result = 'A tie is like kissing your sister'
		
	elif difference < 2.1:
		result = 'Congratulations, you've triumphed over the machine!'
		
	else:
		print 'I don't know, somehow you screwed this up'
		
	# convert comp_number to name using number_to_name
	comp_name = number_to_name(computer_number)
	
	# print results
	print 'You choose ', name
	print 'Computer chooses ', comp_name
	print result
	print
	
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
		
	
		