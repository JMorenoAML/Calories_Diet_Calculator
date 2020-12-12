'''This module is intended to ingest data like WEIGTH, SIZE, GENDER, DIET GOAL...
 And then calculate the suggested Caloric Balance '''

''' 
Our variables are 
WEIGHT float, kg
SIZE float, cm
GENDER cathegorical, Man/woman
DIET GOAL (Cathegorical [for user], making it range on several intervals from -20 to +20% over Calories needed [float]
    { Let's define some intervals and cathegories, % applied over base BMR}
     Higher Weigth loss = -20%
     Normal Weigth loss = -10%
     Ligth weigth loss = -5%
     Keep this weigth = 0% (no changes)
     Ligth weigth gain = +5%
     Normal weigth gain = +10%
     Higher weigth gain = +20%
     
EXERCISE DONE (We can aproximate Cals depending on kind and duration of sport, as tables, integer)
    { Let's define some intervals: 
     TO do later, go on with coding 
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
        if ((new_user.size <= 0) or (new_user.size > 360)):       # Kgs y no Lbs
            print("I don't think that is your correct weigth in Kgs")
            print("Try again!")

            continue
        elif (type(new_user.size != int) or type(new_user.size != float))
            continue

        else:
            break

    ###### User_ID ######

    # Will be assigned externally via SQL

# Benedict-Harris Formula:

#
# man
# BMR_std = (10*new_user.weigth) + (6.25*new_user.heigth) - (5*new_user.age)
# if new_user.gender == "male":
#     BMR_man = BMR_std + 5
# else:

#     BMR_woman = BMR_std - 161

print("Ok ",new_user.alias," your data is:")
print("you are ",str(new_user.age)," years old and your gender is ", new_user.gender)
print("your weigth is ",str(new_user.weight)," Kgs and your size is ",str(new_user.size)," cms "
if new_user.gender == "male":
    print("you caloric use is ",BMR_man, " Kcal/day")         # Find a way to look for BMR_man, if found print it,
else:                                                           # if not found, print BMR_woman (save this comparer)
    print("you caloric use is ",BMR_woman, " Kcal/day")





#####TEST ZONE

take_user_info = user_info_retriever






    # while True:
    #     try:
    #         new_user.size
    #
    # gender = input('Is your gender is male, write 1. For female write 2: ')
    # weight = int(input('What is your weight: '))
    # height = int(input('What is your height in inches: '))

