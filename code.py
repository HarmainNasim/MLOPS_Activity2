class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(1, 2))  
