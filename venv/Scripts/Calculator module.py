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
     
     Hacer un diccionario key-value con lo que el user pulsa como key, y el % a aplicar como value
     
EXERCISE DONE (We can aproximate Cals depending on kind and duration of sport, as tables, integer)
    { Let's define some intervals: 
     TO do later, go on with coding 
OR, CALORIES BURNT (or we can directly input the burnt calories every day, integer)
'''
# la funcion Harris debe recibir un tipo usuario.

from model.User import User   # we do FROM Folder.folder. ... script IMPORT class

# forma 1: crear clase user, y crearle el método harris-benedict para poder aplicarlo al self.
# forma 2: metodo de la clase calculadora, que recibe un objeto "usuario". <- esto mejor


def user_info_retriever():    #nota: hacerlo multilanguage usando spreadsheet de google con translate.
    print("Welcome to Diet&Calories calculator")
    alias = input('What is your name?')
    print("Nice to meet you {}".format(alias))
    print("I need some data from before we prepare your ideal Diet")
    ####### AGE 1/5 #######
    age =""
    while True:
        try:
            age = float(input("How old are you? (in years, numerical) "))  #esto aqui ahora mismo es un string

            if type(age) != float or age <= 0 :
                print("Please write it again, this time as positive and numerical value")
                print(" For example:  24  ")
                continue
            elif age > 120:
                print("You are too old to be using this! Rewrite your age properly :)")
                continue
            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    ####### GENDER 2/5 #######
    gender = ""
    while True:
        gender_dummy = input("Are you female or male? 1 = male, 0 = female ")
        if (gender_dummy == "1"):
            gender = "male"
            break
        elif (gender_dummy == "0"):
            gender = "female"
            break
        else:
            print("Please write 0 for female, or 1 for male")
            print("Try again!")
            continue

    ####### SIZE 3/5 #######
    while True:
        try:
            size = float(input("Write your size in cms "))

            if ((size <=0) or (size > 260)):
                print("I don't think that is your correct heigth in cms")
                print("Try again!")

                continue
            elif (type(size) != float):
                continue

            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    ####### WEIGTH 4/5 #######
    while True:
        try:
            weight = float(input("Write your weigth in Kgs "))      # Disclaimer, cómo saber que lo que meten es realmente
            if ((weight <= 0) or (weight > 360)):       # Kgs y no Lbs
                print("I don't think that is your correct weigth in Kgs")
                print("Try again!")

                continue
            elif (type(weight) != float):
                continue

            else:
                break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

    ###### Summary of User #######

    print("Ok",alias,"our data is:")
    print("you are", str(age), "years old and your gender is", gender)
    print("your weigth is", str(weight), "Kgs and your size is", str(size), "cms ")


    return age, weight, size, gender ,alias


Usuario = User(user_info_retriever())  # <---- aqui ha de venir la logica que asocia a este user con una entrada unica de
                                        # la BBDD de SQL













