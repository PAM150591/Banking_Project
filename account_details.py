import mysql.connector

def details(Accno):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #select all from customer details accrording to given account number;
    query = (f"select * from customer_details where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result=cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error:",e)
        conn_obj.rollback()

    #Print the retrieved data using list unpacking

    if result:
        Acco,name,address,dob,age,mobile,party_id,status,balance=result # Unpacking the row into variables

        # Print data in proper sequence using f-strings
        print("  ACCOUNT DETAILS  ")
        print("-------------------")
        print(f"ACCOUNT DETAILS:{Acco}")
        print(f"NAME:{name}")
        print(f"ADDRESS:{address}")
        print(f"DATE OF BIRTH:{dob}")
        print(f"AGE:{age}")
        print(f"MOBILE:{mobile}")
        print(f"CURRENT BALANCE:{balance}")
    else:
        print("WRONG ACCOUNT NUMBER")

    cur_obj.close()
    conn_obj.close()