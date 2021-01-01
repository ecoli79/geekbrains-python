# lesson-8 example 7
# working with classes

class Compl:
    a = int()
    b = int()

    def __init__(self, a, b):
        try:
            self.a = a
            self.b = b
            print(self.compl)
        except Exception as err:
            print(err)

    @property
    def compl(self):
        res = ""
        if self.a != 0:
            if self.b != 0:
                res += str(self.a) + "+" + str(self.b) + "i"
            else:
                res += str(self.a) + "+" + "i"
        else:
            if self.b != 0:
                res += str(self.b) + "i"
        return res

    def __add__(self, other):
        return str(self.a + other.a) + "+" + str(self.b + other.b) + "i"

    def __mul__(self, other):
        first_compl = [1 if self.a == 0 else self.a,
                       1 if self.b == 0 else self.b]
        second_compl = [1 if other.a == 0 else other.a,
                        1 if other.b == 0 else other.b]

        return str(first_compl[0] * second_compl[0] - first_compl[1] * second_compl[1]) + "+" + str(first_compl[1] * second_compl[0] + first_compl[0] * second_compl[1]) + "i"


z = Compl(3, 5)
y = Compl(1, 5)
f = Compl(0, 4)
print(f"sum {z.compl} and {y.compl} is: ")
print(z + y)
print(f"Mul {z.compl} and {y.compl} is: ")
print(z * y)
