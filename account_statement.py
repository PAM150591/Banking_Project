import mysql.connector

def statement(Accno):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #select all from transaction detil accrording to given account number;
    query = (f"select * from transaction where Accno={Accno}")

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchall()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    if result:
        print("TRANSACTION  |  TYPE     | MODE    |      DATE-TIME       |  AMOUNT |  BALANCE  ")
        print("-------------------------------------------------------------------------")
        for statement in result:
            print(
                f"{statement[0]}         |  {statement[2]}  |  {statement[3]}   |  {statement[4]},{statement[5]} |  {statement[6]}   |   {statement[7]}")
    else:
        print("WRONG ACCOUNT NUMBER")

    conn_obj.close()

