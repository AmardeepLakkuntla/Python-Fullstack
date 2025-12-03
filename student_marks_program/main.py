name = input("Enter student name: ")

mark1 = int(input("Enter marks for Subject 1: "))
mark2 = int(input("Enter marks for Subject 2: "))
mark3 = int(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent Name:", name)
print("Subject 1:", mark1)
print("Subject 2:", mark2)
print("Subject 3:", mark3)
print("Total Marks:", total)
print("Average Marks:", average)
