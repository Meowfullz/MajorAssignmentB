# Preliminary dictionary to store given translated words
vocabulary = {
    'hello': {'French': 'bonjour', 'German': 'hallo'},
    'yes': {'French': 'oui', 'German': 'jawohl'},
    'no': {'French': 'non', 'German': 'nein'},
    'yellow': {'French': 'jaune', 'German': 'gelb'},
    'dog': {'French': 'chien', 'German': 'hund'},
    'table': {'French': 'table', 'German': 'tisch'},
    'book': {'French': 'livre', 'German': 'buchen'}}


word = input('Please enter an English word ')


if word in vocabulary:
	print('I will give you the French and German translations:', word)
	translation = vocabulary[word] 
	print('The French translation is ', {translation['French']})
	print('The German translation is ', {translation['German']})

else:
	print('Error, This english word ', word, ' is not in my vocabulary!')
	