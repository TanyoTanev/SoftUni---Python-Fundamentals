'''* Bread Factory
As a young baker, you are baking the bread out of the bakery.
You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. Each event is separated
with '|' (vertical bar): "event1|event2|event3…"
Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")

If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial energy (100).
Print: "You gained {0} energy.".

After that, print your current energy: "Current energy: {0}.". If the event is "order": You've earned some coins, the number in the
 second part. Each time you get an order, your energy decreases with 30 points.

If you have energy to complete the order, print: "You earned {0} coins.".
If your energy drops below 0, you skip the order and gain 50 energy points. Print: "You had to rest!".
In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins you have to spent and
remove from your coins.
If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print ("You bought {ingredient}.")
If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
If you managed to handle all events through the day, print on the next three lines:
"Day completed!", "Coins: {coins}", "Energy: {energy}".

Input / Constraints

You receive a string, representing the working day events, separated with '|' (vertical bar): " event1|event2|event3…".
Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")'''

string = input()
events = string.split('|')
energy = 100
gained_energy=0
coins = 100

for i in range(len(events)):
    events[i] = events[i].split('-')

#print(events)
check=0

for i in range(len(events)):

    if events[i][0] == 'rest':

        if energy == 100  or energy + int(events[i][1]) >= 100:
            gained_energy = 100 - energy

        else:
            gained_energy = int(events[i][1])
            energy = energy + int(events[i][1])

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
        #i -= 1

    elif events[i][0] == 'order':
        if energy >= 30:

            energy = energy - 30
            coins  = coins + int(events[i][1])
            print(f"You earned {int(events[i][1])} coins.")
        else:
            energy = energy + 50
            print(f"You had to rest!")
        #i -= 1

    else:
        if coins - int(events[i][1]) <= 0:
             print(f"Closed! Cannot afford {events[i][0]}.")
             check+=1
             break
        else:
             coins = coins - int(events[i][1])
             print(f"You bought {events[i][0]}.")


if check==0:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


