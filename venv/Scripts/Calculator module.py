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

from model.User import User   # we do FROM Folder.folder. ... script IMPORT class

new_user = User()


def user_info_retriever():    #nota: hacerlo multilanguage usando spreadsheet de google con translate.
    print("Welcome to Diet&Calories calculator")
    User.alias = input('What is your name?')
    print("Nice to meet you {}".format(new_user.alias))
    print("I need some data from before we prepare your ideal Diet")
    ####### AGE 1/5 #######
    while True:
        new_user.age = int(input("How old are you? (in years, numerical)"))

        if type(new_user.age) != int or new_user.age >= 0:
            print("Please write it again, this time as positive integer numerical value")
            print(" For example:  24  ")
            continue
        else:
            break
    ####### GENDER 2/5 #######
    while True:
        gender_dummy = int(input("Are you female or male? 1 = male, 0 = female"))
        if ((gender_dummy != 1) or (gender_dummy != 0)):
            print("Please write 0 for female, or 1 for male")
            print("Try again!")
            continue
        elif (gender_dummy == 1):
            new_user.gender == "male"
            break
        else:

            new_user.gender == "female"
            break
    return new_user

    ####### SIZE 3/5 #######
    while True:
        new_user.size = int(input("Write your size in cms (integer value)"))
        if ((new_user.size <=0) or (new_user.size > 260)):
            print("I don't think that is your correct heigth in cms")
            print("Try again!")

            continue
        elif (type(new_user.size != int ))
            continue

        else:
            break

    ####### WEIGTH 4/5 #######
    while True:
        new_user.weight = input("Write your weigth in Kgs ")      # Disclaimer, cómo saber que lo que meten es realmente
        if ((new_user.size <= 0) or (new_user.size > 260)):       # Kgs y no Lbs
            print("I don't think that is your correct weigth in Kgs")
            print("Try again!")

            continue
        elif (type(new_user.size != int) or type(new_user.size != float))
            continue

        else:
            break

    ###### User_ID ######

    # Still got no clear if I want to have this inside this function, or be called externally
    # the idea is this ID is unique, and must be incremented every time the function is called.
    # maybe nested functions?? Also I need a way to not allow someone already registered and with an assigned ID,
    # registering again (this would create duplicated entries )

print("your data is:")
print(new_user.age," years old\nyour gender is ", new_user.gender)

#####TEST ZONE

take_user_info = user_info_retriever




    # while True:
    #     try:
    #         new_user.size
    #
    # gender = input('Is your gender is male, write 1. For female write 2: ')
    # weight = int(input('What is your weight: '))
    # height = int(input('What is your height in inches: '))

