# Напишите классы Person (Человек), Student (Студент), Teacher (Учитель), Assistant (Ассистент).
# Схема иерархии классов под описанием задания. У человека есть имя и возраст. Студент наследуется
# от человека, у него, кроме свойств, унаследованных от человека, есть знания (при инициализации
# равны нулю) и год обучения (при инициализации может быть задан, но по умолчанию равен 1). У
# студента также есть метод get_knowledge (получать знания), прибавляющий 1 к его знаниям. У
# учителя, кроме свойств человека, есть список его студентов, а также метод teach (учить), который
# проходится циклом по списку студентов и прибавляет им знания. Ассистент — это аспирант, который
# является и студентом, и учителем, а значит, наследует свойства и методы и одного, и второго.
# Продемонстрируйте работу ассистента. 

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Person):
    def __init__(self, name: str, age: int, year_of_study: int = 1):
        super().__init__(name, age)
        self.knowledge = 0
        self.year_of_study = year_of_study

    def get_knowledge(self):
        self.knowledge += 1

    def __str__(self):
        return super().__str__() + f", Знания: {self.knowledge}, Год обучения: {self.year_of_study}"


class Teacher(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def teach(self):
        for student in self.students:
            student.get_knowledge()

    def __str__(self):
        return super().__str__() + f", Студенты: {[student.name for student in self.students]}"


class Assistant(Student, Teacher):
    def __init__(self, name: str, age: int, year_of_study: int = 1):
        Student.__init__(self, name, age, year_of_study)
        Teacher.__init__(self, name, age)

    def __str__(self):
        return super().__str__() + ", Роль: Ассистент"


# Пример использования классов
if __name__ == "__main__":
    # Создаем студентов
    student1 = Student("Иван", 20)
    student2 = Student("Мария", 21)

    # Создаем учителя и добавляем студентов
    teacher = Teacher("Алексей", 40)
    teacher.add_student(student1)
    teacher.add_student(student2)

    # Создаем ассистента
    assistant = Assistant("Ольга", 25)

    # Ассистент получает знания
    assistant.get_knowledge()
    
    # Учитель обучает студентов
    teacher.teach()

    # Выводим информацию о студентах и ассистенте
    print(student1)  # Знания: 1
    print(student2)  # Знания: 1
    print(assistant)  # Знания: 1

    # Выводим информацию о учителе и его студентах
    print(teacher)  # Студенты: ['Иван', 'Мария']
