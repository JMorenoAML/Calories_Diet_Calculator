import unittest
from model.User import User


# TEST CASES
isabel = User(27, 57, 159, "female", "Isa")
francisca = User(61, 90, 155, "female", "Isa")
juan = User(61, 108, 180, "male", "Juan")


class UserUT(unittest.TestCase):

    global isabel
    global francisca
    global juan

    def test_get_Benedict_Harris(self):

        self.assertEqual(isabel.get_Benedict_Harris(), 1267)
        self.assertEqual(francisca.get_Benedict_Harris(), 1402)
        self.assertEqual(juan.get_Benedict_Harris(), 1905)

    def test_get_final_kcal_request(self):

        self.assertEqual(isabel.get_final_kcal_request(3), 1963)
        self.assertEqual(francisca.get_final_kcal_request(2), 1927)
        self.assertEqual(juan.get_final_kcal_request(1), 2286)


if __name__ == '__main__':
    unittest.main()