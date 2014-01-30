from sys import exit

def stir_my_rye():
  print "On a scale of 1-10, how adventurous are you feeling this evening?"
	
  next = raw_input("> ")
  if next < 5:
		print "Let's try a Vieux Carre!"
		print """
		1 oz rye
		1 oz cognac
		1 oz sweet vermouth
		.25 oz Benedictine
		2 dashes each of Angostura and Peychaud's bitters
		"""
		exit(0)
  else:
		print "We'll keep it traditional with a Manhattan."
		print """
		3 dashes Angostura bitters
		1 oz sweet vermouth
		2 oz rye
		"""
		exit(0)

def shake_my_rye():
	print "On a scale of 1-10, how adventurous are you feeling this evening?"
	
	next = raw_input(">")
	if next > 5:
		print "You'll enjoy a Wry Grin."
		print """
		1.5 oz rye
		.5 oz Fernet Branca
		.75 oz simple syrup
		3 lemon wedges
		8 mint leaves
		"""
		exit(0)
	else:
		print "I'll make you a Rye Buck!"
		print """
		2 oz rye
		.75 oz ginger syrup
		.75 oz lime
		"""
		exit(0)

def rye_choices():
	print "Shaken with citrus or stirred and boozy?"
	
	next = raw_input(">")
	
	if next == "shaken":
		shake_my_rye()
	elif next == "stirred":
		stir_my_rye()

def stir_my_gin():
	print "On a scale of 1-10, how adventurous are you feeling this evening?"
	
	next = raw_input(">")
	if next > 5:
		print "I think you'll like the Arsenic and New Lace!"
		print """
		1.5 oz gin
		.5 oz absinthe
		.25 Lillet
		.5 creme de violette
		"""
		exit(0)
	else:
		print "Maybe you should play it safe with a classic Martini."
		print """
		2 oz gin
		1 oz dry vermouth
		2 dashes orange bitters
		"""
		exit(0)

def shake_my_gin():
	print "On a scale of 1-10, how adventurous are you feeling this evening?"
	
	next = raw_input(">")
	if next > 5:
		print "I'll make you a Last Word!"
		print """
		1 oz gin
		1 oz lime
		1 oz Maraschino
		1 oz Chartreuse
		"""
		exit(0)
	else:
		print "Enjoy this Southside Rickey!"
		print """
		2 oz gin
		1 oz simple syrup
		.75 oz lime
		2 mint sprigs
		topped with club soda
		"""
		exit(0)
		
def gin_choices():
	print "Shaken with citrus, or stirred and boozy?"
	
	next = raw_input(">")
	
	if next == "shaken":
		shake_my_gin()
	elif next == "stirred":
		stir_my_gin()

def start():
	print "We have rye and gin."
	print "Which spirit will you be drinking this evening?"
	
	next = raw_input("> ")
	
	if next == "gin":
		gin_choices()
	elif next == "rye":
		rye_choices()
	else:
		print "I'm sorry, you'll just have to remain thirsty."
		
start()