class BigInteger:
    def __init__(self, value):
        self.value = int(value)

    def __add__(self, other):
        return BigInteger(self.value + other.value)

    def __str__(self):
        return str(self.value)
