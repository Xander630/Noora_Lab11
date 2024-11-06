Grades = []
students = 0
studentspassed = 0
while True:
    grade = int(input("Enter a Student Grade : "))
    if grade < 40 or grade > 100:
        print("Invalid Grade")
        break
    else:
        students += 1
        Grades.append(grade)
        if grade >= 75:
            studentspassed += 1
    Again = input("Do you want to enter another grade? (yes/no): ")
    if Again.lower() == "no":
        result = sum(Grades) / students
        print("The Average Grade is: ", result)
        print("The Number of Students Passed: ", studentspassed)
        Percentage = (studentspassed / students) * 100
        print(f"The Passing Percentage is: {Percentage:2f}%")
        break 
    else:
        continue
        
    
    