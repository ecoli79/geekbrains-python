# lesson-7 example 3
# working with classes

class Cell:
    def __init__(self, cells):
        self.cells = round(cells)

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if self.cells - other.cells >= 0:
            return self.cells - other.cells
        else:
            return "The substruction is low 0, first cell count must be more then second cell."

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        return self.cells // other.cells

    def make_order(self, cols):
        rows_full = self.cells // cols
        row_add = self.cells % cols
        while rows_full > 0:
            print("*" * cols + "\n")
            rows_full -= 1

        print("*" * row_add + "\n")


cell_1 = Cell(58)
cell_2 = Cell(38)

print(f"Сложение двух клеток cell_1: {cell_1.cells} и cell_2: {cell_2.cells}")
print(cell_1 + cell_2)

print(f"Вычитание двух клеток cell_1: {cell_1.cells} и cell_2: {cell_2.cells}")
print(cell_1 - cell_2)

print(f"Умножение двух клеток cell_1: {cell_1.cells} и cell_2: {cell_2.cells}")
cell_3 = cell_1 * cell_2
print(cell_3)

print(f"Деление двух клеток cell_1: {cell_1.cells} и cell_2: {cell_2.cells}")
cell_4 = cell_1 // cell_2
print(cell_4)

print(f"Разбивка клеток по рядам.")
cell_1.make_order(9)
