class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def __repr__(self):
        return f"{self.name}: {self.score}"

students = [Student("Joe",0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zach", 0.75), Student("Sarah", 0.63)]

#show all the students, who did not pass
failing_students = []
for student in students:
    if student.score < 0.7:
        failing_students.append(student)

filtered_list = list(filter(lambda student: student.score < 0.7, students))

print(filtered_list)

#challenge
#use filter to list all even numbers

numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)