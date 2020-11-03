'''Smallest of Three Numbers

Write a function which receives three integer numbers and returns the smallest. Use appropriate name for the function.'''

def the_smallest (a=int, b=int, c=int):

    result = a
    if c >= b :
        check = b
        if check <= a:
           result = check
    else:
        check = c
        if check <=a:
            result = check

    return result

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(the_smallest(a,b,c))