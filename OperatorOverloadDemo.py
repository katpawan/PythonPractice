class Complex():
    """docstring for Complex"""

    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        if(self.imag == 0):
            # return (str(self.real))
            return self.real
        elif (self.imag < 0):
            return ("%d-i%d" % (self.real, abs(self.imag)))
        else:
            return ("%d+i%d" % (self.real, self.imag))


def main():
    c1 = Complex(10, 20)
    c2 = Complex(100, 200)
    c3 = Complex(-100, -200)
    c4 = Complex(-10, -20)
    print(c1 + c2)
    print(c1 + c3)
    print(c1 + c4)


if __name__ == '__main__':
    main()
