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
    def __init__(self, name: str, grade_range: tuple[int, int]):
        self.name = name
        self._marks = []
        self.grade_range = grade_range

    @property
    def average_mark(self) -> float:
        if not self._marks:
            return 0.0
        return sum(self._marks) / len(self._marks)

    @property
    def marks(self) -> list[int]:
        return self._marks

    @marks.setter
    def marks(self, value: list[int]):
        if not all(isinstance(mark, int) for mark in value):
            raise ValueError("Все оценки должны быть целыми числами.")
        if not all(self.grade_range[0] <= mark <= self.grade_range[1] for mark in value):
            raise ValueError(f"Оценки должны быть в диапазоне {self.grade_range}.")
        self._marks = value

    def add_mark(self, mark: int):
        if not isinstance(mark, int):
            raise ValueError("Оценка должна быть целым числом.")
        if not (self.grade_range[0] <= mark <= self.grade_range[1]):
            raise ValueError(f"Оценка должна быть в диапазоне {self.grade_range}.")
        self._marks.append(mark)

    def __str__(self) -> str:
        return f"{self.name}, Средний балл: {self.average_mark:.2f}"


class Group:
    def __init__(self, name: str):
        self.name = name
        self._students = []

    @property
    def students(self) -> list[str]:
        return [student.name for student in self._students]

    @property
    def average_mark(self) -> float:
        if not self._students:
            return 0.0
        total_marks = sum(student.average_mark for student in self._students)
        return total_marks / len(self._students)

    def add_student(self, student: Student):
        self._students.append(student)

    def remove_student(self, student: Student):
        self._students.remove(student)

# Пример использования
if __name__ == "__main__":
    student1 = Student("Иван", (1, 5))
    student1.add_mark(4)
    student1.add_mark(5)
    
    student2 = Student("Мария", (1, 5))
    student2.add_mark(3)
    student2.add_mark(4)

    group = Group("Группа 1")
    group.add_student(student1)
    group.add_student(student2)

    print(student1)  # Иван, Средний балл: 4.50
    print(student2)  # Мария, Средний балл: 3.50
    print(f"Студенты в группе: {group.students}")  # Студенты в группе: ['Иван', 'Мария']
    print(f"Средний балл группы: {group.average_mark:.2f}")  # Средний балл группы: 4.00
