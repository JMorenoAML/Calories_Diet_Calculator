'''This module is intended to ingest data like WEIGTH, SIZE, GENDER, DIET GOAL...
 And then calculate the suggested Caloric Balance '''

''' 
Our variables are 
WEIGHT float, kg
SIZE float, cm
GENDER cathegorical, Man/woman
DIET GOAL (Cathegorical [for user], making it range on several intervals from -20 to +20% over Calories needed [float]
EXERCISE DONE (We can aproximate Cals depending on kind and duration of sport, as tables, integer)
OR, CALORIES BURNT (or we can directly input the burnt calories every day, integer)
'''

from model import User

def user_info_retriever():    #nota: hacerlo multilanguage usando spreadsheet de google con translate.
    print("Welcome to Diet&Calories calculator")
    User.alias = input('What is your name?')
    print("Nice to meet you {}".format(User.alias))
    print("I need some data from before we prepare your ideal Diet")
    ####### AGE 1/5 #######
    while True:
        try:
            User.age = input("How old are you? (in years, numerical)")
        if (not (type(User.age) == int) or (User.age < 0)):
            print("Please write it again, this time as positive integer numerical value")
            print(" For example:  24  ")
            continue
        else:
            break
    ####### GENDER 2/5 #######
    while True:
        try:
            gen_dummy = input("Are you female or male? 1 = male, 0 = female")
        if ((gen_dummy != 1) or (gen_dummy != 0)):
            print("Please write 0 for female, or 1 for male")
            print("Try again!")
            continue
        elif (gen_dummy == 1):
            User.gender == "male"
            break
        else:
            gen_dummy == 0:
            User.gender == "female"
            break

    while True:
        try:
            User.size

    gender = input('Is your gender is male, write 1. For female write 2: ')
    weight = int(input('What is your weight: '))
    height = int(input('What is your height in inches: '))

