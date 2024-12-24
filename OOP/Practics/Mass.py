# Напишите описанную ниже систему классов и продемонстрируйте их работу:
# Mass (масса):
# У массы есть property value: float, которое по умолчанию при создании равно нулю. У массы есть
# магический метод для строкового представления в виде “X kg Y g”, то есть объект этого класса с value
# 1.234 должен отображаться как “1 kg 234 g”. Сеттер property value должен проводить необходимые
# проверки (масса должна быть не отрицательным числом). У массы также должны быть магические
# методы сложения, вычитания, сравнения (больше, меньше, больше или равно, меньше или равно,
# равно, не равно). Продемонстрируйте работоспособность всех методов класса на примерах.

class Mass:
    def __init__(self, value: float = 0.0):
        self.value = value  # Используем сеттер для установки начального значения

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, val: float):
        if val < 0:
            raise ValueError("Масса не может быть отрицательной.")
        self._value = val

    def __str__(self) -> str:
        kg = int(self.value)
        g = int((self.value - kg) * 1000)
        return f"{kg} kg {g} g"

    def __add__(self, other):
        if isinstance(other, Mass):
            return Mass(self.value + other.value)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Mass):
            return Mass(self.value - other.value)
        return NotImplemented

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


# Пример использования класса Mass
if __name__ == "__main__":
    mass1 = Mass(1.234)
    mass2 = Mass(2.567)

    print(mass1)  # 1 kg 234 g
    print(mass2)  # 2 kg 567 g

    # Сложение
    mass3 = mass1 + mass2
    print(mass3)  # 3 kg 801 g

    # Вычитание
    mass4 = mass2 - mass1
    print(mass4)  # 1 kg 333 g

    # Сравнения
    print(mass1 < mass2)   # True
    print(mass1 <= mass2)  # True
    print(mass1 > mass2)   # False
    print(mass1 >= mass2)  # False
    print(mass1 == mass2)  # False
    print(mass1 != mass2)  # True

    # Проверка исключения на отрицательное значение
    try:
        mass5 = Mass(-5)
    except ValueError as e:
        print(e)  # Масса не может быть отрицательной.
