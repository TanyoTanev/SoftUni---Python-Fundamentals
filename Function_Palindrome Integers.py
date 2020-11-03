'''Palindrome Integers

A palindrome is a number which reads the same backward as forward, such as 323 or 1001. Write a function which receives a list of positive
integers and checks if each integer is a palindrome or not. Print the results on the console
The input will be a single string containing the numbers separated by comma and space ", "

Examples'''

def palindrome_integers(string):

    command = string.split(', ')
    result = []

    for word in command:
        if word == word[::-1]:
            result.append('True')
        else:
            result.append('False')


    return result

if __name__ == '__main__':

    result = palindrome_integers(input())
    for i in range(len(result)):
        print(f"{result[i]}")
