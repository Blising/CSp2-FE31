class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.grades = {}

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def add_grades(self, semester, *grades):
        self.grades[semester] = list(map(int, grades))

    def average_grade_semester(self, semester):
        return sum(self.grades.get(semester, [])) / len(self.grades.get(semester, [])) if semester in self.grades else None

    def average_grade_overall(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def best_semester(self):
        return max(self.grades, key=lambda x: sum(self.grades[x]) / len(self.grades[x]))

    def worst_semester(self):
        return min(self.grades, key=lambda x: sum(self.grades[x]) / len(self.grades[x]))

student = Student("Naruto", "uzumaki")   
student.add_grades(1, 5, 5, 5, 5, 100, 100, 100, 100)  
student.add_grades(2, 5, 5, 5, 5, 100, 100, 100, 420)  
student.add_grades(3, 5, 5, 5, 5, 100, 100, 100, 740)
print(student.average_grade_semester(2))
print(student.average_grade_overall())
print(student.best_semester())
print(student.worst_semester())
class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.grades = {}

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def add_grades(self, semester, *grades):
        self.grades[semester] = list(map(int, grades))

    def average_grade_semester(self, semester):
        return sum(self.grades.get(semester, [])) / len(self.grades.get(semester, [])) if semester in self.grades else None

    def average_grade_overall(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades)

    def best_semester(self):
        return max(self.grades, key=lambda x: sum(self.grades[x]) / len(self.grades[x]))

    def worst_semester(self):
        return min(self.grades, key=lambda x: sum(self.grades[x]) / len(self.grades[x]))

student = Student("Naruto", "uzumaki")   
student.add_grades(1, 5, 5, 5, 5, 100, 100, 100, 100)  
student.add_grades(2, 5, 5, 5, 5, 100, 100, 100, 420)  
student.add_grades(3, 5, 5, 5, 5, 100, 100, 100, 740)
print(student.average_grade_semester(2))
print(student.average_grade_overall())
print(student.best_semester())
print(student.worst_semester())
