class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    @classmethod
    def mutliply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a + b