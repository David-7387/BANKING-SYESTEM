from create import insert
from read import read
from update import update
from delete import delete

obj = insert()
objread=read()
objupdate=update()
objdelete=delete()

print("------------Bank Management Syestem---------------")
print("For inserting the data press 1 : ")
print("For Reading the data press 2 : ")
print("For Updating the data press 3 : ")
print("For Deleting the data press 4 : ")

opr=int(input("Please enter your operation:"))

def myopr():
    print("------For Personal information press 1 ----")
    print("------For Bank details press 2 ----")
    print("------For Transaction details press 3 ----")
    print("------For Account Details press 4-----")
    vr=int(input("Please Select your table :"))
    if vr ==1:
        return 'personal_details'
    elif vr ==2:
        return 'bank_details'
    elif vr ==3:
        return 'transaction_details'
    elif vr ==4:
        return 'account_details'
    
if opr ==1:
    h=myopr() # h == account details
    if h=='personal_details':
        cid = int(input("please enter customer id:"))
        fname = input("please enter customer first name:")
        lname = input("please enter customer last name:")
        addr = input("please eneter customer address:")
        pn = int(input("please enter customer phone number:"))
        an = input("please enter customer aadhar number:")
        pan = input("please enter customer pan number:")
        obj.personal_details(cid,fname,lname,addr,pn,an,pan)

    elif h =="bank_details":
        acn = int(input("please enter account number:"))
        cid = int(input("please enter customerid:"))
        ifsc = input("please enter ifsc code:")
        actype = input("please enter account type:")
        obj.bank_details(acn,cid,ifsc,actype)

    elif h =="transaction_details":
        tid = int(input("please enter transaction id:"))
        sac = int(input("please enter sender account number:"))
        rac = int(input("please enter receiver account number:"))
        am = int(input("please enter amount:"))
        mtd=input("please select the method")
        obj.transaction_details(tid,sac,rac,am,mtd)

    elif h =="account_details":
        acn = int(input("please enter account number:"))
        tid = int(input("please enter transactionid:"))
        am = int(input("please enter amount:"))
        cb = int(input("please enter closing balance:"))
        obj.account_details(acn,tid,am,cb)

if opr==2:
    j=myopr()
    cusid=int(input("please enter customer id for fetching data"))
    objread.specific_info(cusid,j)
    
if opr ==3:
    j = myopr()
    cusid = int(input("please enter customer id for fetching data"))
    colname = input("please enter column name:")
    newval = input("please enter new values:") # 500 str # 'jhon'
    objupdate.myupdate(j,colname,newval,cusid)
if opr ==4:
    k=myopr()
    cusid=int(input("please enter customer id to delete the data:"))
    objdelete.specific_del(k,cusid)





