#@ WAP to accept marks of 5 students and display them in a sorted manner

marks = []

marks1 = int(input("Enter your 1 marks name : "))
marks.append(marks1)

marks2 = int(input("Enter your 2 marks name : "))
marks.append(marks2)

marks3 = int(input("Enter your 3 marks name : "))
marks.append(marks3)

marks4 = int(input("Enter your 4 marks name : "))
marks.append(marks4)

marks5 = int(input("Enter your 5 marks name : "))
marks.append(marks5)

marks.sort()
print(marks)

#print("marks: ", marks.sort(),marks)