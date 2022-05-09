#Random import function needed in order to roll the dice properly
import random

#Added the input for the user's name to add depth to dice roller.

user_name= input("Welcome to the dice roll simulator! What is your name?: ")

while user_name.isnumeric():
        print ("Invalid input! Please try again.")
        user_name= input("\nWelcome to the dice roll simulator! What is your name?: ")
print("Welcome "+ user_name.capitalize()+ "!")

#The program checks if the input is in letters or numbers. Numbers return an error.

sides = int(input("\nHow many sides are on the die? "))
die_or_dice = int(input("How many dice would you like? "))
gen_roll= [random.randint(1, sides) for _ in range(die_or_dice)]
print("\nYou have rolled: " + str(gen_roll))

roll_again="yes"
#if you want to roll again you can give the input accordingly
while(roll_again=="yes" or roll_again=="y"):
        gen_roll= [random.randint(1, sides) for _ in range(die_or_dice)]
        print("\nYou have rolled: " + str(gen_roll))
        roll_again=input("Do you want to roll again: y/yes or n/no:: ")        
else:
        print("Goodbye!")
