from datetime import datetime
import account_creation
import mysql.connector
import account_deposite
import account_withdraw
import account_statement
import account_details

def operation(Emp_id):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve employee name from employee details with given employee id
    #select Emp_name from employee_details where emp_id=11110001;
    query = (f"select Emp_name from employee_details where emp_id={Emp_id}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    print(f"WELCOME {result[0]}")
    print("1.ACCOUNT CREATION")
    print("2.CASH WITHDRAW")
    print("3.CASH DEPOSIT")
    print("4.STATEMENT")
    print("5.ACCOUNT DETAILS")

    # User entry for selecting option
    action = input("PLEASE SELECT THE OPERATION:")

    match action:
        case "1":
            name=input("ENTER CUSTOMER NAME:")
            address=input("ENTER CUSTOMER ADDRESS:")
            dob_input = input("ENTER DATE OF BIRTH (YYYY-MM-DD):")
            dob = datetime.strptime(dob_input, '%Y-%m-%d')

            # Calculate age based on the date of birth
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            print(f"EMPLOYEE AGE:{age} YEARS")
            mobile=int(input("ENTER MOBILE NUMBER:"))
            mail=input("ENTER MAIL ID:")
            card_requirement=input(("CARD REQUIREMENT(YES/NO):"))
            #call account creation function
            account_creation.creation(name,address,dob_input,age,mobile,mail,card_requirement)
        case "2":
            accno=input("ENTER THE ACCOUNT NUMBER:")
            amount=float(input("ENTER AMOUNT:"))
            account_withdraw.withdraw(accno,amount)
        case "3":
            accno=input("ENTER THE ACCOUNT NUMBER:")
            amount=float(input("ENTER AMOUNT:"))
            account_deposite.deposite(accno,amount)
        case "4":
            accno=input("ENTER THE ACCOUNT NUMBER:")
            account_statement.statement(accno)
        case "5":
            accno=input("ENTER THE ACCOUNT NUMBER:")
            account_details.details(accno)
        case _:
            print("You enter wrong option.Kindly enter option in between 1 & 5")