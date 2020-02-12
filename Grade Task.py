##Made by Ryan S##
student_id = int(input("Enter Student ID: "))
exam_mark = int(input("Enter exam result: "))
A = 90
B = 70
C = 50
if exam_mark >= 90:
    print ("A Grade")
if exam_mark >= 70 and exam_mark <90:
    print ("B Plus")
if exam_mark >= 50 and exam_mark <69:
    print ("C Minus")
if exam_mark == 69:
    print ("Nice you got a C+")
if exam_mark <50:
    print ("Sorry fam you failed thine test")
