class Dish:
    categories = ["Салат", "Суп", "Горячее", "Десерт", "Напиток"]

    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительным числом.")
        self._price = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in Dish.categories:
            raise ValueError(f"Категория должна быть одной из: {
                             ', '.join(Dish.categories)}.")
        self._category = value

    def __str__(self):
        return f"Блюдо: {self.name}, Цена: {self.price:.2f}, Категория: {self.category}"


# Тестовые данные
dish1 = Dish("Цезарь", 450.0, "Салат")
dish2 = Dish("Борщ", 300.0, "Суп")


print(dish1)
print(dish2)
