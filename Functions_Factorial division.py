'''* Factorial Division

Write a function that receives two integer numbers. Calculate factorial of each number. Divide the first result by the second and
print the division formatted to the second decimal point.


'''

def fact_division(a, b):

    fact1 = 1
    fact2 = 1

    for i in range(1,a+1):
        fact1=fact1*i
    for i in range(1,b+1):
        fact2=fact2*i
    print(f"{fact1/fact2:.2f}")


if __name__ == '__main__':
    fact_division(int(input()), int(input()))