# Даны два числа a и b. Найдите их наибольший общий делитель.

def find_gcd(a: int, b: int) -> int:
    if b == 0:
        return a

    return find_gcd(b, a % b)


print(find_gcd(70, 8))
