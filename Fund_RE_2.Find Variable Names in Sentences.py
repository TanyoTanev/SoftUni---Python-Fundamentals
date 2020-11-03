'''2. Find Variable Names in Sentences
Write a program that finds all variable names in a given string. A variable name starts with an underscore (&quot;_&quot;) and
contains only Capital and Non-Capital English Alphabet letters and digits. Extract only their names, without the
underscore. Try to do this only with regular expressions.
The output consists of all variable names, extracted and printed on a single line, each separated by a comma.
'''
import re
#\b[_]([a-zA-Z]*\b)
pattern = r'\b[_](?P<word>[a-zA-Z]+\b)'

text = '''The _id and _age variables are both integers.'''
text1= '''Calculate the _area of the _perfectRectangle object.'''
text2 = '''__invalidVariable _evenMoreInvalidVariable_
_validVariable'''

string = input()

matches = re.findall(pattern, string)

print(','.join(matches))
    #print(f'{word}')