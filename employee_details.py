#module import
import mysql.connector
import functions


#Define employee function
def employees(Emp_name,Designation,DOB,Emp_age,Emp_address):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve last party id from employee details
    query = "SELECT party_id FROM employee_details ORDER BY party_id DESC LIMIT 1"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a last employee party code
    if result:
        last_party_id = result[0]

        #Call the function of cout next party id
        employee_party_id=functions.party_id_count(last_party_id)

    else:
        # No non-null employee codes found, use the initial format
        employee_party_id = "ABC001"


    # Build the query with user-provided name using LIKE operator
    # insert into employee_details(Emp_name,Designation,DOB,Emp_age,Emp_address,party_id) values("PAM","Casher","2023-11-11",32,"NEWTOWN,KOLKATA-700153","ABC001");
    sql = "INSERT INTO employee_details (Emp_name, Designation, DOB, Emp_age,Emp_address,party_id) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (Emp_name, Designation, DOB, Emp_age,Emp_address,employee_party_id)

    try:
        cur_obj.execute(sql,data)
        print("NEW EMPLOYEE ENTRY SUCCESSFUL.")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    #Retrieve Emp_id from employee details
    query = "SELECT Emp_id FROM employee_details ORDER BY Emp_id DESC LIMIT 1"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a last employee Id
    last_employee_id = result[0]

    #Call function for create login id
    log_id=functions.create_login_id(Emp_name,DOB)

    #call function for create password
    log_password=functions.create_password()

    #call fuction for encrypt the password
    ecrypt_password=functions.encrypt_password(log_password)

    #When employee account is created then employee status will be ACTIVE
    status="ACTIVE"

    # Build the query with user-provided name using LIKE operator
    # insert into employee_details(Emp_name,Designation,DOB,Emp_age,Emp_address,party_id) values("PAM","Casher","2023-11-11",32,"NEWTOWN,KOLKATA-700153","ABC001");
    sql1 = "INSERT INTO emp_party (Party_id,User_Name,User_Pass,Emp_Status) VALUES (%s, %s, %s, %s)"
    data1 = (employee_party_id,log_id,ecrypt_password,status)

    try:
        cur_obj.execute(sql1,data1)
        print("Username:",log_id)
        print("Password:",log_password)
        print("Kindly Change Your Password From yourself")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


    conn_obj.close()