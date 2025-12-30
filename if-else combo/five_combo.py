def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


def attendance_status(attendance):
    if attendance >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


def scholarship_check(marks, attendance):
    if marks >= 85 and attendance >= 90:
        return "Eligible for Scholarship"
    elif marks >= 70 and attendance >= 80:
        return "Partial Scholarship"
    else:
        return "Not Eligible"


def remarks(marks):
    if marks >= 90:
        return "Excellent performance"
    elif marks >= 75:
        return "Very good"
    elif marks >= 60:
        return "Good"
    elif marks >= 40:
        return "Needs improvement"
    else:
        return "Poor performance"


def hostel_eligibility(distance):
    if distance >= 50:
        return "Hostel Allowed"
    else:
        return "Hostel Not Allowed"