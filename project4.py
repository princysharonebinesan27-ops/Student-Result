print("==========STUDENT RESULT==========")
name = input("\nenter student name:")
tamil = int(input("\nenter tamil mark:"))
english = int(input("\nenter english mark:"))
maths = int(input("\nenter maths mark:"))
science = int(input("\nenter science mark:"))
computer = int(input("\nenter computer mark:"))
total = tamil + english + maths + science + computer
print("\nTotal Marks:",total,"/500")
average = total / 5
print("\nAverage:",average,"%")
if average>= 90:
    grade = "A"
elif average>= 85:
    grade= "B"
elif average>= 75:
    grade = "C"
elif average>= 35:
    grade = "good"
else:
    grade = "fail"
print("\nGrade:",grade)
if average>= 35:
    result = "pass"
else:
    result = "fail"
print("\nResult:",result)
