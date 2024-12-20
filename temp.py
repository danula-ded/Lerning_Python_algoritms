# та же функция, ускоренная мемоизацией
# сложность: O(n)

# в memo хранятся результаты решений подзадач (подсчитанные числа)
def fibonacci(n, memo={0: 0, 1: 1}):
    # если возможно - используем уже подсчитанное значения
    if n in memo:
        return memo[n]
    # иначе считаем число по формуле и сохраняем в memo
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    # возвращаем нужное число
    return memo[n]


print(fibonacci(10))


def fib(n, memo={0: 0, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
