# fuction 'display_student_summary' : Prints students names and grades

def display_student_summary (S,G):
    
    for i in range(len(S)):
        print('Name :', S[i] , ', Grade :', G[i])

# function 'get_avg_grade' : Prints the average grade of the class

def get_avg_grade (G):
    
    sum = 0
    for i in range(len(G)):
        sum += float(G[i])
    return float(sum/len(G))

# function 'get_heighest_grade' : Prints the highest grade earned (Student name and grade)

def get_heighest_grade (S,G):

    j = 0
    k = 0
    for i in range(len(S)):
        if j < float(G[i]):
            j = float(G[i])
            k = i
    print('The highest grade is', j, 'earned by :', S[k])

# function 'count_passed' : Prints the count of students who passed (grade >= 60)

# main program

num_of_students = int(input('Kindly enter the number of students : '))
while num_of_students <= 0:
    print('The number of the students must be positive')
    num_of_students = int(input('Kindly enter the number of students : '))

names = []
grades = []

while num_of_students > 0:
    name = input('Enter the name of the student : ')
    names.append(str(name))
    grade = float(input('Enter his grade : '))
    while grade < 0 or grade > 100:
        print('The grade must be between 0 and 100')
        grade = float(input('Enter his grade : '))
    grades.append(grade)
    num_of_students -= 1

display_student_summary (names,grades)
print('The average grade of the class is :', get_avg_grade (grades))
get_heighest_grade (names,grades)
