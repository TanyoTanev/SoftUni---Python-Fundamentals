'''* Feed the Animals

The sanctuary needs to provide food for the animals and feed them, so your task is to help with the process
Create a program that organizes the daily feeding of animals. You need to keep information about animals, their daily food limit
 and the areas of the Wildlife Refuge they live in. You will be receiving lines with commands until you receive the "Last Info" message.
There are two possible commands:

"Add:{animalName}:{dailyFoodLimit}:{area}":
Add the animal and its daily food limit to your records. It is guaranteed that the names of the animals are unique and there will never be
animals with the same name. If it already exists, just increase the value of the daily food limit with the current one that is given.

"Feed:{animalName}:{food}:{area}":
Check if the animal exists and if it does, reduce its daily food limit with the given food for feeding. If its limit reaches 0 or less,
the animal is considered successfully fed and you need to remove it from your records and print the following messageAdd:Jamie:1290:RiverArea:

"{animalName} was successfully fed"
You need to know the count of hungry animals there are left in each area in the end. If an animal has daily food limit above 0, it is considered hungry.

In the end, you have to print each animal with its daily food limit sorted in descending order by the daily food limit and then by its name
in ascending order in the following format:

Animals:

{animalName} -> {dailyFoodLimit}g

{animalName} -> {dailyFoodLimit}g

Afterwards, print the areas with the count of animals, which are not fed in descending order by the count of animals. If an area has 0 hungry animals in it, don't print it. The output must be in the following format:

Areas with hungry animals:

{areaName} : {countOfUnfedAnimals}

{areaName} : {countOfUnfedAnimals}

Input / Consrtaints

You will be receiving lines until you receive the "Last Info" command.
The food comes in grams and is an integer number in the range [1...100000].
The input will always be valid.
There will never be a case, in which an animal is in two or more areas at the same time.

Output

Print the appropriate message after the "Feed" command, if an animal is fed.
Print the animals with their daily food limit in the format described above.
Print the areas with the count of unfed animals in them in the format described above.

Examples
Add:Maya:7600:WaterfallArea
Add:Bobbie:6570:DeepWoodsArea
Add:Adam:4500:ByTheCreek
Add:Jamie:1290:RiverArea
Add:Gem:8730:WaterfallArea
Add:Maya:1230:WaterfallArea
Add:Jamie:560:RiverArea
Feed:Bobbie:6300:DeepWoodsArea
Feed:Adam:4650:ByTheCreek
Feed:Jamie:2000:RiverArea

Last Info'''

#string = input() #'Feed:Bobbie:6300:DeepWoodsArea'#'Add:Maya:7600:WaterfallArea'
#message = string.split(':')
#print(message)
#animals = [[0]] * 4

animals = [[], [], [], []]
#print(animals)


while True:

    string = input()
    message = string.split(':')


    if message[0]=='Last Info':
       break

    elif message[0]=='Add':
        res = [i for i in range(len(animals[1])) if animals[1][i] == message[1]]
        #print(res)
        if res: #animals[1][:] == message[1]:
         animal_index = (max(res))
         #print(animal_index)
         animals[2][animal_index] = animals[2][animal_index]+int(message[2])

        else:
         animals[1].append(message[1])
         animals[2].append(int(message[2]))
         animals[3].append(message[3])

    elif message[0]== 'Feed':
         res = [i for i in range(len(animals[1])) if animals[1][i] == message[1]]
         if res:  # animals[1][:] == message[1]:
            animal_index = (max(res))
         # print(animal_index)
            animals[2][animal_index] = animals[2][animal_index] - int(message[2])
            if animals[2][animal_index] <=0:
                print(f"{animals[1][animal_index]} was successfully fed")
                animals[1].pop(animal_index)
                animals[2].pop(animal_index)
                animals[3].pop(animal_index)

animals_2 = [[],[]] # необходимо за сортиране на зоните


sorted_area = [[0]*len(animals[3]) for i in range(2)]

#print(animals_2)

[animals_2[0].append(i) for i in animals[3]]

#print(animals_2)
#print(res)


#СОРТИРАНЕ НА НЕНАХРАНЕНИТЕ ЖИВОТНИ
sorted_animals = [[] for i in range(len(animals))]
a=0
while len(animals)>0:

#print(max(animals[2]))
 if len(animals[2])>0:
    sorted_animals[1].append(max(animals[2]))
#print(sorted_animals[1])
    a=animals[2].index(max(animals[2]))
#print(a)
    sorted_animals[0].append(animals[1][a])
    sorted_animals[3].append(animals[3][a])
    animals[1].pop(a)
    animals[2].pop(a)
    animals[3].pop(a)

    #print(animals)
 else:
     break

#print(f"сортираното е :{sorted_animals}")
print(f"Animals:")
for i in range(len(sorted_animals[1])):
    print(f"{sorted_animals[0][i]} -> {sorted_animals[1][i]}g")


#print(animals_2)
#print(animals)

#СОРТИРАНЕ НА ЗОНИТЕ
area = [[0]*len(sorted_area[1]) for i in range(2)]
#print(area)

for i in range(len(animals_2[0])):
    if area[0].count(animals_2[0][i]):
        pass
    else:
       area[0][i]=animals_2[0][i]

#print(area)

for i in range(len(area[0])):
    if area[0][i]!=0:
        area[1][i]=animals_2[0].count(area[0][i])
#print(animals_2)

#СОРТИРАНЕ НА ЗОНИТЕ В НАМАЛЯВАЩ РЕД
#print(sorted_area)
sorted_area = [[],[]]

while len(area[0])>0:


 if len(area[0])>0:
    sorted_area[1].append(max(area[1]))
#print(sorted_animals[1])
    a=area[1].index(max(area[1]))
#print(a)
    sorted_area[0].append(area[0][a])
    #sorted_area[1].append(area[1][a])
    area[0].pop(a)
    area[1].pop(a)


    #print(animals)
 else:
     break

#print(sorted_area)
#КРАЙ СОРТИРАНЕ


print(f"Areas with hungry animals:")
for i in range(len(sorted_area[0])):
    if sorted_area[0][i]:
        print(f"{sorted_area[0][i]} : {sorted_area[1][i]}")

