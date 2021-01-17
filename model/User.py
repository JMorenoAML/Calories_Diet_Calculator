import math


class User:

    COEFICIENTES = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}

    def __init__(self, age, weight, size, gender, alias):
        self.age = age
        self.weight = weight
        self.size = size
        self.gender = gender
        self.alias = alias

    def get_Benedict_Harris(self):
        bmr_std = (10 * self.weight) + (6.25 * self.size) - (5 * self.age)
        if self.gender == "male":
            bmr_man = bmr_std + 5
            bmr = bmr_man
        else:
            bmr_woman = bmr_std - 161
            bmr = bmr_woman
        return math.floor(bmr)

    def get_final_kcal_request(self, intensity_level):
        intensity_factor = User.COEFICIENTES.get(intensity_level, "Respuesta inválida")
        return math.floor(intensity_factor * self.get_Benedict_Harris())
