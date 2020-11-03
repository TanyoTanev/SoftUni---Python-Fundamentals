'''5.Write a program to calculate the total cost of different types of furniture. You will be given some lines of input until
you receive the line &quot;Purchase&quot;. For the line to be valid it should be in the following format:
&quot;&gt;&gt;{furniture name}&lt;&lt;{price}!{quantity}&quot;
The price can be floating point number or whole number. Store the names of the furniture and the total price. At the
end print the each bought furniture on separate line in the format:
&quot;Bought furniture:
{1 st name}
{2 nd name}
…&quot;
And on the last line print the following: &quot;Total money spend: {spend money}&quot; formatted to the second decimal
point.
'''

import re

pattern = r'>>(?P<product>[A-Za-z]+)<<(?P<price>[0-9]+\.?[0-9]+)!(?P<quantity>[0-9]+)'

text = ''
products = []

while True:

    commmand = input()

    if commmand == 'Purchase':
        break
    text = text + commmand
    matches = re.findall(pattern, text)

total_cost = 0
print("Bought furniture:")

for i in range(len(matches)):

    products.append(matches[i][0])
    total_cost = total_cost + float(matches[i][1])*int(matches[i][2])
    print(products[i])


print(f"Total money spend: {total_cost:.2f}")