'''2.Message Decrypter
Create a program, that checks if inputs have a valid message and decrypt it. On the first line you will receive a number that indicates
how many inputs you will receive on the next lines.
A message is valid when:
-	There is nothing else before and after it
-	It starts with a tag, which is surrounded by either '$' or '%' (but not both at the same time), the tag itself has to be minimum 3 characters long,
start with a uppercase letter, followed only by lowercase letters
-	There is a colon and a single white space after the tag
-	There are 3 groups consisting of numbers between '[' and ']', followed by a pipe ('|')
Example for a valid message:
"$Request$: [73]|[115]|[32]|"
You must check if the message is valid and if it is- decrypt it, if it isn’t - print the following message:
"Valid message not found!"
Decrypting a message means to take all numbers and turn them into ASCII symbols. After successful decrypt, print it in the following format:
{tag}: {decryptedMessage}
Input
•	On the first line - n - the count of inputs.
•	On the next n lines - input that you have to check if it has a valid message.
Output
•	Print all results from each input, each on a new line.
'''

import re

pattern = r'(((?P<beg>\$)(?P<name>[A-Z][a-z][a-z]+)(\$: )(?P<numbers>\[(\d+)\]\|))(?P<numbers1>\[(\d+)\]\|)(?P<numbers2>\[(\d+)\]\|)+)'
pattern1 = r'((?P<beg>%)(?P<name>[A-Z][a-z][a-z]+)(%: )(?P<numbers>\[(\d+)\]\|))(?P<numbers1>\[(\d+)\]\|)(?P<numbers2>\[(\d+)\]\|)+'

count = int(input())
for i in range(count):

     text = input()

#text = '%Request%: [73]|[115]|[105]|[32]|[75]|'
#text1 = '%Taggy%: [118]|[97]|[108]|'
#text2= '%Taggy$: [73]|[73]|[73]|'
#text3= '$Request$: [73]|[115]|[105]|'



     matches = re.match(pattern, text)
     matches1 = re.match(pattern1, text)
#print(matches)
#print(matches1)

     if not matches and not matches1 :
        print('Valid message not found!')

     elif matches and len(matches.group(0)) > 29:
        print('Valid message not found!')

     elif matches1 and len(matches1.group(0)) > 28:
        print('Valid message not found!')

     elif matches :
        print(f"{matches.group('name')}: {chr(int(matches.group(7))) + chr(int(matches.group(9))) + chr(int(matches.group(11)))}")

     elif matches1 :
          print(f"{matches1.group('name')}: {chr(int(matches1.group(6))) + chr(int(matches1.group(8))) + chr(int(matches1.group(10)))}")