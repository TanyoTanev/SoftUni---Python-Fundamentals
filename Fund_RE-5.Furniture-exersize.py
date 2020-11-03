'''5.Furniture- retake for exersize
Write a program to calculate the total cost of different types of furniture. You will be given some lines of input until you receive the
line "Purchase". For the line to be valid it should be in the following format:
">>{furniture name}<<{price}!{quantity}"

The price can be floating point number or whole number. Store the names of the furniture and the total price. At the end print the each bought
 furniture on separate line in the format:
"Bought furniture:
{1st name}
{2nd name}
…"
And on the last line print the following: "Total money spend: {spend money}" formatted to the second decimal point.
'''

import re

#pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>[0-9]+\.?[0-9]+)!(?P<quantity>[0-9]+)'
pattern = r'>{2}(?P<furniture>[a-zA-Z]+)<{2}(?P<price>[0-9]+\.*[0-9]*)!{1}(?P<quantity>[0-9]+)'
text = ''


while True:

  command = input()
  if command == 'Purchase':
      break

  text = text + command
  matches = re.findall(pattern, text)

#print(command)
#print(matches)
print("Bought furniture:")

total_sum = 0

for match in matches:
    print(match[0])
    #print(match[1])
    #print(match[2])
    total_sum += float(match[1])*int(match[2])

print(f"Total money spend: {total_sum:.2f}")