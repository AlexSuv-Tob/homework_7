'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном  виде
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
новая матрица.
'''
class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(str(el) for el in lt) for lt in self.matrix)

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other = Matrix(other)
        result = []
        num = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                num.append(summa)
                if len(num) == len(self.matrix):
                    result.append(num)
                    num = []
        return Matrix(result)

mx = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mx.matrix)
print('----------------------------------------------------------------------------')
print(mx.__str__())
print('-----------------------------------------------------------------------------')
other = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
res = mx + other
print(res)


