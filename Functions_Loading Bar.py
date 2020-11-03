'''* Loading Bar

You will receive a single integer number between 0 and 100 which is divided with 10 without residue (0, 10, 20, 30...).

Your task is to create a function that visualizes a loading bar depending on that number you have received in the input.

Examples

'''

def loading_bar (number):

    times_ten = number//10
    string='['

    if number==0:
        pass
    else:
      for i in range(1,times_ten+1):
        string=string +'%'

    for i in range(1,10-times_ten+1):
        string = string+'.'
    string=string + ']'

    if number == 100:
        print(f"100% Complete!\n{string}")
    else:
        print(f"{number}% {string}\nStill loading...")


if __name__=='__main__':

    loading_bar(int(input()))
