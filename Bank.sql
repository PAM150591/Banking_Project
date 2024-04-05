create database Bank_database;
use Bank_database;
show tables;

Create table customer_details
(
Accno	        	int	   	not null primary key Auto_increment,
Cust_name  	varchar(30)	not null,
Cust_address   varchar(300)	not null,
DOB 	        	date 		not null,
Cust_age	 int		not null,
Mob		 int(10)		not null,
Party_id       	varchar(30)	not null,
Acc_Status	char(10)	not null,
Balance 	decimal	not null
)Auto_increment=100000;

Create table transaction
(
Transaction_id	        	int		not null	primary key	Auto_increment,
Accno			int		not null,
Transaction_type	char(10)	not null,
Transaction_mode	char(10)	not null,
Transaction_date	date 		not null,	
Amount		decimal	not null,
Balance		decimal	not null
) Auto_increment=1000;

ALTER TABLE transaction ADD CONSTRAINT FOREIGN KEY(Accno) REFERENCES customer_details(Accno);

Create table cust_party
(
Sl_no		int		not null	primary key	Auto_increment,
Party_id	varchar(30)	not null,
User_Name	varchar(30)	not null,
User_Pass	varchar(100)	not null,
Cust_Status	varchar(10)	not null
) Auto_increment=1;

ALTER TABLE cust_party ADD CONSTRAINT FOREIGN KEY(Party_id) REFERENCES customer_details(Party_id);

CREATE INDEX idx_cust_party_ibfk_2 ON customer_details(Party_id);

Create table employee_details
(
Emp_id		int			not null	primary key	Auto_increment,
Emp_name	varchar(30)	not null,
Designation	varchar(20)	not null,
DOB		date		not null,
Emp_age	int		not null,
Emp_address	varchar(300)	not null,
party_id	varchar(10) 	not null
) Auto_increment=11110000;

Create table emp_party
(
Sl_no		int		not null	primary key	Auto_increment,
Party_id	varchar(30)	not null,
User_Name	varchar(30)	not null,
User_Pass	varchar(100)	not null
) Auto_increment=1;

ALTER TABLE emp_party ADD CONSTRAINT FOREIGN KEY(Party_id) REFERENCES employee_details (Party_id);
CREATE INDEX emp_party_ibfk_2 ON employee_details (Party_id);

DESCRIBE employee_details;
DESCRIBE emp_party;
describe customer_details;
describe cust_party;
describe transaction;
describe atm_details;

select * from employee_details;
select * from emp_party;
select * from customer_details;
select * from cust_party;
select * from transaction;
select * from atm_details;
select * from transaction where Accno=100001;
SELECT * FROM atm_details WHERE card_number =123456789125698;

select User_Name,User_Pass from emp_party where party_id = 'ABC002';

ALTER TABLE emp_party ADD Emp_Status char(10);

select party_id from employee_details where emp_id=11110001;

select User_Name,User_Pass from emp_party where party_id ='ABC002';
SELECT User_Pass FROM emp_party WHERE User_Name ='{User_Name}' AND login_name ='{party_id}';

UPDATE emp_party SET User_Pass = 'abcd@123' WHERE User_Name ='suma@1991' AND Party_id ='ABC003';

SELECT Emp_id,party_id FROM employee_details ORDER BY party_id DESC LIMIT 1;

SELECT Balance FROM customer_details WHERE Accno=100000;

ALTER TABLE transaction ADD Transaction_date DATE NOT NULL DEFAULT (CURRENT_DATE) AFTER Transaction_mode ;

ALTER TABLE transaction ADD Transaction_time TIME NOT NULL DEFAULT (CURRENT_TIME) AFTER Transaction_date ;

ALTER TABLE customer_details ADD card_issue varchar(10) NOT NULL  AFTER Balance ;

select Cust_name,party_id from customer_details where Accno=100001;

DELETE FROM cust_party WHERE Sl_no=4;
DELETE FROM customer_details WHERE Accno=100003;

DELETE  FROM transaction WHERE Accno=100001;

SELECT Balance FROM customer_details WHERE Accno=100004 and Cust_name='RAJDEEP BHADRA';

shoW databases;

SELECT Emp_id FROM employee_details ORDER BY Emp_id DESC LIMIT 1;

create table atm_details
(
sl_no			int		not null	primary key	Auto_increment,
Party_id		varchar(30)	not null,
card_number		int(16)		not null,
card_pin		int(4)		not null,
cvv_number		int(3)		not null,
issue_date		date		not null,
valid_date		date		not null,
status			varchar(10)	not null
) Auto_increment=1;

ALTER TABLE atm_details ADD CONSTRAINT FOREIGN KEY(Party_id) REFERENCES customer_details (Party_id);

select Cust_name,party_id from customer_details where Accno=100014;

SELECT card_number FROM atm_details ORDER BY card_number DESC LIMIT 1;

ALTER TABLE atm_details DROP COLUMN card_number;
ALTER TABLE atm_details DROP COLUMN issue_date;
ALTER TABLE atm_details DROP COLUMN valid_date;

ALTER TABLE atm_details ADD card_number varchar(16) NOT NULL  AFTER Party_id ;
ALTER TABLE atm_details ADD issue_date varchar(7) NOT NULL  AFTER cvv_number ;
ALTER TABLE atm_details ADD valid_date varchar(7) NOT NULL  AFTER issue_date; 

select card_pin,cvv_number from atm_details where Party_id='ABC0000012' and card_number=1000202400000002;

SELECT Transaction_date,Transaction_type,Amount,Balance FROM transaction WHERE Accno =100014 ORDER BY transaction_date DESC LIMIT 5;

select Party_id from customer_details where Accno = 100014;

SELECT COUNT(*) FROM atm_details WHERE Party_id = 'ABC0000012' AND card_pin = 1229;

ALTER TABLE customer_details ADD mail_id varchar(30) NOT NULL  AFTER Mob ;

select party_id from customer_details where Accno=100014;
select card_pin,cvv_number from atm_details where Party_id=(select party_id from customer_details where Accno=100014) and card_number=1000202400000002;
select card_pin,cvv_number from atm_details where Party_id='ABC0000012' and card_number=1000202400000002;


DELETE FROM customer_details WHERE Accno=100009;