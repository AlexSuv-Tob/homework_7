class Cell(object):
    def __init__(self, num_cell):
        self.num_cell = int(num_cell)

    def __add__(self, num_cell):
        return self.num_cell + num_cell

    def __sub__(self, num_cell):
        if abs(self.num_cell - num_cell) >= 2 or abs(num_cell - self.num_cell >= 2):
            return self.num_cell - num_cell
        else:
            print(('разность количества клеток меньше 2х'))

    def __mul__(self, num_cell):
        return self.num_cell * num_cell

    def __truediv__(self, num_cell):
        return self.num_cell // num_cell

    @property
    def y_cell(self):
        y_cell = Cell(num_cell)
        return y_cell

    def make_order(self, y_cell, num_cell_rov):
        a = y_cell // num_cell_rov
        b = y_cell % num_cell_rov
        return r'\n'.join(['*' * num_cell_rov for i in range(a)]) + r'\n' + '*' * b


my_cell = Cell(25)
num_cell = 15

a = my_cell + num_cell
b = my_cell - num_cell
c = my_cell * num_cell
d = my_cell / num_cell

print(a)
print(b)
print(c)
print(d)
print(my_cell.make_order(16, 5))
