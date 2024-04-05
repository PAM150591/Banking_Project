import account_statement
import cust_credential_reset
import account_transfer
import functions
import upi_process
import mysql.connector

def operation(from_accno, cust_name,party_id):
    conn_obj=functions.sql_connection()
    cur_obj = conn_obj.cursor()


    print(f"WELCOME {cust_name}")
    while True:
        # print(f"WELCOME {cust_name}")
        print("\n1.ACCOUNT FUND TRANSFER")
        print("2.UPI FUND TRANSFER")
        print("3.STATEMENT")
        print("4.CHANGE PASSWORD")
        print("5.CHANGE USERNAME")
        print("6. Exit\n")

        choice=input("PLEASE SELECT THE OPERATION: ")

        if choice == "1":
            to_accno=input("ENTER THE ACCOUNT NUMBER: ")
            to_username=input("ENTER ACCOUNT HOLDER: ")
            amount=float(input("ENTER THE AMOUNT: "))
            account_transfer.online_transfer(from_accno, to_accno, to_username, amount)
        elif choice == "2":
            print("=======WELCOME TO UPI TRANSFER=======")
            # Retrieve required data from upi table acording to upi id
            query1 = (f"SELECT status FROM upi_details WHERE Party_id ='{party_id}'")

            try:
                cur_obj.execute(query1)
                result1 = cur_obj.fetchone()
                conn_obj.commit()
            except mysql.connector.Error as e:
                print("Error retrieving data from MySQL:", e)
                conn_obj.rollback()

            personal_status = result1[0]
            # print(personal_status)

            if personal_status == "DEACTIVATE":

                print("YOUR UPI ID IS NOT ACTIVATE.KINDLY ACTIVATE UPI ID")

                upi_pin = input("ENTER NEW UPI PIN(FOUR DIGIT): ")
                upi_process.activate(party_id,upi_pin,conn_obj,cur_obj)
            else:
                sender_upi=input("ENTER SENDER UPI ID: ")
                sender_name=upi_process.sender_name(sender_upi,conn_obj,cur_obj)
                print(f"SENDER NAME: {sender_name}")
                choice=input("MAY YOU PROCEED?(YES/NO)")
                if choice=="YES":
                    print("LETS GO")
                elif choice=="NO":
                    pass
                else:
                    print("\nInvalid choice. Please try again.")
        elif choice == "3":
            account_statement.statement(from_accno)
        elif choice == "4":
            new_password=input("ENTER NEW PASSWORD:")
            cust_credential_reset.password_reset(from_accno, new_password)
        elif choice == "5":
            new_username=input("ENTER NEW USERNAME:")
            cust_credential_reset.username_reset(from_accno, new_username)
        elif choice == "6":
            print("\nTHANK YOU FOR USING NETBANKING. SEE YOU AGAIN.")
            break
        else:
            print("\nInvalid choice. Please try again.")

    cur_obj.close()
    conn_obj.close()