'''* On the Way to Annapurna

You’ve hired a Sherpa and he has a list of supplies you both need to go on the way. He has passed you some notes and you have to order them
correctly in a diary before you start circling around the town’s stores.

Create a program, that lists stores and the items that can be found in them. You are going to be receiving commands with the information
you need until you get the "End" command. There are three possible commands:

"Add->{Store}->{Item}"
Add the store and the item in your diary. оIf the store already exists, add just the item.
"Add->{Store}->{Item},{Item1}…,{ItemN}"
Add the store and the items to your notes. If the store already exists in the diary – add just the items to it.
"Remove->{Store}"
Remove the store and its items from your diary, if it exists.
In the end, print the collection sorted by the count of the items in descending order and then by the names of the stores, again,
in descending order in the following format:

Stores list:

{Store}
<<{Item}>>
<<{Item}>>

<<{Item}>>
Input / Constraints
You will be receiving information until the “END” command is given.
There will always be at least one store in the diary.
Input will always be valid, there is no need to check it explicitly.

Output
Print the list of stores in the format given above.
Add->PeakSports->Map,Navigation,Compass
Add->Pharmacy->Pain-killers
Add->Groceries->Nuts
Add->Groceries->Nuts
Add->Paragon->Tent
Remove->Paragon
END
'''


shops = []
items = []

while True:

    string = input()
    command = string.split('->')

    #print(command)

    if command[0]=='END':
       break

    elif command[0]=='Add':
        items_to_add = command[2].split(',')
        res = [shops.index(i) for i in shops if i == command[1]]
        #print(res)
        #print(items)
        if res:
           shop_index = (max(res))
           items[shop_index] = items[shop_index] + items_to_add
        else:
            shops.append(command[1])
            items.append(items_to_add)

    elif command[0]=='Remove':
           #items_to_remove = command[2].split(',')
           res = [shops.index(i) for i in shops if i == command[1]]
        #print(res)
        #print(items)
           if res:
            shop_index = (max(res))
            if len(shops) > 1:
             shops.pop(shop_index)
             items.remove(items[shop_index])
            #else:
               # items.pop(items_to_remove)



#print(shops)
#print(items)


#СОРТИРАНЕ

#sort_alphabetical= []
sort_alphabetical = [[0] for i in range(len(shops))]
#print(sort_alphabetical)

for i in range(len(shops)):
    sort_alphabetical[i] = shops[i]
    for j in range(len(items[i])):
     sort_alphabetical[i] = sort_alphabetical[i] + '+' +items[i][j]

#print(sort_alphabetical)
sort_alphabetical.sort(reverse=True)
#print(sort_alphabetical)

for i in range(len(shops)):
    shops_to_add = sort_alphabetical[i].split('+')
    shops[i]=shops_to_add[0]
    shops_to_add.pop(0)
    items[i] =  shops_to_add

#print(shops)
#print(items)

sorted_shops = []
sorted_items = []


while len(shops)>0:


 if len(shops)>0:
     list_len = [len(i) for i in items]
     index_max=list_len.index(max(list_len))

     sorted_items.append(items[index_max])
     sorted_shops.append(shops[index_max])

     shops.pop(index_max)
     items.remove(items[index_max])



print(f"Stores list:")

for i in range(len(sorted_shops)):
    print(f"{sorted_shops[i]}")
    for j in range(len(sorted_items[i])):
     print(f"<<{sorted_items[i][j]}>>")