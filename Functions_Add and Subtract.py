'''Add and Subtract

You will receive three integer numbers.
Write a function sum_numbers() to get the sum of the first two integers and subtract() function that subtracts the third integer from the result.
Wrap the two functions in a function called add_and_subtract() which will receive the three numbers

Example'''

def sum_numbers(a=int, b=int):

    return a + b

def subtract(c , d):

    return c - d

def add_and_subtract(a,b,c):

    return subtract(sum_numbers(a,b),c)


if __name__== '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(add_and_subtract(a, b, c))
    #print(subtract(29,10))
   # print(sum_numbers(23,6))

