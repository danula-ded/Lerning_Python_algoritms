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
from typing import List

class Worker(ABC):
    company_phone = "+1-800-555-0199"  # Телефон фирмы

    def __init__(self, first_name: str, last_name: str, phone: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone if phone else Worker.company_phone

    @abstractmethod
    def notify(self, message: str):
        pass

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, Телефон: {self.phone}"


class Developer(Worker):
    def __init__(self, first_name: str, last_name: str, languages: List[str], phone: str = None):
        super().__init__(first_name, last_name, phone)
        self.languages = languages

    def notify(self, message: str):
        print(f"Отправляем '{message}' работнику {self.first_name} {self.last_name} на номер {self.phone}")

    def __str__(self) -> str:
        languages_str = ', '.join(self.languages)
        return f"{super().__str__()}, Языки программирования: {languages_str}"


# Пример использования
if __name__ == "__main__":
    worker1 = Developer("Иван", "Иванов", ["Python", "JavaScript", "C++"])
    worker2 = Developer("Анна", "Петрова", ["Java", "Ruby"], "+7-123-456-7890")

    print(worker1)  # Иван Иванов, Телефон: +1-800-555-0199, Языки программирования: Python, JavaScript, C++
    print(worker2)  # Анна Петрова, Телефон: +7-123-456-7890, Языки программирования: Java, Ruby

    worker1.notify("У вас новая задача!")  # Отправляем 'У вас новая задача!' работнику Иван Иванов на номер +1-800-555-0199
    worker2.notify("Собрание в 15:00.")  # Отправляем 'Собрание в 15:00.' работнику Анна Петрова на номер +7-123-456-7890
