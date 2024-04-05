import mysql.connector
import functions


def password_reset(Accno,new_User_Pass):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve party id from employee details with given employee id
    #select party_id from customer_details where Accno=11110001;
    query = (f"select party_id from customer_details where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of Account number
    if result:
        party_id = result[0]
        # call fuction for encrypt the password
        ecrypt_password = functions.encrypt_password(new_User_Pass)

        # Build the query with user-provided password using LIKE operator
        # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition;
        query1 = (f"UPDATE cust_party SET User_Pass = '{ecrypt_password}' WHERE Party_id ='{party_id}'")

        try:
            cur_obj.execute(query1)
            print("YOUR PASSWORD HAS BEEN RESET SUCCESSFULLY!")
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()
    else:
        print("INVALID ACCOUNT NUMBER")

    conn_obj.close()



def username_reset(Accno,User_name):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve party id from employee details with given employee id
    #select party_id from customer_details where Accno=11110001;
    query = (f"select party_id from customer_details where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of Account number
    if result:
        party_id = result[0]

        # Build the query with user-provided password using LIKE operator
        # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition;
        query1 = (f"UPDATE cust_party SET User_Name = '{User_name}' WHERE Party_id ='{party_id}'")

        try:
            cur_obj.execute(query1)
            print("YOUR USERNAME HAS BEEN RESET SUCCESSFULLY!")
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()
    else:
        print("INVALID ACCOUNT NUMBER")

    conn_obj.close()