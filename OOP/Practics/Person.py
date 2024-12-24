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


class Student(Person):
    def __init__(self, name: str, age: int, year: int = 1):
        super().__init__(name, age)
        self.knowledge = 0
        self.year = year

    def get_knowledge(self):
        self.knowledge += 1


class Teacher(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.students = []

    def teach(self):
        for student in self.students:
            student.get_knowledge()


class Assistant(Student, Teacher):
    def __init__(self, name: str, age: int, year: int = 1):
        Student.__init__(self, name, age, year)
        Teacher.__init__(self, name, age)


student1 = Student("Иван", 18, 1)
student2 = Student("Ольга", 19, 2)

teacher = Teacher("Елена", 35)
teacher.students.append(student1)
teacher.students.append(student2)

assistant = Assistant("Алексей", 24, 3)
assistant.students.append(student1)
assistant.students.append(student2)

print(f"Знания студентов до обучения: {
      student1.knowledge}, {student2.knowledge}")

teacher.teach()
print(f"Знания студентов после учителя: {
      student1.knowledge}, {student2.knowledge}")

assistant.teach()
print(f"Знания студентов после ассистента: {
      student1.knowledge}, {student2.knowledge}")
