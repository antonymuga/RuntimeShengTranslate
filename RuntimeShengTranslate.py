#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*        RUNTIME SHENG TRANSLATOR - ENGLISH TRACK        *
#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*  Welcome to Runtime Sheng translator. v1.0.0           *
#	*  MIT License, Copyright(c) 2018, Antony Muga           *
#	*  All Rights Reserved.                                  *
#	*  Author: Antony Muga                                   *
#	----------------------------------------------------------
#	*  Project's Links:                                      *
#	*  Twitter: https://twitter.com/RuntimeLab               *
#	*  Runtime Lab on LinkedIn                               *
#	*  RuntimeLab on Github                                  *
#	*  RuntimeShengTranslator project on GitHub                    *
#	----------------------------------------------------------
#	*  Personal social links:                                *
#	*  GitHub: https://github.com/antonymuga/                *
#	*  Website: https://antonymuga.github.io                 *
#	*  LinkedIn: https://www.linkedin.com/in/antony-muga/    *
#	*  Email: https://sites.google.com/view/antonymuga/home  *
#	----------------------------------------------------------


# The below 'import sys' is currently vestigial now but will come in handy while writing new submissions
# into the individual dictionary files, open, write, close and all that Jazz
import sys

# Import the project details
import about

# Import the dictionaries for the different languages
from Dictionaries import ToEng # English dictionary
from Dictionaries import ToFre # French dictionary
from Dictionaries import ToGer # German dictionary
from Dictionaries import ToSpa # Spanish dictionary
from Dictionaries import ToIta # Italian dictionary

# Print line separator
print("\n","*"*75, "\n")

# Print the project details
print(about.projectDetails)

# Print line separator for different sections
print("\n","*"*75, "\n")


# Declare a tuple that contains all the imported dictionaries
dictionaryList = (ToEng.shengToEng, ToFre.shengToFre, ToGer.shengToGer, ToSpa.shengToSpa, ToIta.shengToIta)

# Enter new word submissions
submissions = []


# Select language for translation
langSelect = int(input("""

	PLEASE SELECT THE LANGUAGE YOU WANT TO TRANSLATE SHENG TO:

	  0: ENGLISH

	  1: FRENCH

	  2: GERMAN

	  3: SPANISH

	  4: ITALIAN

	Language: """))


# Select the active dictionary that is to be used for translation
def chosenDictionary():
	if (langSelect == 0):
		activeDictionary = dictionaryList[0]
	elif (langSelect == 1):
		activeDictionary = dictionaryList[1]
	elif (langSelect == 2):
		activeDictionary = dictionaryList[2]
	elif (langSelect == 3):
		activeDictionary = dictionaryList[3]
	elif (langSelect == 4):
		activeDictionary = dictionaryList[4]
	else:
		print("""
			Invalid input.RuntimeShengTranslator is exiting!
			{}""".format(about.signOff))
		exit()
	return activeDictionary

# Select the language to be used for translation, usefull in the output string
def chosenLanguage():
	if chosenDictionary() == dictionaryList[0]:
		language = "ENGLISH"
	elif chosenDictionary() == dictionaryList[1]:
		language = "FRENCH"
	elif chosenDictionary() == dictionaryList[2]:
		language = "GERMAN"
	elif chosenDictionary() == dictionaryList[3]:
		language = "SPANISH"
	elif chosenDictionary() == dictionaryList[4]:
		language = "ITALIAN"
	return language


