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

def user_info_retriever():    #nota: hacerlo multilanguage usando spreadsheet de google con translate.
    print("Welcome to Diet&Calories calculator")
    weigth= input("Write your weigth in Kg:")
    input()




