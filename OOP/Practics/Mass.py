class Mass:
    def __init__(self, value: float = 0.0):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError("Масса должна быть неотрицательным числом.")
        self._value = val

    def __str__(self):
        kg = int(self.value)
        g = int((self.value - kg) * 1000)
        return f"{kg} kg {g} g"

    def __add__(self, other):
        if isinstance(other, Mass):
            return Mass(self.value + other.value)
        raise TypeError("Складывать можно только объекты класса Mass.")

    def __sub__(self, other):
        if isinstance(other, Mass):
            result = self.value - other.value
            if result < 0:
                raise ValueError(
                    "Результат вычитания не может быть отрицательным.")
            return Mass(result)
        raise TypeError("Вычитать можно только объекты класса Mass.")

    def __eq__(self, other):
        if isinstance(other, Mass):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Mass):
            return self.value != other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Mass):
            return self.value < other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Mass):
            return self.value <= other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Mass):
            return self.value > other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Mass):
            return self.value >= other.value
        return NotImplemented


mass1 = Mass(1.234)
mass2 = Mass(2.567)
mass3 = Mass(0.5)

print(mass1)
print(mass2)
print(mass3)

mass4 = mass1 + mass3
print(mass4)

mass5 = mass2 - mass1
print(mass5)

print(mass1 == mass2)
print(mass1 != mass2)
print(mass1 < mass2)
print(mass1 <= mass2)
print(mass2 > mass3)
print(mass2 >= mass3)
