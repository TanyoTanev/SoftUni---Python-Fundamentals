'''
	*Array Manipulator

Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of integers.
 He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of money, though, and he is willing
 to give somebody half of it if to help him do his job. You, on the other hand, love arrays (and money) so you decide to try your luck.

The array may be manipulated by one of the following commands

exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays.
E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
If the index is outside the boundaries of the array, print "Invalid index"
max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
If there are two or more equal min/max elements, return the index of the rightmost one
If a min/max even/odd element cannot be found, print "No matches"
first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
If the count is greater than the array length, print "Invalid count"
If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"
end – stop taking input and print the final state of the array

Input

The input data should be read from the console.
On the first line, the initial array is received as a line of integers, separated by a single space
On the next lines, until the command "end" is received, you will receive the array manipulation commands
The input data will always be valid and in the format described. There is no need to check it explicitly.

Output

The output should be printed on the console.
On a separate line, print the output of the corresponding command
On the last line, print the final array in square brackets with its elements separated by a comma and a space
See the examples below to get a better understanding of your task

1 3 5 7 9
exchange 1
max odd
min even
first 2 odd
last 2 even
exchange 3
end

1 10 100 1000
max even
first 5 even
exchange 10
min odd
exchange 0
max even
min even
end

1 10 100 1000
exchange -1
first 2 odd
last 4 odd
end

'''


import sys
#max = sys.maxsize
#min = -sys.maxsize - 1

list_numbers = list(map(int, input().split(" ")))

def exhange_index(idx):
    global list_numbers

    '''exchange {index} – splits the array after the given index, and exchanges the places of the two resulting sub-arrays.
E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
If the index is outside the boundaries of the array, print "Invalid index"'''
    if idx<0 or idx>= len(list_numbers):
        print("Invalid index")
        return

   # list1=[]
  #  list2=[]

   # list1= list_numbers [0:idx+1]
   # list2 =list_numbers [idx+1:]
    list_numbers =list_numbers[idx+1:] + list_numbers[:idx+1]

    #print(list_numbers)
    #return list_numbers

def max_odd():
    global list_numbers
    max_odd_num = -sys.maxsize -1

    for i in range(len(list_numbers)):
       if list_numbers[i] % 2 > 0 and max_odd_num <= list_numbers[i]:
            max_odd_num = list_numbers[i]
    if max_odd_num == -sys.maxsize -1:
                print("No matches")
                return
    else:
              return print(list_numbers.index(max_odd_num))

def max_even():
    max_even_num = -sys.maxsize -1
    global list_numbers

    for i in range(len(list_numbers)):
       if list_numbers[i] % 2 == 0 and max_even_num <= list_numbers[i]:
            max_even_num = list_numbers[i]

    if max_even_num == -sys.maxsize -1:
                print("No matches")
                return
    else:
              return print(list_numbers.index(max_even_num))

def min_odd():
    min_odd_num = sys.maxsize
    global list_numbers

    for i in range(len(list_numbers)):
       if list_numbers[i] % 2 > 0 and min_odd_num >= list_numbers[i]:
            min_odd_num = list_numbers[i]

    if min_odd_num == sys.maxsize:
                print("No matches")
                return
    else:
              return print(list_numbers.index(min_odd_num))


def min_even():
    global list_numbers
    min_even_num = sys.maxsize

    for i in range(len(list_numbers)):
       if list_numbers[i] % 2 == 0 and min_even_num >= list_numbers[i]:
            min_even_num = list_numbers[i]

    if min_even_num == sys.maxsize:
        print("No matches")
        return
    else:
        return print(list_numbers.index(min_even_num))

'''first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
If the count is greater than the array length, print "Invalid count"
If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty array "[]"
end – stop taking input and print the final state of the array
'''
def first_even(count ):
    even_list=[]
    count_times =0
    global list_numbers

    if count > len(list_numbers):
        print("Invalid count")
        return

    for i in range(len(list_numbers)):
        if list_numbers[i] % 2 == 0 and count_times < count:
            even_list.append(list_numbers[i])
            count_times+=1
    print(even_list)

def first_odd(count):
    even_list=[]
    count_times =0
    global list_numbers

    if count > len(list_numbers):
        print("Invalid count")
        return

    for i in range(len(list_numbers)):
        if list_numbers[i] % 2 > 0 and count_times < count:
            even_list.append(list_numbers[i])
            count_times+=1
    print(even_list)

def last_odd(count):
    odd_list = []
    count_times = 0
    global list_numbers

    if count > len(list_numbers):
        print("Invalid count")
        return

    for i in range(len(list_numbers)-1,-1,-1):
        if list_numbers[i] % 2 > 0 and count_times < count:
            odd_list.append(list_numbers[i])
            count_times += 1
    odd_list.reverse()
    print(odd_list)

def last_even(count):
    even_list = []
    count_times = 0
    global list_numbers

    if count > len(list_numbers):
        print("Invalid count")
        return

    for i in range(len(list_numbers)-1,-1,-1):
        if list_numbers[i] % 2 == 0 and count_times < count:
            even_list.append(list_numbers[i])
            count_times += 1
    even_list.reverse()
    print(even_list)


def calling():
    global list_numbers
    while True:

        string = input()
        command = string.split(' ')


        if command[0]=='end':
           #print(list_numbers)
           break

        elif command[0]== 'exchange':
            exhange_index(int(command[1]))

        elif command[0] == 'max':
            if command[1] == 'even':
                max_even()
            elif command[1] == 'odd':
                max_odd()

        elif command[0]=='min':
            if command[1] == 'even':
                min_even()
            elif command[1] == 'odd':
                min_odd()

        elif command[0] == 'first':
            if command[2] == 'odd':
                first_odd(int(command[1]))
            elif command[2]== 'even':
                first_even(int(command[1]))

        elif command[0]== 'last':
            if command[2] == 'odd':
                last_odd(int(command[1]))
            elif command[2] == 'even':
                last_even(int(command[1]))
    return print(list_numbers)

if __name__ == '__main__':


   # string=input()
    #list_numbers = string.split(' ')

   #for i in range (len(list_numbers)):
        #if list_numbers[i].isdigit():
    #       list_numbers[i]=int(list_numbers[i])

    #command = input()
    #command = command.split(' ')

    #exhange_index(10, list_numbers)
    calling()
    #first_even(5, list_numbers)
   # print(list_numbers)
    #command = input()
    #command = command.split(' ')
  #  list_numbers = [1, 4, 8, 2, 3]
    #exhange_index(2,[1, 2, 3, 4, 5])
  #  print(max_odd(list_numbers))
  #  print(max_even(list_numbers))
    #print(min_odd(list_numbers))
    #print(min_even(list_numbers))
   # first_even(2, [1, 8, 2, 3])
  # first_odd(2, [1, 8, 2, 3])
   # last_even(2,[1, 8, 2, 3])
  #  last_odd(2, [1, 8, 2, 3])

    #print(list_numbers)

