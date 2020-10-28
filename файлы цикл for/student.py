num = int(input("Ииедите кол-во студентов:"))
student_file = open('student.txt', 'w')
for i in range(num):
    student = input()
    student_file.write(student+ ' ')
student_file.close()
student_read = open('student.txt')
student_list = student_read.readlines()
for student in student_list:
    print(student)