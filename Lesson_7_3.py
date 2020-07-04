class Cell:
    def __init__(self, mass:int):
        self.mass = mass
        self.__make_cell = 0

    def __add__(self, other):
        new_cell = self.mass + other.mass
        return Cell(new_cell)

    def __sub__(self, other):
        new_cell = self.mass - other.mass
        if new_cell > 0:
            return Cell(new_cell)
        else:
            print('Клетка не создалась')
            return None

    def __mul__(self, other):
        new_cell = self.mass * other.mass
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = self.mass // other.mass
        return Cell(new_cell)

    def __str__(self):
        return 'В клетке {} ячеек\n'.format(self.mass)

    def make_order(self, n):
        new_str = ''
        self.__make_cell = self.mass
        while self.__make_cell > 0:
            if self.__make_cell > n:
                self.__make_cell -= n
                new_str += '*' * n + '\n'
            else:
                new_str += '*' * self.__make_cell
                self.__make_cell -= n

        return  new_str

if __name__ == "__main__":
    one = Cell(45)
    two = Cell(4)
    ad = one + two
    sub = one - two
    sub_no = two - one
    mul = one * two
    tru = one / two
    print(one, two, ad, sub, sub_no, mul, tru)
    print(one.make_order(13))
