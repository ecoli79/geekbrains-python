# lesson-7 example 2
# working with classes

from abc import ABC, abstractmethod


class Closes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def count_material(self):
        pass


class Coat(Closes):

    @property
    def count_material(self):
        return self.size / 6.5 + 0.5


class Suite(Closes):

    @property
    def count_material(self):
        return (self.height * 2 + 0.3) / 100


my_coat = Coat(52, 150)
my_suite = Suite(52, 150)

print(
    f"Чтобы сшить пальто {my_coat.size} размера необходимо {my_coat.count_material} метров шерстяной ткани")
print(
    f"Чтобы сшить костюм {my_suite.size} размера необходимо {my_suite.count_material} метров ткани")
