# Create a payroll system where:

# Employee details stored in dictionary

# Salary calculation includes:

# Basic salary

# HRA (20%)

# DA (10%)

# Tax (5%)

# Display payslip


employees = {}

def add_employee(emp_id, name, basic):
    employees[emp_id] = {"name": name, "basic": basic}
    print("Employee added")

def calculate_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    tax = basic * 0.05
    net_salary = basic + hra + da - tax
    return hra, da, tax, net_salary

def display_payslip(emp_id):
    if emp_id not in employees:
        print("Employee not found")
        return

    emp = employees[emp_id]
    hra, da, tax, net = calculate_salary(emp["basic"])

    print("\n--- PAY SLIP ---")
    print("Name:", emp["name"])
    print("Basic:", emp["basic"])
    print("HRA:", hra)
    print("DA:", da)
    print("Tax:", tax)
    print("Net Salary:", net)

add_employee(101, "Ravi", 25000)
display_payslip(101)