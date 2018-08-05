#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*        RUNTIME SHENG TRANSLATOR - ENGLISH TRACK        *
#	++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#	*  Welcome to Runtime Sheng translator. v1.0.0           *
#	*  MIT License, Copyright(c) 2018, Antony Muga           *
#	*  All Rights Reserved.                                  *
#	*  Author: Antony Muga                                   *
#	----------------------------------------------------------
#	*  Project's Links:                                      *
#	*  Twitter: https://twitter.com/RuntimeClubKe            *
#	*  Runtime Club on LinkedIn                              *
#	*  Runtime Club on Github                                *
#	*  RuntimeTranslate project on GitHub                    *
#	----------------------------------------------------------
#	*  Personal social links:                                *
#	*  GitHub: https://github.com/antonymuga/                *
#	*  Website: https://antonymuga.github.io                 *
#	*  LinkedIn: https://www.linkedin.com/in/antony-muga/    *
#	*  Email: https://sites.google.com/view/antonymuga/home  *
#	----------------------------------------------------------

import sys

# Import the project details
import About

# Import the dictionaries for the different languages
from Dictionaries import ToEng # English dictionary
from Dictionaries import ToFre # French dictionary
from Dictionaries import ToGer # German dictionary
from Dictionaries import ToSpa # Spanish dictionary
from Dictionaries import ToIta # Italian dictionary

# Print line separator
print("\n","*"*75, "\n")

# Print the project details
print(About.projectDetails)

# Print line separator for diffrent sections
print("\n","*"*75, "\n")


# Declare a tuple that contains all the imported dictionaries
dictionaryList = (ToEng.shengToEng, ToFre.shengToFre, ToGer.shengToGer, ToSpa.shengToSpa, ToIta.shengToIta)


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
			Invalid input.RuntimeTranslate is exiting!
			""")
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
def RuntimeTranslate():

	# Call the chosen dictionary
	chosenDictionary()

	# Call the shosen language
	chosenLanguage()
	# Declaration of the Sheng to english dictionary
	submissions = []

	# Enter the search string, only one word is supported for now
	searchItem = str(input("""
	NOTE: Currently, only single words are supported.
	More features will be added in through course of 
	development.

	PLEASE ENTER A SHENG WORD TO TRANSLATE.

	Your word: """))

	
	# testing for empty inputs, loop forever till the user actually enter meaningful output
	while (len(searchItem) == 0) or (searchItem == "") or (searchItem == " ") or (searchItem.isspace())== True:
		print("\n\t Invalid input.Please enter a word to proceed! \n ")
		print("\n","*"*75, "\n")
		searchItem = str(input("\n\t PLEASE ENTER A SHENG WORD TO TRANSLATE.\n\n\t Your word: "))


	# If the input is not empty or a space
	else:

		# Declare the situational languge for translation
		currentLang = chosenLanguage()

		# CASE 1: Test to see whether the input is in Title case, if not, convert it to title case
		if searchItem.istitle() == False:

			# Convert the input from the keyboard into title case
			searchItem = searchItem.title()

			# Check if the word exists in the dictionary keys
			if (searchItem in chosenDictionary().keys()) == True:
				print("\n","*"*75, "\n")
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				# Output the translation string, if you write python code the line below should be self explanatory
				print("\n\t THE TRANSLATION IS AS FOLLOWS: \n\n\t SHENG         {} \n\n\t '{}' --> '{}'".format(currentLang, searchItem, chosenDictionary()[searchItem]))

				# Print line separator
				print("\n","*"*75, "\n")

				# Offer option to translate the same word in the same language
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))

				# If user selects yes, run the core logic again
				if translateAnother == 1:
					RuntimeTranslate()

				# If the user selects no, print the sign off details and exit app
				elif translateAnother == 2:
					print(About.signOff)
					exit()
				# Exit for invalid inputs
				else:
					exit()
			# If the word does not exist in the chosen dictionary, print the message of no availability
			elif (searchItem in chosenDictionary().keys()) == False:
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				print("\n\t SORRY, NO MATCH WAS FOUND FOR '{}'.".format(searchItem))

				# Append the new word to the submissions list
				submissions = []
				submissions.append(searchItem)

				# Print line separator
				print("\n","*"*75, "\n")

				# Offer user the option to translate another word in the same language
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))

				# If the user selscts yes, run core logic again
				if translateAnother == 1:
					RuntimeTranslate()
				# If the user selects no, print the sign off message and exit app
				elif translateAnother == 2:
					print(About.signOff)
					exit()
				else:
					exit()

		# CASE 2: Run this logic if the the user inputs a word that is already in title case
		# The code below is self explanatory if you actually do write python code
		elif searchItem.istitle() == True:
			if (searchItem in chosenDictionary().keys()) == True:
				print("\n","*"*75, "\n")
				print("\n\t LANGUAGE: {}\n".format(currentLang))
				print("\n\t THE TRANSLATION IS AS FOLLOWS: \n\n\t SHENG         {} \n\n\t '{}' --> '{}'".format(currentLang, searchItem, chosenDictionary()[searchItem]))
				print("\n","*"*75, "\n")
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))
				if translateAnother == 1:
					RuntimeTranslate()
				elif translateAnother == 2:
					print(About.signOff)
					exit()
				else:
					exit()
			elif (searchItem in chosenDictionary().keys()) == False:
				print("\n\t CHOSEN LANGUAGE: {}\n".format(currentLang))
				print("\n\t SORRY, NO MATCH WAS FOUND FOR'{}'.".format(searchItem))
				submissions = []
				submissions.append()
				print("\n","*"*75, "\n")
				translateAnother = int(input("\n\t TRANSLATE ANOTHER SHENG WORD TO {}? \n\t \n\t 1: Yes \n\n\t 2: No \n\n\t Select: ".format(currentLang)))
				if translateAnother == 1:
					RuntimeTranslate()
				elif translateAnother == 2:
					print(About.signOff)
					exit()
				else:
					exit()

# Calling the core logic of the RuntimeTranslate App
RuntimeTranslate()


