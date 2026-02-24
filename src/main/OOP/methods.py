class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'FixedFloat {self.amount:.2f}'

    @staticmethod
    def from_sum(value1, value2):  # doesn't take in object or class. it passes nothing in
        return FixedFloat(value1 + value2)
        print('Hello, I dont take parameters')


number = FixedFloat.from_sum(19.575, 0.789)
print(number)


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'FixedFloat {self.amount:.2f}'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


number = FixedFloat.from_sum(19.575, 0.789)
print(number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'{self.symbol}{self.amount:.2f}'

money = Euro.from_sum(16.758, 9.999)
print(money)
