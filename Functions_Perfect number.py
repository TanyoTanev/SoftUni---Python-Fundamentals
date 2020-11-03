'''Perfect Number

Write a function that receives an integer number and returns if this number is perfect or NOT.

A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its
positive divisors excluding the number itself (also known as its aliquot sum).

Examples'''

def perfect_number (string):
    sum_divisors=1
    number=int(string)
    result = ''
    result2 = '1'

    for i in range(2,number):
        if number % i == 0:
            sum_divisors = sum_divisors + i
            result2 = result2 + '+' +str(i)

    if sum_divisors==number:
        result ='We have a perfect number!'
    else:
        result  = "It's not so perfect."
    #print(sum_divisors)
    #print(number)
    return result , result2


if __name__ == '__main__':

   result , result2 = perfect_number(input())

   if result == "It's not so perfect.":
       print(result)

   else:
       print(result)
       #print(result2)
