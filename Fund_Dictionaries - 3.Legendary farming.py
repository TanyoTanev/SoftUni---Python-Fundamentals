'''Legendary Farming

You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a tedious process and it requires
quite a bit of farming. Anyway, you are not too pretentious – any legendary item will do. The possible items are:

Shadowmourne – requires 250 Shards;
Valanyr – requires 250 Fragments;
Dragonwrath – requires 250 Motes;

Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input, in the format:

2 motes 3 ores 15 stones

Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to print that the corresponding
legendary item is obtained. Then, print the remaining shards, fragments, motes, ordered by quantity in descending order, then by name in ascending
order, each on a new line. Finally, print the collected junk items in alphabetical order.

Input
Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
Output

On the first line, print the obtained item in the format: {Legendary item} obtained!
On the next three lines, print the remaining key materials in descending order by quantity
If two key materials have the same quantity, print them in alphabetical order
On the final several lines, print the junk items in alphabetical order
All materials are printed in format {material}: {quantity}
The output should be lowercase, except for the first letter of the legendary

Examples
Input
Output

3 Motes 5 stones 5 Shards
6 leathers 255 fragments 7 Shards

Valanyr obtained!
fragments: 5
shards: 5
motes: 3
leathers: 6
stones: 5


123 silver 6 shards 8 shards 5 motes
9 fangs 75 motes 106 MOTES 8 Shards
86 Motes 7 stones 19 silver

Dragonwrath obtained!
shards: 22
motes: 19
fragments: 0
fangs: 9
silver: 123
'''

ll = []
materials = {'shards': 0 , 'fragments': 0, 'motes': 0 }
junk = dict()


while materials['shards'] < 250 and materials['fragments'] < 250 and materials['motes'] < 250:

   ll = [x.lower() for x in input().split(' ')]
   #print(ll)


   for i in range(1,len(ll),2):
       if ll[i] in materials:
          if materials[ll[i]] + int(ll[i-1]) >= 250:
             materials[ll[i]] =  materials[ll[i]] + int(ll[i-1])
             break
          else:
              materials[ll[i]] = materials[ll[i]] + int(ll[i - 1])
       else:
            if ll[i] in junk:
                junk[ll[i]] += int(ll[i-1])
            else:
                 junk[ll[i]] = int(ll[i-1])




if materials['fragments'] > 250:
    materials['fragments'] -=250
    print('Valanyr obtained!')
elif materials['shards'] > 250:
    materials['shards'] -= 250
    print('Shadowmourne obtained!')
else:
    materials['motes'] -=250
    print('Dragonwrath obtained!')

#print(materials)
#print(junk)

sorted_materials = dict(sorted(materials.items(), key=lambda x: (-x[1], x[0])))
sorted_junk = dict(sorted(junk.items(), key=lambda x:x[0]))

[ print(f"{material}: {sorted_materials[material]}") for material in sorted_materials]
[ print(f"{material}: {junk[material]}") for material in sorted_junk]
#print(sorted_materials)
