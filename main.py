from datetime import datetime
import employee_details
import employee_login
import emp_password_reset
import customer_login
import cust_credential_reset
import atm_access

#Design as per option select and UI base
print("------------WELCOME TO ABC BANK------------")
print("===========================================")
print("===========================================")
print("1.NEW EMPLOYEE ENTRY")
print("2.EMPLOYEE RESET PASSWORD")
print("3.EMPLOYEE LOGIN")
print("4.CUSTOMER LOGIN")
print("5.CUSTOMER PASSWORD RESET")
print("6.ATM ACCESS")

#User entry for selecting option
action = input("PLEASE SELECT THE OPERATION:")

match action:
    case "1":
        # Get user input for student data
        employee_name=input("ENTER EMPLOYEE NAME:")
        designation=input("ENTER EMPLOYEE DESIGNATION:")
        dob_input = input("Enter Date of Birth (YYYY-MM-DD):")
        dob = datetime.strptime(dob_input, '%Y-%m-%d')

        # Calculate age based on the date of birth
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        print(f"EMPLOYEE AGE:{age} YEARS")
        Emp_add=input("ENTER EMPLOYEE ADDRESS:")

        employee_details.employees(employee_name,designation,dob_input,age,Emp_add)
    case "2":
        emp_id = input("ENTER EMPLOYEE ID:")
        user_id=input("ENTER EMPLOYEE LOGIN ID:")
        new_password=input("ENTER NEW PASSWORD:")
        emp_password_reset.password_reset(emp_id,user_id,new_password)

    case "3":
        # Get user input for student data
        emp_id=input("ENTER EMPLOYEE ID:")
        username=input("USERNAME:")
        password=input("PASSWORD:")
        employee_login.employee_log(emp_id,username,password)
    case "4":
        accno=input("ACCOUNT NUMBER:")
        username = input("USERNAME:")
        password = input("PASSWORD:")
        customer_login.customer(accno,username,password)
    case "5":
        accno=input("ENTER ACCOUNT NUMBER:")
        new_password=input(("NEW PASSWORD:"))
        cust_credential_reset.password_reset(accno,new_password)

    case "6":
        accno=input("ENTER ACCOUNT NUMBER:")
        atm_card=input("ENTER ATM CARD NUMBER:")
        atm_pin=int(input("ENTER ATM PIN:"))
        atm_cvv=int(input("ENTER ATM CVV:"))
        atm_access.atm_access(accno,atm_card,atm_pin,atm_cvv)
    case _:
        print("You enter wrong option.Kindly enter option in between 1 & 3")