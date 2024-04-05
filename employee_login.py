#module import
import mysql.connector
import bcrypt
import employee_operation

def employee_log(Emp_id,User_Name,User_Pass):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve party id from employee details with given employee id
    #select party_id from employee_details where emp_id=11110001;
    query = (f"select party_id from employee_details where emp_id={Emp_id}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a employee id
    if result:
        party_id = result[0]

        #select User_Name,User_Pass from emp_party where party_id = 'ABC002';
        query1=(f"SELECT User_Pass FROM emp_party WHERE User_Name ='{User_Name}' AND Party_id ='{party_id}'")
        # print(query1)


        try:
            cur_obj.execute(query1)
            result1 = cur_obj.fetchone()
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()

        if result1:
            # Compare the hashed password with the entered password
            if bcrypt.checkpw(User_Pass.encode('utf-8'), result1[0].encode('utf-8')):

                #Call the operation function after successful login
                employee_operation.operation(Emp_id)
            else:
                print("Incorrect password.")
        else:
            print("Invalid User Name")
    else:
        print("Invalid employee ID")
