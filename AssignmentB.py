# Preliminary dictionary to store given translated words
vocabulary = {
    'hello': {'French': 'bonjour', 'German': 'hallo'},
    'yes': {'French': 'oui', 'German': 'jawohl'},
    'no': {'French': 'non', 'German': 'nein'},
    'yellow': {'French': 'jaune', 'German': 'gelb'},
    'dog': {'French': 'chien', 'German': 'hund'},
    'table': {'French': 'table', 'German': 'tisch'},
    'book': {'French': 'livre', 'German': 'buchen'}}

# Gets initial word to be translated
word = input('Please enter an English word ')

# if word entered exists in the vocabulary dictionary
if word in vocabulary:
	print('I will give you the French and German translations:', word)
	translation = vocabulary[word] 
	#prints the translations
	print('The French translation is ', {translation['French']})
	print('The German translation is ', {translation['German']})

# if the word entered does not exist in the vocab dictionary, prints an error message
else:
	print('Error, This english word ', word, ' is not in my vocabulary!')
	