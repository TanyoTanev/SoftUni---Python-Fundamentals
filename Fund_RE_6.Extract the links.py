'''6.Extract the links

Write a program that extracts links from a given text. The text will come in the form of strings, each
representing a sentence. You need to extract only the valid links from it. Example:

&quot;www.internet.com&quot;

Sub-Domain Domain name Domain

extension

The Sub-Domain must always be &quot;www&quot;. The Domain name can consist of English alphabet letters
(uppercase and lowercase), digits and dashes (&quot;–&quot;). The Domain extension consists of one or more
domain blocks, a domain block consists of a dot followed by one or more lowercase English alphabet
letters, a Domain extension must have at least one domain block in order to be valid. The Sub-Domain
and Domain name must be separated by a single dot. Any link that does NOT follow the specified above
rules should be treated as invalid.
'''

import re

pattern = r'(?P<domain>www.[A-Za-z-0-9]+)(?P<extendion>[.A-Za-z]+)'
text = ''


while True:
    line = input()
    text = text + ' '+ line
    if not line:
        break



matches = re.findall(pattern, text, flags=re.RegexFlag.IGNORECASE)

for i in range(len(matches)):
    if len(matches[i][1]) > 1:
        print(''.join(matches[i]))