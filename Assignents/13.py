print("Enter the marks entered by the student : ")
w=float(input("Writing Marks Scored: "))
l=float(input("Lab exams Scored: "))
a=float(input("Assignments Scored: "))

grade=(w*70)/100 + (l*20)/100 +(a*10)/100

print(f"Grade of the student is {grade}")