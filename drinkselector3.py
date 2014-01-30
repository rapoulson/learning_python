from sys import exit

spirits = {'gin': {'stirred': {},
				  'shaken': {}},
		  'rye': {'stirred': {'title': "On a scale of one to ten, how adventurous are you feeling this evening?"},
		  		  'shaken': {'title': "On a scale of 1-10, how adventurous are you feeling this evening?", 
		  		  			 'awesome': "Vieux Carre", 'basic':"Manhattan" }}}
		  
print spirits['gin']['stirred']['title']

spirit = raw_input("> ") # gin
spirits[spirit]


def choices(order):
	spirit = spirits[order]
	
	print "How would you like that made?"
	method = raw_input("> ")
	
	next = spritit[method]
	
	print next['title']
	drink_type = raw_input("awesome or basic: ")
	
	print next[drink_type]
	
	


def start():
	print "We have rye and gin."
	print "Which spirit will you be drinking this evening?"
	
	next = raw_input("> ")
	choices(next)
	
	if next == "gin":
		gin_choices()
	elif next == "rye":
		choices()
	else:
		print "Can't decide? I'll pick a random drink for you."
		from random import choice
		print choice(drinks)
		
start()
		