# THE CORE LOGIC OF RUNTIME TRANSLATOR APP
def RuntimeShengTranslator():

	# Call the chosen dictionary
	chosenDictionary()

	# Call the chosen language
	chosenLanguage()

	# Enter the search string, only one word is supported for now
	shengWord = str(input("""
	NOTE: Currently, only single words are supported.
	More features will be added in through the course of 
	development.

	PLEASE ENTER A SHENG WORD TO TRANSLATE.

	Your word: """))

	# TO DO
	# Write new logic to test for empty input, the one below is whack

	# Number of times the user is going to enter an invalid input before the program exits
	# Initialized to 1
	trials = 0
	# testing for empty inputs, loop forever till the user actually enters meaningful input
	while ((len(shengWord) == 0) == True) or (shengWord.isspace()) == True:

		# TODO: Instead of comming up with an print() error, why not raise an exception instead

		# Print an invalid input error on the screen
		print("\n\t Invalid input.Please enter a Sheng word to proceed! \n ")
		print("\n","*"*75, "\n")
		shengWord = str(input("\n\t PLEASE ENTER A SHENG WORD TO TRANSLATE.\n\n\t Your word: "))
		# Increment the trials by 1
		trials += 1
		if trials >= 3:
			print("\n\t RuntimeShengTranslator has exited after 3 failed attempts.\n")
			print(about.signOff)
			exit()


	# If the input is not empty or a space
	else:

		# Declare the situational languge for translation
		currentLang = chosenLanguage()

		# CASE 1: Test to see whether the input is in Title case, if not, convert it to title case
		if shengWord.istitle() == False:

			# Convert the input from the keyboard into title case
			shengWord = shengWord.title()

			# Check if the word exists in the dictionary keys
			if (shengWord in chosenDictionary().keys()) == True:
				print("\n","*"*75, "\n")
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				# Output the translation string, if you do actually write python code, the line below should be self explanatory
				print("\n\t THE TRANSLATION IS AS FOLLOWS: \n\n\t SHENG         {} \n\n\t '{}' --> '{}'".format(currentLang, shengWord, chosenDictionary()[shengWord]))

				# Print line separator
				print("\n","*"*75, "\n")

				# Offer option to translate the another Sheng word in the same language
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))

				# If user selects yes, run the core logic again
				if translateAnother == 1:
					RuntimeShengTranslator()

				# If the user selects no, print the sign off details and exit app
				elif translateAnother == 2:
					print("\n","*"*75, "\n")
					print(about.signOff)
					print("\n","*"*75, "\n")
					exit()
				# Exit for invalid inputs
				else:
					exit()
			# If the Sheng word does not exist in the chosen dictionary, print the message of no availability
			elif (shengWord in chosenDictionary().keys()) == False:
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				print("\n\t SORRY, NO MATCH WAS FOUND FOR '{}'.".format(shengWord))

				# Append the new word to the submissions list
				submissions.append(shengWord)

				# Print line separator
				print("\n","*"*75, "\n")

				# Offer user the option to translate another Sheng word in the same language
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))

				# If the user selects yes, run core logic again
				if translateAnother == 1:
					RuntimeShengTranslator()
				# If the user selects no, print the sign off message and exit app
				elif translateAnother == 2:
					print("\n","*"*75, "\n")
					print(about.signOff)
					print("\n","*"*75, "\n")
					exit()
				else:
					exit()

		# CASE 2: Run this logic if the the user inputs a Sheng word that is already in title case
		# The code below is self explanatory if you actually do actually write python code
		elif shengWord.istitle() == True:
			if (shengWord in chosenDictionary().keys()) == True:
				print("\n","*"*75, "\n")
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				print("\n\t THE TRANSLATION IS AS FOLLOWS: \n\n\t SHENG         {} \n\n\t '{}' --> '{}'".format(currentLang, shengWord, chosenDictionary()[shengWord]))
				print("\n","*"*75, "\n")
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))
				if translateAnother == 1:
					RuntimeShengTranslator()
				elif translateAnother == 2:
					print("\n","*"*75, "\n")
					print(about.signOff)
					print("\n","*"*75, "\n")
					exit()
				else:
					exit()
			elif (shengWord in chosenDictionary().keys()) == False:
				print("\n\t CHOSEN LANGUAGE: {}\n".format(currentLang))
				print("\n\t SORRY, NO MATCH WAS FOUND FOR'{}'.".format(shengWord))
				submissions.append()
				print("\n","*"*75, "\n")
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))
				if translateAnother == 1:
					RuntimeShengTranslator()
				elif translateAnother == 2:
					print("\n","*"*75, "\n")
					print(about.signOff)
					print("\n","*"*75, "\n")
					exit()
				else:
					exit()

# Calling the core logic of the RuntimeShengTranslator App
RuntimeShengTranslator()