import statistics
class Student:

    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

    def get_grade(self):
        return self._grade

def basic_stats(student_list):
    grades = []
    for student in student_list:
        grades.append(student.get_grade())


    return (
    f'Mean: {statistics.mean(grades)}',
    f'Median: {statistics.median(grades)}',
    f'Mode: {statistics.mode(grades)}'
    )

s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]
print(basic_stats(student_list))  # should print a tuple of three values

