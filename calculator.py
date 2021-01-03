class Calculator:

    def square(self, x):
        return x * x

    def division(self, x, y):
        return x % y

    def nwd(self, x, y):
        while y:
            x, y = y, x % y
        return x

if  __name__ == "__main__":
    calculator = Calculator()














