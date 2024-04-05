import mysql.connector


def online_transfer(from_accno,to_accno,to_username,amount):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()


    #Retrieve balance from customer details acording to account
    query = (f"SELECT Balance FROM customer_details WHERE Accno={from_accno}")
    # print(query)

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
        # print(prev_balance)

        if prev_balance >= amount:

            # adding with previous balance with given amount
            cur_balance = float(prev_balance) - float(amount)
            # print(cur_balance)

            # This is deposit type transaction
            transaction_type = "WITHDRAW"

            # This is cash mode transaction
            transaction_mode = "ONLINE"

            # create query for insert value into transaction table
            sql = "INSERT INTO transaction (Accno,Transaction_type,Transaction_mode,Amount,Balance) VALUES (%s, %s, %s, %s, %s)"
            date = (from_accno, transaction_type, transaction_mode, amount, cur_balance)

            # Quary for update balance in customer table
            # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition
            query1 = (f"UPDATE customer_details SET Balance={cur_balance} WHERE Accno={from_accno} ")
            # print(query1)

            try:
                cur_obj.execute(sql, date)
                cur_obj.execute(query1)
                conn_obj.commit()
            except mysql.connector.Error as e:
                print("Error retrieving data from MySQL:", e)
                conn_obj.rollback()

            #Deposite to other account
            # Retrieve balance from customer details acording to account
            query2 = (f"SELECT Balance FROM customer_details WHERE Accno={to_accno} and Cust_name='{to_username}'")
            # print(query2)

            try:
                cur_obj.execute(query2)
                result1 = cur_obj.fetchone()
                conn_obj.commit()
            except mysql.connector.Error as e:
                print("Error retrieving data from MySQL:", e)
                conn_obj.rollback()

            # Handle cases based on the presence of a account number
            if result:
                prev_balance1 = result1[0]
                # print(prev_balance1)

                # adding with previous balance with given amount
                cur_balance1 = float(prev_balance1) + float(amount)
                # print(cur_balance1)

                # This is deposit type transaction
                transaction_type = "DEPOSIT"

                # This is cash mode transaction
                transaction_mode = "ONLINE"

                # create query for insert value into transaction table
                sql1 = "INSERT INTO transaction (Accno,Transaction_type,Transaction_mode,Amount,Balance) VALUES (%s, %s, %s, %s, %s)"
                date1 = (to_accno, transaction_type, transaction_mode, amount, cur_balance1)

                # Quary for update balance in customer table
                # UPDATE table_name SET column1 = value1, column2 = value2, ...WHERE condition
                query3 = (f"UPDATE customer_details SET Balance={cur_balance1} WHERE Accno={to_accno} and Cust_name='{to_username}'")
                # print(query3)

                try:
                    cur_obj.execute(sql1, date1)
                    cur_obj.execute(query3)
                    conn_obj.commit()
                except mysql.connector.Error as e:
                    print("Error retrieving data from MySQL:", e)
                    conn_obj.rollback()
                print("TRANSFER SUCCESSFULLY")
            else:
                print("WRONG RECIPIENT ACCOUNT NUMBER")

        else:
            print("INSUFFICIENT BALANCE TO WITHDRAW")

    else:
        print("WRONG ACCOUNT NUMBER")

    cur_obj.close()
    conn_obj.close()
