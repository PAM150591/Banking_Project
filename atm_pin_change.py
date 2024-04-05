import mysql.connector

def atm_pin(accno,atm_pin):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    # SQL query to fetch recent transactions
    query1=(f"select Party_id from customer_details where Accno = {accno}")

    try:
        cur_obj.execute(query1)
        result1 = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of account number
    if result1:
        party_id = result1[0]

        # Validate current PIN
        query2 = (f"SELECT COUNT(*) FROM atm_details WHERE Party_id = '{party_id}' AND card_pin = {atm_pin}")

        try:
            cur_obj.execute(query2)
            result2 = cur_obj.fetchone()
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()

            if result2[0] == 0:
                print("INCORRECT PIN. PLEASE TRY AGAIN.")
                exit()

        # Get new PIN and confirmation
        new_pin = input("ENTER NEW PIN:")
        confirm_new_pin = input("CONFIRM NEW PIN:")
        if new_pin != confirm_new_pin:
            print("PINs DO NOT MATCH. PLEASE TRY AGAIN.")
            exit()

        # Update PIN in the database
        query3 = (f"UPDATE atm_details SET card_pin = {new_pin} WHERE Party_id = '{party_id}'")

        cur_obj.execute(query3)
        result2 = cur_obj.fetchone()
        conn_obj.commit()

        print("PIN CHANGE SUCCESSFULLY")
    else:
        print("TECHNICAL ERROR. KINDLY TRY AGAIN")