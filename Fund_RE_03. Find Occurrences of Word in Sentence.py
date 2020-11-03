'''3.
Write a program that finds, how many times a given word, is used in a given sentence. Note that letter case does
not matter – it is case-insensitive.
The output is a single number indicating the amount of times the sentence contains the word.
'''

import re

text = 'The waterfall was so high, that the child couldn&#39;t see its peak.'
pattern = 'the'

matches = re.findall(pattern, text)

print(matches)