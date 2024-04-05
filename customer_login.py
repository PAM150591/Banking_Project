import mysql.connector
import bcrypt
import customer_operation


def customer(Accno,User_Name,User_Pass):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #select party_id from employee_details where emp_id=11110001;
    query = (f"select Cust_name,party_id from customer_details where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a employee id
    if result:
        cust_name,party_id=result

        #select User_Pass from cust_party where party_id = 'ABC002';
        query1=(f"SELECT User_Pass FROM cust_party WHERE User_Name ='{User_Name}' AND Party_id ='{party_id}'")
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
                customer_operation.operation(Accno,cust_name,party_id)
            else:
                print("WRONG CREDENTIAL")
        else:
            print("WRONG CREDENTIAL")

    else:
        print("WRONG CREDENTIAL")

    conn_obj.close()