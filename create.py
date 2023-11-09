import mysql.connector

# creating.connection
class insert:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Bdavidraj@123",
                database="bank"
        )
    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print("-----------------personal details succesfully saved------------------- :")

    def bank_details(self,acn,cid,ifsc,actype):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("----------Bank details has been succesfully saved--------:")

    
    def transaction_details(self,tid,sac,rac,am,mtd):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({tid},{sac},{rac},{am},'{mtd}')")
        self.conn.commit()
        print("----------Transaction details has been succesfully saved--------:")

    
    def account_details(self,acn,tid,am,cb):
        cur=self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({acn},{tid},{am},{cb})")
        self.conn.commit()
        print("----------Account details has been succesfully saved--------:")
    




