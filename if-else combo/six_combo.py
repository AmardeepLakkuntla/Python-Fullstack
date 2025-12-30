from five_combo import (
    check_pass_fail,
    calculate_grade,
    attendance_status,
    scholarship_check,
    remarks,
    hostel_eligibility
)

print("----- STUDENT PORTAL -----")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
distance = int(input("Enter distance from college (km): "))

print("\n--- STUDENT REPORT ---")
print("Name:", name)
print("Roll No:", roll)

result = check_pass_fail(marks)
print("Result:", result)

grade = calculate_grade(marks)
print("Grade:", grade)

attendance_result = attendance_status(attendance)
print("Attendance:", attendance_result)

scholarship = scholarship_check(marks, attendance)
print("Scholarship:", scholarship)

final_remarks = remarks(marks)
print("Remarks:", final_remarks)

hostel = hostel_eligibility(distance)
print("Hostel Status:", hostel)

if result == "Fail":
    print("\n⚠ Warning: Student has failed. Improvement required.")
else:
    print("\n✅ Student is promoted to next semester.")