import mysql.connector

# conn_obj = functions.sql_connection()
# cur_obj = conn_obj.cursor()
def activate(party_id,upi_pin,conn_obj,cur_obj):

    status="ACTIVATE"

    # Update data in upi details according to party id
    query1 = (f"UPDATE upi_details SET upi_pin={upi_pin}, status='{status}' WHERE Party_id='{party_id}'")
    # print(query1)

    try:
        cur_obj.execute(query1)
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    cur_obj.close()
    conn_obj.close()

def sender_name(sender_upi,conn_obj,cur_obj):
    # Select sender name from customer detail using sender_upi
    query2 = (f"SELECT Cust_name FROM customer_details WHERE Party_id=(SELECT Party_id FROM upi_details WHERE mail_upi_id ='{sender_upi}' OR mob_upi_id = '{sender_upi}');")
    # print(query2)

    try:
        cur_obj.execute(query2)
        result1 = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    sender_name = result1[0]
    return sender_name

    cur_obj.close()
    conn_obj.close()

    def upi_transfer():
        print("")