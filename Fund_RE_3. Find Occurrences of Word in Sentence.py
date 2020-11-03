'''3.
Write a program that finds, how many times a given word, is used in a given sentence. Note that letter case does
not matter – it is case-insensitive.
The output is a single number indicating the amount of times the sentence contains the word.
'''

import re

#text = 'The waterfall was so high, that the child couldn&#39;t see its peak.'
#pattern = 'the'

text = input() #'How do you plan on achieving that? How? How can you even think of that?'
pattern =input()  #'how'

#text = 'There was one. Therefore I bought it. I wouldn&#39;t buy it otherwise.'
#pattern = 'there'


matches = re.findall(rf"\b{pattern}\b", text, re.IGNORECASE)
#the_list = re.compile(pattern, re.I)

print(len(matches))
