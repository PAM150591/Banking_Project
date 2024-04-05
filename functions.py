"""Function.py"""

"""
All sub function are coding here
"""
#Import required module
import random
import string
import bcrypt
import mysql.connector

def sql_connection():
    conn_obj = mysql.connector.connect(
        host="localhost",
        port=3308, user="root",
        password="abcd@123",
        auth_plugin="mysql_native_password",
        database="bank_database")
    # cur_obj = conn_obj.cursor()
    return conn_obj

#Fuction to create employee loging id

def create_login_id(emp_name,date_of_birth):
    """Creates a login ID in the format of 1st 4 characters of name@year of birth, extracting the year from a YYYY-MM-DD date."""

    name=emp_name.lower() # Convert to lowercase for consistency

    # Extract year of birth from date_of_birth
    year_of_birth = date_of_birth[:4]

    first_four_chars = name[:4]  # Extract the first 4 characters

    login_id = first_four_chars + "@" + year_of_birth
    return login_id

#Function to create employee loging password
def create_password():
    characters = string.ascii_letters + string.digits  # combining letters and digits
    password = ''.join(random.choice(characters) for i in range(8))  # generating an 8-character password  for i in range(8))
    return password

def party_id_count(last_party_id):
    # Extract the numeric part of the last party id
    numeric_part = int(last_party_id[3:])

    # Calculate the next party id
    employee_party_id = f"ABC{numeric_part + 1:03d}"  # Ensure 3-digit format 03d

    return employee_party_id

def encrypt_password(log_password):
    # Encrypt password using bcrypt
    hashed_password = bcrypt.hashpw(log_password.encode('utf-8'), bcrypt.gensalt())
    encrypted_password=hashed_password.decode('utf-8')
    return encrypted_password


def cust_party_count(last_party_id):
    # Extract the numeric part of the last party id
    numeric_part = int(last_party_id[3:])

    # Calculate the next party id
    cust_party_id = f"ABC{numeric_part + 1:07d}"  # Ensure 7-digit format 07d

    return cust_party_id

def cust_login_id(Cust_name,DOB):
    """Creates a login ID in the format of 1st 4 characters of name@year of birth, extracting the year from a YYYY-MM-DD date."""

    name=Cust_name.lower() # Convert to lowercase for consistency

    # Extract year of birth from date_of_birth
    year_of_birth = DOB[:4]

    first_four_chars = name[:4]  # Extract the first 4 characters

    login_id = first_four_chars + "_" + year_of_birth
    return login_id

def generate_atm_pin():
    # Generate a random 4-digit ATM PIN
    pin = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    return pin

def generate_cvv_number():
    # Generate a random 3-digit CVV number
    cvv = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    return cvv

def generate_card_number(card_number):
    # Extract the numeric part of the last party id 
    numeric_part = int(card_number[10:])
    new_card_number=f"1000202400{numeric_part + 1:06d}"
    return new_card_number

def mail_upi_generate(email):
    # Check if the email contains '@'
    if '@' in email:
        # Split the email address at '@' and get the prefix
        prefix = email.split('@')[0]
        mail_upi = prefix + "@okabc"
        return mail_upi
    else:
        # If there is no '@' in the email, return an error message
        return "Invalid email address. Please include '@' in the email."

# datetime.datetime.now()
# now=datetime.datetime.now()