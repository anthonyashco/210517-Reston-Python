import unittest
# write a person class that has the instance variables of name and age
# implement __init__ with the default argument for age as -1
# implement __str__ to give name and age in the following format 'Bill, 40 years old'
# additionally make a class variable that keeps track of the amount of people created


class Person:
    amount = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.amount += 1

    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old"


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):
    # ! Tests appear to run in alphabetic order, changed function names.

    def test1_adam(self):
        adam = Person('Adam', 19)
        self.assertEquals(str(adam), 'Adam, 19 years old')

    def test2_richard(self):
        richard = Person('Richard', 22)
        self.assertEquals(str(richard), 'Richard, 22 years old')

    def test3_amount(self):
        self.assertEquals(Person.amount, 2)


if __name__ == '__main__':
    unittest.main()