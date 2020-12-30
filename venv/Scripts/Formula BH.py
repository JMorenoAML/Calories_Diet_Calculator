
class BH_Formula:

    BMR_std = (10*weight) + (6.25*size) - (5*age)
        if gender == "male":
            BMR_man = BMR_std + 5
            BMR = BMR_man
        else:
            BMR_woman = BMR_std - 161
            BMR = BMR_woman