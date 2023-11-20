import mysql.connector
mydb=mysql.connector.connect(host='local host',user='root',password='banu@123',database='bms')
def open_account():
    name=input("enter your name:")
    acc=input("enter your account:")
    dob=input("enter your dob:")
    add=input("enter your address:")
    con=input("enter your contact:")
    op_bal=int(input("enter your opening balance:"))
    data1=(name,acc,dob,add,con,op_bal)
    data2=(name,acc,op_bal)
    sql1=('insert into account values(%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("data entered succesfully")
    main()
def deposit():
    amount=input("entered the amount to deposit:")
    acc=input("enter your acc no:")
    a="select balance from amount where acc_no=%s"
    data1=(acc)
    x=mydb.corsor()
    x.execute(a,data1)
    result=x.fetch one()
    t=result[0]+amount
    sql=('update amount set balance where acc_no=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print("_______________________________________")
    main()
def withdraw():
    amount=input("enter the amount to withdraw:")
    acc=input("enter your acc no")
    a="select balance from amount where acc_no=%s"
    data1=(acc1)
    x=mydb.corsor()
    x.execute(a,data1)
    result=x.fetch one()
    t=result[0]-amount
    sql=('update amount set balance where acc_no=%s')
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    print("_______________________________________")
    main()
def balance():
    ac:input("enter the account number:")
    a="select"*"from amount where acc no=%s"
    data=(ac1)
    x=mydb.cursor()
    x.execute(a.data)
    mydb.commit()
    
