import mysql.connector


def withdraw(Accno,Amount):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #Retrieve balance from customer details acording to account
    query = (f"SELECT Balance FROM customer_details WHERE Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a account number
    if result:
        prev_balance = result[0]

        if prev_balance >= Amount:

            # adding with previous balance with given amount
            cur_balance = float(prev_balance) - float(Amount)

            # This is deposit type transaction
            transaction_type = "WITHDRAW"

            # This is cash mode transaction
            transaction_mode = "CASH"

            # create query for insert value into transaction table
            sql = "INSERT INTO transaction (Accno,Transaction_type,Transaction_mode,Amount,Balance) VALUES (%s, %s, %s, %s, %s)"
            date = (Accno, transaction_type, transaction_mode, Amount, cur_balance)

            # Quary for update balance in customer table
            # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition
            query1 = (f"UPDATE customer_details SET Balance={cur_balance} WHERE Accno={Accno} ")

            try:
                cur_obj.execute(sql, date)
                cur_obj.execute(query1)
                conn_obj.commit()
            except mysql.connector.Error as e:
                print("Error retrieving data from MySQL:", e)
                conn_obj.rollback()

            print(f"ACCOUNT NUMBER:{Accno}")
            print(f"PREVIOUS BALANCE:{prev_balance}")
            print(f"CURRENT BALANCE:{cur_balance}")
            print(f"=============================")

        else:
            print("INSUFFICIENT BALANCE TO WITHDRAW")

    else:
        print("WRONG ACCOUNT NUMBER")

    conn_obj.close()
