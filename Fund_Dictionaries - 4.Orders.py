'''Orders

Write a program that keeps information about products and their prices. Each product has a name, a price and a quantity.
If the product doesn't exist yet, add it with its starting quantity.
If you receive a product, which already exists, increase its quantity by the input quantity and if its price is different, replace the price as well.
You will receive products' names, prices and quantities on new lines. Until you receive the command "buy", keep adding items. When you do receive
the command "buy", print the items with their names and total price of all the products with that name.

Input
Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
The product data is always delimited by a single space.

Output
Print information about each product in the following format:
"{productName} -> {totalPrice}"
Format the average grade to the 2nd digit after the decimal separator.

Examples
Input
Output

Beer 2.20 100
IceTea 1.50 50
NukaCola 3.30 80
Water 1.00 500
buy

Beer -> 220.00
IceTea -> 75.00
NukaCola -> 264.00
Water -> 500.00

Beer 2.40 350
Water 1.25 200
IceTea 5.20 100
Beer 1.20 200
IceTea 0.50 120
buy

Beer -> 660.00
Water -> 250.00
IceTea -> 110.00

CesarSalad 10.20 25
SuperEnergy 0.80 400
Beer 1.35 350
IceCream 1.50 25
buy

CesarSalad -> 255.00
SuperEnergy -> 320.00
Beer -> 472.50
IceCream -> 37.50
'''

products = {}

#command = input().split(' ')
#products = {'gosho': [1, 2], 'peter': [3,4] }

while True:

    command = input().split(' ')
    if command[0] == 'buy':
        break

    else:

        if command[0] not in products:
            products[command[0]] = [float(command[1]), int(command[2])]
        elif products[command[0]] == float(command[1]):
            products[command[0]][1] += int(command[2])
        else:
            products[command[0]][0] = float(command[1])
            products[command[0]][1] +=int(command[2])
    #print(products)

#print(products)
#print(products['gosho'][1])

[print(f"{product} -> {products[product][0]*products[product][1]:.2f}") for product in products]