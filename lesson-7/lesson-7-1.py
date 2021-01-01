# lesson-7 example 1
# working with classes

class Martix:

    def __init__(self, in_matrix):
        self.matrix = in_matrix

    def __str__(self):
        return '\n'.join(str(row).replace('[', '').replace(',', '  ').replace(']', '') for row in self.matrix)

    def __add__(self, other):
        # пока просто через try сделал чтобы разноразмерные матрицы не ломали программу...
        try:
            return [self.matrix[row][col] + other.matrix[row][col] for col in range(len(self.matrix)) for row in range(len(other.matrix))]
        except IndexError:
            return "Matrixs not same size! Only same size matrix may added."


mat1 = Martix([[31, 22], [37, 43], [51, 86]])
print(mat1)
print("-"*42)

mat2 = Martix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(mat2)
print("-"*42)

mat3 = Martix([[3, 5, 8, 3], [8, 3, 7, 1], [10, 8, 4, 6]])
print(mat3)
print("-"*42)

mat4 = Martix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(mat1 + mat2)
print(mat2 + mat4)
