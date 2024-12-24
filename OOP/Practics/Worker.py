# Напишите два класса - Worker (Работник) и Developer (Разработчик).
# Разработчик должен наследоваться от работника. Работник - абстрактный класс. Абстрактного
# работника инстанцировать нельзя, только объекты классов-потомков. У каждого работника есть имя,
# фамилия и телефон. При создании телефон по умолчанию равен телефону фирмы (придумайте свой).
# У работника есть метод notify, который уведомляет работника (“отправляет сообщение” на телефон
# работника). Этот метод должен принимать сообщение для работника и выводить в print сообщение
# формата “отправляем СООБЩЕНИЕ работнику ИМЯ ФАМИЛИЯ на номер ТЕЛЕФОН”
# (использовать интерполяцию). Также у работника есть магический метод для строкового
# представления. У разработчика кроме всех свойств и методов работника есть свойство, в котором
# хранится список языков, на которых он пишет. Метод строкового представления у разработчика
# добавляет перечисление языков (кроме того, что уже есть в методе строкового представления
# работника).
from abc import ABC, abstractmethod


class Worker(ABC):
    company_phone = "+1234567890"

    def __init__(self, first_name: str, last_name: str, phone: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone if phone else Worker.company_phone

    @abstractmethod
    def __str__(self):
        pass

    def notify(self, message: str):
        print(f"Отправляем '{message}' работнику {self.first_name} {
              self.last_name} на номер {self.phone}")


class Developer(Worker):
    def __init__(self, first_name: str, last_name: str, phone: str = None, languages: list[str] = None):
        super().__init__(first_name, last_name, phone)
        self.languages = languages if languages else []

    def __str__(self):
        languages_str = ", ".join(
            self.languages) if self.languages else "не указаны"
        return f"{self.first_name} {self.last_name}, Телефон: {self.phone}, Языки программирования: {languages_str}"


# Примеры использования
developer = Developer("Иван", "Иванов", "+7987654321",
                      ["Python", "JavaScript"])
print(developer)

developer.notify("Не забудьте сдать отчёт!")

developer2 = Developer("Ольга", "Петрова")
print(developer2)

developer2.notify("Планёрка в 10:00.")
