import mysql.connector


def atm_balance(Accno):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    # select all from customer details accrording to given account number;
    query = (f"select Balance from customer_details where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error:", e)
        conn_obj.rollback()

    # Print the retrieved data using list unpacking

    if result:

        current_balance=float(result[0])

        # Print data in proper sequence using f-strings

        print(f"CURRENT BALANCE:{current_balance}")
    else:
        print("TECHNICAL ERROR. KINDLY TRY AGAIN")

    cur_obj.close()
    conn_obj.close()