import string

def run_story(story):
	indexes = range(1, len(story), 2)
	for i in indexes:
		story[i] = raw_input(story[i])
	print string.join(story)

lib = [
	"Once upon a time, there was a very sick boy named",
	"Name:",
	". His tummy hurt, his head hurt, even his",
	"Noun (body part):",
	"hurt. He puked all over his",
	"Noun:",
	"When he slept, he had dreams about",
	"Noun (plural):",
	"fighting",
	"Adverb:",
]

run_story(lib)