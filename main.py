# main program

num_of_students = int(input('Kindly enter the number of students :'))
while num_of_students <= 0:
    print('The number of the students must be positive')
    num_of_students = int(input('Kindly enter the number of students :'))

names = []
grades = []

while num_of_students > 0:
    name = input('Enter the name of the student :')
    names.append(str(name))
    grade = float(input('Enter his grade : '))
    while grade < 0 or grade > 100:
        print('The grade must be between 0 and 100')
        grade = float(input('Enter his grade : '))
    grades.append(grade)
    num_of_students -= 1

# display_student_summary (names,grades)