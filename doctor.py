"""
doctor.py
Date: 9/10/2019
Author: David T.

description...
	
"""

import random

hedges = ("Please tell me more.","Many of my patients tell me the same thing.","Please continue.","Go on.")
qualifiers = ("Why do you say that ","You seem to think that ","Can you explain why ","Can you tell me more about ")
replacements = {"I":"you", "I'm":"you are", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours","am":"are"}

history = []

def reply(sentence):
	"""Builds and returns a reply to the user's sentence."""
	probability = random.randint(1,4)
	
	# adds the user input to the list
	history.append(sentence)
	
	if probability == 1:
		return random.choice(hedges)
	elif probability == 2 and len(history):
		# Doctor is going back to an earlier topic
		return "Earlier you said that "+changePerson(random.choice(history))
	else:
		return random.choice(qualifiers)+changePerson(sentence)+"?"

def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns"""
	words = sentence.split()
	replyWords = []
	
	for word in words:
		replyWords.append(replacements.get(word,word))
	
	return " ".join(replyWords)

def main():
	"""Handles the interaction between patient and doctor"""
	print("Good morning, I hope you are well today.")
	print("What can I do for you?")
	
	while True:
		sentence = input("\n>>>")
		if sentence.upper() == "QUIT":
			print("Have a nice day.")
			break
		print(reply(sentence))
	
	input()

main()