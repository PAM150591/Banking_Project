import mysql.connector
import atm_balance
import atm_deposit
import atm_withdraw
import atm_mini_statement
import atm_pin_change


def atm_access(accno,atm_card,atm_pin,atm_cvv):
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    cur_obj = conn_obj.cursor()

    #select party_id from employee_details where emp_id=11110001;
    query1 = (f"select Cust_name,party_id from customer_details where Accno={accno}")

    try:
        cur_obj.execute(query1)
        result1 = cur_obj.fetchone()
        conn_obj.commit()
    except mysql.connector.Error as e:
        print("Error retrieving data from MySQL:", e)
        conn_obj.rollback()

    # Handle cases based on the presence of a account number
    if result1:
        customer_name=result1[0]
        party=result1[1]


        # select pin number and cvv number from atm_details using given card number;
        query2 = (f"select card_pin,cvv_number from atm_details where Party_id='{party}' and card_number={atm_card}")

        try:
            cur_obj.execute(query2)
            result2 = cur_obj.fetchone()
            conn_obj.commit()
        except mysql.connector.Error as e:
            print("Error retrieving data from MySQL:", e)
            conn_obj.rollback()

        # Handle cases based on the presence of a account number
        if result2:
            pin_number = result2[0]
            cvv_number = result2[1]


            if pin_number==atm_pin and cvv_number==atm_cvv:
                while True:
                    print(f"\n-{customer_name}-")
                    print("\nATM Options:")
                    print("1. Balance Inquiry")
                    print("2. Withdraw Cash")
                    print("3. Deposit Cash")
                    print("4. MINI STATEMENT")
                    print("5. Change PIN")  # Added option for PIN change
                    print("6. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        # Simulate balance inquiry (replace with actual balance retrieval)
                        atm_balance.atm_balance(accno)
                    elif choice == "2":
                        amount=float(input("ENTER AMOUNT:"))
                        atm_withdraw.atm_withdraw(accno,amount)
                    elif choice == "3":
                        amount=float(input("ENTER AMOUNT:"))
                        atm_deposit.atm_deposit(accno,amount)
                    elif choice == "4":
                        atm_mini_statement.atm_statement(accno)
                    elif choice == "5":
                        atm_pin_change.atm_pin(accno,atm_pin)
                    elif choice == "6":
                        print("\nThank you for using our ATM.")
                        break
                    else:
                        print("\nInvalid choice. Please try again.")
            else:
                print("INCORRECT PIN. KINDLY TRY AGAIN")
        else:
            print("KINDLY INSERT CARD PROPERLY")

    else:
        print("KINDLY INSERT CARD PROPERLY")


    cur_obj.close()
    conn_obj.close()
