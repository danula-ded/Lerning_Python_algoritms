from typing import Dict, Type


class SingletonMeta(type):
    _instances: Dict[Type, 'Counter'] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Counter(metaclass=SingletonMeta):
    def __init__(self):
        self._value = 0
        self._step = 1

    @property
    def value(self):
        return self._value

    @property
    def step(self):
        return self._step

    def tick(self):
        self._value += self._step

    def reset(self):
        self._value = 0


class DownwardCounter(Counter):
    def __init__(self):
        super().__init__()
        self._step = -1


class UpwardCounter(Counter):
    def __init__(self):
        super().__init__()
        self._step = 1


counter1 = Counter()
print(counter1.value)  # 0
counter1.tick()
print(counter1.value)  # 1
counter1.tick()
print(counter1.value)  # 2
counter1.reset()
print(counter1.value)  # 0

print("---")

counter2 = DownwardCounter()
print(counter2.value)  # 0
counter2.tick()
print(counter2.value)  # -1
counter2.tick()
print(counter2.value)  # -2
# counter2.reset()
# print(counter2.value)

print("---")

counter5 = DownwardCounter()
counter5.tick()
print(counter5.value)  # -3
counter5.tick()
print(counter5.value)  # -4

print("---")

counter3 = UpwardCounter()
print(counter3.value)  # 0
counter3.tick()
print(counter3.value)  # 1
counter3.tick()
print(counter3.value)  # 2
counter3.reset()
print(counter3.value)  # 0

print("---")

# Проверка Singleton
counter4 = Counter()
print(counter4 is counter1)

print("---")

counter6 = UpwardCounter()
print(counter6 is counter3)
