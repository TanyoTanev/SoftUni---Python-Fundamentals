'''Hello, France
The budget was enough to get them to Frankfurt and they have some money left, but their final aim is to go to France, which means that they
will need more finances. They’ve decided to make profit by buying items on discount from the Thrift Shop and selling them for a higher price.
You must help them.
Create a program that calculates the profit after buying some items and selling them on a higher price. In order to fulfil that, you are going
to need certain data - you will receive a collection of items and a budget in the following format:

{type->price|type->price|type->price……|type->price}

{budget}
The prices for each of the types cannot exceed a certain price, which is given bellow:

Type

Maximum Price

Clothes
50.00

Shoes
35.00

Accessories
20.50

If a price for a certain item is higher than the maximum price, don’t buy it. Every time you buy an item, you have to reduce the budget
with the value of its price. If you don’t have enough money for it, you can’t buy it. Buy as much items as you can.

You have to increase the price of each of the items you have successfully bought with 40%. Print the list with the new prices and the
profit you will gain from selling the items. They need exactly 150$ for tickets for the train, so if their budget after selling the products
is enough – print – "Hello, France!" and if not – "Time to go."

Input / Constraints

On the 1st line you are going to receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]'''

string = input()
products = string.split('|')
budget = int(input())
budget_in_the_beggining = budget
#a=0

for i in range(len(products)):
    products[i] = products[i].split('->')

#print(products)
i=0
while i < len(products):

  if products[i][0] == 'Clothes':
      if float(products[i][1]) > 50.00:
           products.remove(products[i])
           i-=1

  elif products[i][0] == 'Shoes':
      if float(products[i][1]) > 35.00:
           products.remove(products[i])
           i -= 1

  elif products[i][0] == 'Accessories':
      if float(products[i][1]) > 20.50:
           products.remove(products[i])
           i -= 1

  i+=1
#print(products)

i = 0


while i < len(products):
    if budget >=float(products[i][1]) and budget > 0:
        budget= budget - float(products[i][1])
        #effort=effort + int(fire[i][1])
    else:
        products.remove(products[i])
        i -= 1
    i+=1

profit = 0

for i in range(len(products)):
    print(f"{float(products[i][1])*1.4:.2f}",end=' ')
    profit = profit + float(products[i][1])*1.4
print(f"\nProfit: {profit-budget_in_the_beggining+budget:.2f}")

if profit + budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")