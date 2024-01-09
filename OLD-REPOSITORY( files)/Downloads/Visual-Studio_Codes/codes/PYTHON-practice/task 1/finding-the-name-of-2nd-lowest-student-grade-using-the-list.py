
x = int(input('Enter the number of students: '))

list = []
for _ in range(x):
    name = input('Enter the name: ')
    grade = input('Enter the grade: ')
    list.append([name, grade])

grades = [score for _, score in list]
highest_grade = max(grades)
                         ###############################################################
while highest_grade in grades:
    grades.remove(highest_grade)
                                  
second_lowest_grade = max(grades)
second_lowest_student_s = sorted([name for name, score in list if score == second_lowest_grade])
                        ###############################################################
for student in second_lowest_student_s:
    print('\nThe name of the second-lowest-grade from the provided lists:',student)