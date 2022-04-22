import random

inp_dice_type= input("What kind of dice would you like to roll? (Options: D2, D6, D8, D10, D20): ").lower()

if inp_dice_type== "D2":
    print(random.randint(1, 2))

if inp_dice_type== "D6":
    print(random.randint(1, 6))  
    
if inp_dice_type== "D8":
    print(random.randint(1, 8))    

if inp_dice_type== "D10":
    print(random.randint(1, 10))
    
if inp_dice_type== "D20":
    print(random.randint(1, 20))
    
cont_inp= input("Would you like to roll again? (Y/N): ").lower()
if cont_inp== "Y":
    print (inp_dice_type)    
