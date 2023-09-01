#Multiply to 100, for example if it's 0.33 then your debt to income ratio is 33%

print('''
Debt To Income Calculator
=========================
''')
restart = "y"
def dti_calc():
    total_debt = input('''Enter Gross Monthly debt: ''')
    total_debt = float(total_debt)
    gross_monthly_income = input('''Enter Gross Monthly Income: ''')
    gross_monthly_income = float(gross_monthly_income)
    print('''
    Here is your debt to income percentage:
    ''')
    print(total_debt/gross_monthly_income)
while restart == "y":
    dti_calc()
    continue_question = input('''
    Do you want to continue? Y/N: ''').lower()
    restart = continue_question
    if restart == "y":
     continue
else:
    print('''
         Goodbye!''')