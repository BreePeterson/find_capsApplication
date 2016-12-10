#Programer: Brian Peterson
#Overview: A simple program that finds and lists all the captial leters in a string. The program is part of an application for Rohde & Schwarz
#Extra info: December 9, 2016

import string

def string_upper(capz):
	BigLetters = input
	input = "Please enter a string"
	for char in capz:
		if char.isupper():
			BigLetters += char
	return BigLetters

print(string_upper)