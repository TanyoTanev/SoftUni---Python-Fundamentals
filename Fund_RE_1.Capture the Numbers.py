'''1.Capture the Numbers
0 +Write a program that finds all numbers in a sequence of strings.
The output is all the numbers, extracted and printed on a single line – each separated by a single space.
'''

import re
pattern = '[0-9]+'

text = ''



while True:
    line = input()
    text = text + ' '+ line
    if not line:
        break

matches = re.findall(pattern, text)#, flags=re.RegexFlag.MULTILINE)

print(' '.join(matches))