import mysql.connector

def atm_statement(Accno):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    # SQL query to fetch recent transactions
    query=(f"SELECT Transaction_date,Transaction_type,Amount,Balance FROM transaction WHERE Accno ={Accno} ORDER BY transaction_date DESC LIMIT 5")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchall()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    if result:
        print("DATE    |  TYPE     |  AMOUNT |  BALANCE  ")
        print("----------------------------------------------")
        for statement in result:
            print(
                f"{statement[0]}  |  {statement[1]}  |  {statement[2]}   |  {statement[3]}")
    else:
        print("TECHNICAL ERROR. KINDLY TRY AGAIN")

    cur_obj.close()
    conn_obj.close()
