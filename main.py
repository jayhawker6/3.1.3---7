## Welcome to Beefy's Brackish Burgers! ##
## Complete with Andrew's idiotproof+++ ##
## Error Prevention Code solutions!(tm) ##
## Andrew Inc: Making overcomplicated   ##
## Solutions to simple problems since   ##
##               2017                   ##
#----------------------------------------#
import os


def clear():
    os.system("clear")


def printbill():
    print('Bill: %s$' % (cash))


def printorder():
    print('Order: %s' % (order))


def printall():
    print('')
    printbill()
    printorder()
    print('')


while True:
    global name
    try:
        name = str(input('Name: '))
    except ValueError:
        print(
            "Please give us something that wouldn't break our program. Thank you!"
        )
        continue
    if name == (''):
        print(
            'Please give us a name that does not resemble the ever growing bottomless void of death. Thank you!'
        )
        continue
    else:
        break
clear()
print(
    "Hello %s! Welcome to Beefy's Brackish Burgers! please order from our menu below."
    % (name))
while True:
    global sandwich
    global cash
    global order
    order = []
    cash = 0.00
    try:
        sandwich = int(
            input("""
        Sandwiches:

        1 - Chicken    (5.25)$
        2 - Beef       (6.25)$
        3 - Tofu       (5.75)$
        4 - Reindeer   (25.52)$

        5 - Skip
        6 - Quit
        Answer:
        """))
        print('')
    except ValueError:
        print('Please enter a sandwich numer.')
        continue
    if sandwich == 1:
        print("One chicken sandwich on the way!")
        order.append('Chicken Sandwich')
        cash += 5.25
        break
    elif sandwich == 2:
        print("One beef sandwich on the way!")
        order.append('Beef Sandwich')
        cash += 6.25
        break
    elif sandwich == 3:
        print("One tofu sandwich on the way!")
        order.append("Tofu Sandwich")
        cash += 5.75
        break
    elif sandwich == 4:
        print(
            "Sadly tis not the season to be jolly. Reindeer are currently in short supply and our famous reindeer sandwiches will be back next christmas. Thank you!"
        )
        continue
    elif sandwich == 5:
        print("Skipping...")
        order.append('No Meal')
        print('')
        break
    elif sandwich == 6:
        print("Quitting...")
        quit('User initiated quit')
    else:
        print("Please use a valid option!")
        continue
clear()
printorder()
while True:
    global beverage
    try:
        beverage = int(
            input("""
        Beverages:

        1 - Small               (1.00)
        2 - Medium              (1.75)
        3 - Large               (2.25)
        4 - Reindeer Smoothie   (14.50
        
        5 - Skip
        6 - Quit
        Answer: 
        """))
        print('')
    except ValueError:
        print('Please enter a beverage number. Thank you!')
        continue
    if beverage == 1:
        print('One small coming up!')
        order.append('Small Beverage')
        cash += 1.00
        break
    elif beverage == 2:
        print('One medium coming up!')
        order.append('Medium Beverage')
        cash += 1.75
        break
    elif beverage == 3:
        print('One large coming up!')
        order.append('Large Beverage')
        cash += 2.25
        break
    elif beverage == 4:
        print(
            "Sadly tis not the season to be jolly. Reindeer are currently in short supply and our famous reindeer smoothies will be back next christmas. Thank you!"
        )
        continue
    elif beverage == 5:
        print('Skipping...')
        order.append('No Beverage')
        break
    elif beverage == 6:
        print('Quitting')
        quit('User initiated quit')
    else:
        print('Please use a valid option!')
clear()
printorder()
while True:
    global fries
    try:
        fries = int(
            input("""
        Fries:

        1 - Small               (1.00)
        2 - Medium              (1.50)
        3 - Large               (2.00)
        4 - Reindeer Rings      (8.75)
        
        5 - Skip
        6 - Quit
        Answer: 
        """))
        print('')
    except ValueError:
        print('Please enter a fry number. Thank you!')
        continue
    if fries == 1:
        while True:
            try:
                a = int(
                    input("""
                Would you like to mega size that?
                
                1 - Yes
                2 - No
                Answer:
                """))
            except ValueError:
                print("Please enter a valid answer!")
                continue
            if a == 1:
                print('One large coming up!')
                order.append('Large Fry')
                cash += 2
                break
            elif a == 2:
                print('One small coming up!')
                order.append('Small Fry')
                cash += 1
                break
            else:
                print('Please enter a valid answer!')
                continue
        break
    elif fries == 2:
        print('One medium coming up!')
        order.append('Medium Fries')
        cash += 1.75
        break
    elif fries == 3:
        print('One large coming up!')
        order.append('Large Fries')
        cash += 2.25
        break
    elif fries == 4:
        print(
            "Sadly tis not the season to be jolly. Reindeer are currently in short supply and our famous reindeer rings will be back next christmas. Thank you!"
        )
        continue
    elif fries == 5:
        print('Skipping...')
        order.append('No Fries')
        break
    elif fries == 6:
        print('Quitting')
        quit('User initiated quit')
    else:
        print('Please use a valid option!')
clear()
printall()
while True:
    global packets
    try:
        packets = int(input("How many ketchup packets would you like?: "))
    except ValueError:
        continue
    if packets < 0:
        print(
            'Sadly at this time BBB does not supply antimatter kethup packets. Sorry for the inconvience!'
        )
    elif packets == 0:
        order.append('No Packets')
        break
    else:
        print("Here's your %s packets!" % (packets))
        order.append(str('%s Packets' % (packets)))
        cash += packets * .25
        break
if sandwich < 4 and beverage < 4 and fries < 4:
    print(
        "You have qualified for a 1.00$ price discount by ordering a full meal!"
    )
    cash -= 1
clear()
print('Here is your order!')
printall()
quit('End of program.')
