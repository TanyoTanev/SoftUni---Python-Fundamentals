'''Big Numbers Lover

You really like big numbers, so you always find a way to form one from numbers given to you
You will receive a single line containing numbers separated by a single space. Form the biggest number possible from them
'''

string = '3 30 34 5 9'  #
list_1 = string.split(' ')
list_2 = []
print(list_1)


for i in range(len(list_1)):

    res = [int(j) for j in str(list_1[i])]
    list_2.append(res)

print(list_2)

# take the second element for sort
def take_element(elem):
    return elem[0]

# random list
#random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(list_2, reverse = True, key = take_element)
print(sorted_list)


print(len(sorted_list[3]))

