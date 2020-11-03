'''Odd and Even Sum

You will receive a single number. You have to write a function that returns the sum of all even and all odd digits from that number
as a single string like in the examples below.

Examples'''

#odd=0
#even=0

def odd_even_sum(string):
    odd=0
    even=0

    for i in range(len(string)):
        if int(string[i])%2==0:
            even = even + int(string[i])
        else:
            odd = odd + int(string[i])

    return odd, even


if __name__ == '__main__':

    odd, even = odd_even_sum(input())
    print(f"Odd sum = {odd}, Even sum = {even}")