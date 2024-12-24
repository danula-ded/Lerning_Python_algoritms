# Напишите описанную ниже систему классов и продемонстрируйте их работу:
# Класс «Студент»:
# Свойства класса:
# Диапазон возможных оценок: tuple[int, int].
# Свойства объекта:
# name (имя): str;
# average_mark (средний балл): float - read-only property;
# marks (оценки): list[int] - список оценок студента. Является property, сеттер проверяет тип данных
# оценки и вхождение в диапазон.
# Методы:
# add_mark - добавляет новую оценку к оценкам студента;
# + метод строкового представления, включающий в себя имя и средний балл.
class Student:
    grade_range = (1, 5)

    def __init__(self, name: str):
        self.name = name
        self._marks = []

    @property
    def average_mark(self):
        return sum(self._marks) / len(self._marks) if self._marks else 0.0

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, new_marks):
        if not all(isinstance(mark, int) and self.grade_range[0] <= mark <= self.grade_range[1] for mark in new_marks):
            raise ValueError(f"Оценки должны быть целыми числами в диапазоне {
                             self.grade_range}.")
        self._marks = new_marks

    def add_mark(self, mark: int):
        if not isinstance(mark, int) or not self.grade_range[0] <= mark <= self.grade_range[1]:
            raise ValueError(f"Оценка должна быть целым числом в диапазоне {
                             self.grade_range}.")
        self._marks.append(mark)

    def __str__(self):
        return f"{self.name}, Средний балл: {self.average_mark:.2f}"


# Примеры использования
student = Student("Иван")
print(student)

student.add_mark(4)
student.add_mark(5)
student.add_mark(3)
print(student)

student.marks = [5, 5, 4]
print(student)

try:
    student.add_mark(6)  # Некорректная оценка
except ValueError as e:
    print(e)

try:
    student.marks = [5, 6, 4]  # Некорректный список оценок
except ValueError as e:
    print(e)
