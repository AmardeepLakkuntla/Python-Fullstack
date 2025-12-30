# Problem 3: Employee Performance Appraisal (IF-ELIF-ELSE)

name = input("Enter employee name: ")
salary = float(input("Enter base salary: "))
score = int(input("Enter performance score: "))

if score >= 90:
    bonus = salary * 0.20
    print("Performance: Excellent")
elif score >= 75:
    bonus = salary * 0.10
    print("Performance: Good")
elif score >= 60:
    bonus = salary * 0.05
    print("Performance: Average")
else:
    bonus = 0
    print("Performance: Needs Improvement")

final_salary = salary + bonus
print("Final salary for", name, "is:", final_salary)