#!usr/bin/python3

import pickle

class myPickleClass_Animal:
    def __init__(self, number_of_paws, color):
        self.numPaws = number_of_paws
        self.color = color

class myPickleClass_Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, 4, color)

mary = Sheep("White")
print(str.format(("My sheep mary {0} and has {1} paws", mary.color,
                  mary.number_of_paws))

my_pickled_mary = pickle.dumps(mary)
#my_pickled_mary = pickle.dumps(mary)
print(my_pickled_mary)


