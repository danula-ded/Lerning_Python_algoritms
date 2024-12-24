# Класс “Dish” ("Блюдо"):
# Свойства класса:
# categories: list[str] - список возможных категорий блюд.
# Свойства объекта:
# name (название): str - публичное свойство;
# price (цена): float – property, сеттер проверяет значение (только положительные числа);
# category (категория): str – property, сеттер проверяет валидность категории.
# Методы:
# Метод строкового представления, отображающий название, цену и категорию.
class Dish:
    categories = ["appetizer", "main course", "dessert", "beverage"]  # Возможные категории блюд

    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self._price = None  # Инициализируем цену как None
        self.price = price  # Используем сеттер для проверки
        self.category = category  # Используем сеттер для проверки

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Цена должна быть положительным числом.")
        self._price = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value: str):
        if value not in Dish.categories:
            raise ValueError(f"Категория должна быть одной из следующих: {', '.join(Dish.categories)}.")
        self._category = value

    def __str__(self) -> str:
        return f"Блюдо: {self.name}, Цена: {self.price:.2f}, Категория: {self.category}"


# Пример использования
if __name__ == "__main__":
    dish1 = Dish("Салат Цезарь", 12.50, "appetizer")
    dish2 = Dish("Стейк", 25.00, "main course")
    
    print(dish1)  # Блюдо: Салат Цезарь, Цена: 12.50, Категория: appetizer
    print(dish2)  # Блюдо: Стейк, Цена: 25.00, Категория: main course

    # Проверка исключений
    try:
        dish3 = Dish("Суп", -5.00, "appetizer")  # Ошибка: цена отрицательная
    except ValueError as e:
        print(e)

    try:
        dish4 = Dish("Чай", 3.00, "snack")  # Ошибка: категория невалидная
    except ValueError as e:
        print(e)
