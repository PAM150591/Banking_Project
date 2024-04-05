import customer_mail
import functions
import mysql.connector
import datetime


def creation(Cust_name, Cust_address, DOB, Cust_age, Mob,mail, card_issue):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    # Retrieve last party id from employee details
    query = "SELECT Party_id FROM customer_details ORDER BY party_id DESC LIMIT 1"

    try:
        cur_obj.execute(query)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a last customer party code
    if result:
        last_party_id = result[0]

        # Call the function of cust_party_count
        cust_party_id = functions.cust_party_count(last_party_id)

    else:
        # No non-null employee codes found, use the initial format
        cust_party_id = "ABC0000001"

    # At time of account creation account status will be 'ACTIVE'
    acc_status = 'ACTIVE'

    # At time of account creation account balance will be '0'.
    balance = 0.0

    # Build the query with user-provided name using LIKE operator
    # insert into customer_details(Cust_name,Cust_address,DOB,Cust_age,Mob,Party_id,Acc_Status,Balance) values("PAM","Casher","2023-11-11",32,"NEWTOWN,KOLKATA-700153","ABC001");
    sql = "INSERT INTO customer_details (Cust_name,Cust_address,DOB,Cust_age,Mob,mail_id,Party_id,Acc_Status,Balance,card_issue) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
    data = (Cust_name, Cust_address, DOB, Cust_age, Mob,mail, cust_party_id, acc_status, balance, card_issue)

    try:
        cur_obj.execute(sql, data)
        print("NEW ACCOUNT CREATION SUCCESSFUL.")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    #Creation for log in id and password
    # Retrieve Account number,party number from customer details
    query1 = "SELECT Accno,Party_id FROM customer_details ORDER BY party_id DESC LIMIT 1"

    try:
        cur_obj.execute(query1)
        result = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a last employee Id
    Accno = result[0]
    Cust_party_id = result[1]

    # Call function for create customer login id
    log_id = functions.cust_login_id(Cust_name, DOB)

    # call function for create password
    log_password = functions.create_password()

    # call fuction for encrypt the password
    ecrypt_password = functions.encrypt_password(log_password)

    # When customer login id  is created then employee status will be ACTIVE
    status = "ACTIVE"

    # Build the query with user-provided name using LIKE operator
    sql1 = "INSERT INTO cust_party (Party_id,User_Name,User_Pass,Cust_Status) VALUES (%s, %s, %s, %s)"
    data1 = (Cust_party_id, log_id, ecrypt_password, status)

    try:
        cur_obj.execute(sql1, data1)
        print("ACCOUNT NUMBER:", Accno)
        print("USERNAME:", log_id)
        print("PASSWORD:", log_password)
        print("Kindly Change Your Password From yourself")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


    #upi id creation
    mail_upi=functions.mail_upi_generate(mail)
    mob_upi=str(Mob) + "@okabc"
    status="DEACTIVATE"

    sql2 = "INSERT INTO upi_details (Party_id,mail_upi_id,mob_upi_id,status) VALUES (%s, %s, %s, %s)"
    data2 = (Cust_party_id, mail_upi, mob_upi, status)

    try:
        cur_obj.execute(sql2, data2)
        print("========================")
        print("UPI ID1:", mail_upi)
        print("OR")
        print("UPI ID2:", mob_upi)
        print("Kindly Activate your upi id")
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()


    #Creation of ATM card details
    if card_issue == "YES":

        # Retrieve last party card number from employee details
        query2 = "SELECT card_number FROM atm_details ORDER BY card_number DESC LIMIT 1"

        try:
            cur_obj.execute(query2)
            result = cur_obj.fetchone()
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()

        # Handle cases based on the presence of a last customer party code
        if result:
            card_number = result[0]

            # Call the function of cust_party_count
            card_new_number = functions.generate_card_number(card_number)

        else:
            # No non-null employee codes found, use the initial format
            card_new_number = "1000202400000000"

        # create 4 digit atm pin number
        pin_number = functions.generate_atm_pin()

        # create 3 digit cvv number
        cvv_number = functions.generate_cvv_number()

        #To create issue date and expiry date
        today = datetime.date.today()

        # Get issue date in MM/YYYY format
        issue_date = today.strftime("%m/%Y")

        # Calculate expiry date by adding 5 years
        expiry_date = (today + datetime.timedelta(days=365 * 5)).strftime("%m/%Y")

        #Card Status-Active
        card_status="ACTIVE"

        # Store the details in atm_details table
        sql2 = "INSERT INTO atm_details (Party_id,card_number,card_pin,cvv_number,issue_date,valid_date,status) VALUES (%s, %s, %s,%s, %s, %s,%s)"
        data2=(Cust_party_id,card_new_number,pin_number,cvv_number,issue_date,expiry_date,card_status)

        try:
            cur_obj.execute(sql2, data2)
            print("========================")
            print("CARD REQUIREMENT:YES")
            print("CARD NUMBER:", card_new_number)
            print("PIN NUMBER:", pin_number)
            print("CVV NUMBER:", cvv_number)
            print("ISSUE DATE:", issue_date)
            print("EXPIRY DATE:", expiry_date)
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()

        #Call send mail function for mail customer for sending details
        message=(f"NAME:{Cust_name}\nACCOUNT NUMBER:{Accno}\n===INTERNET BANKING===\nUSERNAME:{log_id}\nPASSWORD:{log_password}\n===CARD DETAILS===\nCARD NUMBER:{card_new_number}\nPIN NUMBER:{pin_number}\nCVV PIN:{cvv_number}\nEXPIRY DATE:{expiry_date}\n===UPI DETAILS===\nUPI ID1:{mail_upi}\nUPI ID2:{mob_upi}\nKindly Activate your upi id")
        customer_mail.send_mail(mail,Cust_name,message)

    else:
        print("CARD REQUIREMENT:NO")



    conn_obj.close()
