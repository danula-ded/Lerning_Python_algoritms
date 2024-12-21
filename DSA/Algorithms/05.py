# Даны два числа a и b. Найдите пару чисел x и y,
# являющуюся решением уравнения вида: ax + by = НОД(a, b)

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0

    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

print(extended_gcd(18, 84))
