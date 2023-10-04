import re

# txt = "The rain in Spain"

# #Find all lower case characters alphabetically between "a" and "m":
'''
Write a Python program that matches a word containing 'z',
not the start or end of the word.
'''
# x = re.findall("[a-m]", txt)
# print(sorted(x))

text = "Zebra"

pattern = r'\b\w*z\w*\b'

matches = re.findall(pattern, text, re.IGNORECASE )
for i in matches:
    print(i)
else:
    print(None)


    '''
    dates    
    '''