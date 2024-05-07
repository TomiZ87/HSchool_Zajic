def choice():
    while True:
        choices = input("1. Super - Gross Salary, 2. Gross Salary, 3. Net Salary: ")
        if choices == "1": supergross()
        elif choices == "2": gross()
        elif choices == "3": net()
        else: print("Try again")
def supergross():
    supergross_num = float(input("Enter your supergross salary: "))
    gross_num = supergross_num / 1.352
    employer_ded = gross_num * 0.352
    after_deductions = gross_num / 1.134
    employee_ded = after_deductions * 0.134
    if after_deductions <= 410.24:
        tax = 0
        net_num = after_deductions
    else:
        net1_num = (after_deductions - 410.24) / 1.19
        net_num = net1_num + 410.24
        tax = net1_num * 0.19
    print("Employer Deductions: ", round(employer_ded, 2))
    print("Gross Salary: ", round(gross_num, 2))
    print("Employee Deductions: ", round(employee_ded, 2))
    print("After deductions: ", round(after_deductions, 2))
    print("Tax: ", round(tax, 2))
    print("Net income: ", round(net_num, 2))
    
def gross():
    gross_num = float(input("Enter your gross salary: "))
    supergross_num = gross_num * 1.352
    employer_ded = gross_num * 0.352
    after_deductions = gross_num / 1.134
    employee_ded = after_deductions * 0.134
    if after_deductions <= 410.24:
        tax = 0
        net_num = after_deductions
    else:
        net1_num = (after_deductions - 410.24) / 1.19
        net_num = net1_num + 410.24
        tax = net1_num * 0.19
    print("Employer Deductions: ", round(employer_ded, 2))
    print("SuperGross Salary: ", round(supergross_num, 2))
    print("Employee Deductions: ", round(employee_ded, 2))
    print("After deductions: ", round(after_deductions, 2))
    print("Tax: ", round(tax, 2))
    print("Net income: ", round(net_num, 2))
def net():
    net_num = float(input("Enter your net salary: "))
    if net_num > 410.24:
        tax = (net_num - 410.24) * 0.19
        after_deductions = net_num + tax
    else:
        tax = 0
        after_deductions = net_num
    employee_ded = after_deductions * 0.134
    gross_num = after_deductions + employee_ded
    employer_ded = gross_num * 0.352
    supergross_num = gross_num + employer_ded
    print("SuperGross Salary: ", round(supergross_num, 2))
    print("Employer Deductions: ", round(employer_ded, 2))
    print("Gross Salary: ", round(gross_num, 2))
    print("Employee Deductions: ", round(employee_ded, 2))
    print("After deductions: ", round(after_deductions, 2))
    print("Tax: ", round(tax, 2))

choice()
