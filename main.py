import tkinter as tk
from tkinter import *
import mysql.connector

root = tk.Tk()
root.title("FOOD DELIVERY DATABASE MANAGEMENT")
root.geometry("478x510")
root.resizable("FALSE","FALSE")
root.configure(bg='#add8e6')

header = Label(root,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
header.grid(row=0,column=0,columnspan=3,pady=15)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmay#1805",
    database="dbms_project",
    auth_plugin="caching_sha2_password"
)
print(mydb)
c = mydb.cursor()
#c.execute("SELECT * FROM customer")
#for x in c.description:
#    print(x)

'''
Creating function for showing the tables
'''

def show_customer():
    root2 = tk.Tk()
    root2.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root2.geometry("500x510")
    root2.resizable("FALSE","FALSE")
    root2.configure(bg='#add8e6')

    header = Label(root2,text="CUSTOMER TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=7,pady=15)
    
    c.execute("SELECT * FROM customer")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root2,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root2.mainloop()
    return

def show_employee():
    root3 = tk.Tk()
    root3.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root3.geometry("478x510")
    root3.resizable("FALSE","FALSE")
    root3.configure(bg='#add8e6')

    header = Label(root3,text="EMPLOYEE TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=7,pady=15)
    
    c.execute("SELECT * FROM employee")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root3,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root3.mainloop()
    return

def show_chef():
    root4 = tk.Tk()
    root4.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root4.geometry("478x510")
    root4.resizable("FALSE","FALSE")
    root4.configure(bg='#add8e6')

    header = Label(root4,text="CHEF TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,pady=15)
    
    c.execute("SELECT * FROM chef")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root4,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root4.mainloop()
    return

def show_food():
    root5 = tk.Tk()
    root5.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root5.geometry("478x510")
    root5.resizable("FALSE","FALSE")
    root5.configure(bg='#add8e6')

    header = Label(root5,text="FOOD TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=3,pady=15)
    
    c.execute("SELECT * FROM food")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root5,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root5.mainloop()
    return

def show_delivery():
    root6 = tk.Tk()
    root6.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root6.geometry("478x510")
    root6.resizable("FALSE","FALSE")
    root6.configure(bg='#add8e6')

    header = Label(root6,text="DELIVERY TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=8,pady=15)
    
    c.execute("SELECT * FROM delivery")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root6,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root6.mainloop()
    return

def show_order():
    root7 = tk.Tk()
    root7.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root7.geometry("478x510")
    root7.resizable("FALSE","FALSE")
    root7.configure(bg='#add8e6')

    header = Label(root7,text="ORDER TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=3,pady=15)
    
    c.execute("SELECT * FROM orders")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root7,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root7.mainloop()
    return

def show_payment():
    root8 = tk.Tk()
    root8.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root8.geometry("478x510")
    root8.resizable("FALSE","FALSE")
    root8.configure(bg='#add8e6')

    header = Label(root8,text="PAYMENT TABLE",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=4,pady=15)
    
    c.execute("SELECT * FROM payment")
    result = c.fetchall()

    for index , x in enumerate(result):
        num = 0
        for y in x:
            lookup_label = Label(root8,text=y, fg="black",bg="white",padx=5,pady=5)
            lookup_label.grid(row=index+1,column=num,padx=5,pady=5)
            num+=1

    root8.mainloop()
    return


'''
Creating function for editing the tables
'''

def edit_customer():
    root9 = tk.Tk()
    root9.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root9.geometry("478x510")
    root9.resizable("FALSE","FALSE")
    root9.configure(bg='#add8e6')


    '''
    ADD TO SQL DATABASE
    '''

    def add_customer_entry():

        custid_label = Label(root9,text="Customer ID",fg="black")
        custid_label.grid(row=2,column=0,padx=5,pady=5)
        custid_label_entry = Entry(root9)
        custid_label_entry.grid(row=2,column=1)
        
        name_label = Label(root9,text="Customer Name",fg="black")
        name_label.grid(row=3,column=0,padx=5,pady=5)
        name_label_entry = Entry(root9)
        name_label_entry.grid(row=3,column=1)

        email_label = Label(root9,text="Customer e-mail",fg="black")
        email_label.grid(row=4,column=0,padx=5,pady=5)
        email_label_entry = Entry(root9)
        email_label_entry.grid(row=4,column=1)

        address_label = Label(root9,text="Customer address",fg="black")
        address_label.grid(row=5,column=0,padx=5,pady=5)
        address_label_entry = Entry(root9)
        address_label_entry.grid(row=5,column=1)

        pincode_label = Label(root9,text="Customer pincode",fg="black")
        pincode_label.grid(row=6,column=0,padx=5,pady=5)
        pincode_label_entry = Entry(root9)
        pincode_label_entry.grid(row=6,column=1)

        gender_label = Label(root9,text="Customer Gender",fg="black")
        gender_label.grid(row=7,column=0,padx=5,pady=5)
        gender_label_entry = Entry(root9)
        gender_label_entry.grid(row=7,column=1)

        phoneno_label = Label(root9,text="Customer Phone Number",fg="black")
        phoneno_label.grid(row=8,column=0,padx=5,pady=5)
        phoneno_label_entry = Entry(root9)
        phoneno_label_entry.grid(row=8,column=1)


        def addit():
            
            sql_command="INSERT INTO customer(custid,name,email,address,pincode,gender,phoneno) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values=(custid_label_entry.get(),name_label_entry.get(),email_label_entry.get(),address_label_entry.get(),pincode_label_entry.get(),gender_label_entry.get(),phoneno_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root9,text="Record Added!!")
            text.grid(row=12,column=0)

            custid_label.grid_forget()
            custid_label_entry.grid_forget()
            
            name_label.grid_forget()
            name_label_entry.grid_forget()

            email_label.grid_forget()
            email_label_entry.grid_forget()

            address_label.grid_forget()
            address_label_entry.grid_forget()

            pincode_label.grid_forget()
            pincode_label_entry.grid_forget()

            gender_label.grid_forget()
            gender_label_entry.grid_forget()

            phoneno_label.grid_forget()
            phoneno_label_entry.grid_forget() 

            add_details.grid_forget()

            return

        


        add_details = Button(root9,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=9,column=0)
        
        return

    def delete_customer_entry():

        deleteid_label = Label(root9,text="Customer ID to be deleted")
        deleteid_entry = Entry(root9)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM customer WHERE custid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root9,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root9,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return



    header = Label(root9,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root9,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_customer_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root9,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_customer_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)

    root9.mainloop()
    return

def edit_employee():
    root10 = tk.Tk()
    root10.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root10.geometry("478x510")
    root10.resizable("FALSE","FALSE")
    root10.configure(bg='#add8e6')

    '''
    ADD TO SQL DATABASE
    '''

    def add_employee_entry():

        empid_label = Label(root10,text="Employee ID",fg="black")
        empid_label.grid(row=2,column=0,padx=5,pady=5)
        empid_label_entry = Entry(root10)
        empid_label_entry.grid(row=2,column=1)
        
        name_label = Label(root10,text="Employee Name",fg="black")
        name_label.grid(row=3,column=0,padx=5,pady=5)
        name_label_entry = Entry(root10)
        name_label_entry.grid(row=3,column=1)

        dob_label = Label(root10,text="Employee Date of Birth",fg="black")
        dob_label.grid(row=4,column=0,padx=5,pady=5)
        dob_label_entry = Entry(root10)
        dob_label_entry.grid(row=4,column=1)

        address_label = Label(root10,text="Employee address",fg="black")
        address_label.grid(row=5,column=0,padx=5,pady=5)
        address_label_entry = Entry(root10)
        address_label_entry.grid(row=5,column=1)
    
        gender_label = Label(root10,text="Employee Gender",fg="black")
        gender_label.grid(row=7,column=0,padx=5,pady=5)
        gender_label_entry = Entry(root10)
        gender_label_entry.grid(row=7,column=1)

        phoneno_label = Label(root10,text="Employee Phone Number",fg="black")
        phoneno_label.grid(row=8,column=0,padx=5,pady=5)
        phoneno_label_entry = Entry(root10)
        phoneno_label_entry.grid(row=8,column=1)

        salary_label = Label(root10,text="Employee Salary",fg="black")
        salary_label.grid(row=9,column=0,padx=5,pady=5)
        salary_label_entry = Entry(root10)
        salary_label_entry.grid(row=9,column=1)

        def addit():
            sql_command="INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s)"
            values=(empid_label_entry.get(),name_label_entry.get(),dob_label_entry.get(),address_label_entry.get(),gender_label_entry.get(),phoneno_label_entry.get(),salary_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root10,text="Record Added!!")
            text.grid(row=12,column=0)

            empid_label.grid_forget()
            empid_label_entry.grid_forget()
            
            name_label.grid_forget()
            name_label_entry.grid_forget()

            dob_label.grid_forget()
            dob_label_entry.grid_forget()

            address_label.grid_forget()
            address_label_entry.grid_forget()

            gender_label.grid_forget()
            gender_label_entry.grid_forget()

            phoneno_label.grid_forget()
            phoneno_label_entry.grid_forget()

            salary_label.grid_forget()
            salary_label_entry.grid_forget() 

            add_details.grid_forget()
            return

        add_details = Button(root10,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=10,column=0)
        
        return

    
    def delete_employee_entry():

        deleteid_label = Label(root10,text="Employee ID to be deleted")
        deleteid_entry = Entry(root10)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM employee WHERE empid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root10,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root10,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root10,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root10,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_employee_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root10,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_employee_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)
    root10.mainloop()
    return

def edit_chef():
    root11 = tk.Tk()
    root11.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root11.geometry("478x510")
    root11.resizable("FALSE","FALSE")
    root11.configure(bg='#add8e6')



    '''
    ADD TO SQL DATABASE
    '''

    def add_chef_entry():

        chefid_label = Label(root11,text="Chef ID",fg="black")
        chefid_label.grid(row=2,column=0,padx=5,pady=5)
        chefid_label_entry = Entry(root11)
        chefid_label_entry.grid(row=2,column=1)

        cheffoodid_label = Label(root11,text="Food ID",fg="black")
        cheffoodid_label.grid(row=8,column=0,padx=5,pady=5)
        cheffoodid_label_entry = Entry(root11)
        cheffoodid_label_entry.grid(row=8,column=1)

        def addit():
            sql_command="INSERT INTO chef VALUES(%s,%s)"
            values=(chefid_label_entry.get(),cheffoodid_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root11,text="Record Added!!")
            text.grid(row=12,column=0)

            chefid_label.grid_forget()
            chefid_label_entry.grid_forget()
            
            cheffoodid_label.grid_forget()
            cheffoodid_label_entry.grid_forget() 

            add_details.grid_forget()
            return

        add_details = Button(root11,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=9,column=0)
        
        return

    
    def delete_chef_entry():

        deleteid_label = Label(root11,text="Chef ID to be deleted")
        deleteid_entry = Entry(root11)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM chef WHERE empid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root11,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root11,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root11,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root11,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_chef_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root11,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_chef_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)
    root11.mainloop()
    return

def edit_food():
    root12 = tk.Tk()
    root12.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root12.geometry("478x510")
    root12.resizable("FALSE","FALSE")
    root12.configure(bg='#add8e6')

    '''
    ADD TO SQL DATABASE
    '''

    def add_food_entry():

        foodid_label = Label(root12,text="Food ID",fg="black")
        foodid_label.grid(row=2,column=0,padx=5,pady=5)
        foodid_label_entry = Entry(root12)
        foodid_label_entry.grid(row=2,column=1)

        foodname_label = Label(root12,text="Food Name",fg="black")
        foodname_label.grid(row=8,column=0,padx=5,pady=5)
        foodname_label_entry = Entry(root12)
        foodname_label_entry.grid(row=8,column=1)

        price_label = Label(root12,text="Price",fg="black")
        price_label.grid(row=9,column=0,padx=5,pady=5)
        price_label_entry = Entry(root12)
        price_label_entry.grid(row=9,column=1)

        def addit():

            sql_command="INSERT INTO food VALUES(%s,%s,%s)"
            values=(foodid_label_entry.get(),foodname_label_entry.get(),price_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root12,text="Record Added!!")
            text.grid(row=12,column=0)

            foodid_label.grid_forget()
            foodid_label_entry.grid_forget()
            
            foodname_label.grid_forget()
            foodname_label_entry.grid_forget() 

            price_label.grid_forget()
            price_label_entry.grid_forget() 

            add_details.grid_forget()
            return

        add_details = Button(root12,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=10,column=0)
        
        return

    
    def delete_food_entry():

        deleteid_label = Label(root12,text="Food ID to be deleted")
        deleteid_entry = Entry(root12)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM food WHERE foodid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root12,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root12,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root12,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root12,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_food_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root12,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_food_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)    
    root12.mainloop()
    return

def edit_delivery():
    root13 = tk.Tk()
    root13.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root13.geometry("478x510")
    root13.resizable("FALSE","FALSE")
    root13.configure(bg='#add8e6')


    '''
    ADD TO SQL DATABASE
    '''

    def add_delivery_entry():

        deliveryid_label = Label(root13,text="Delivery ID",fg="black")
        deliveryid_label.grid(row=2,column=0,padx=5,pady=5)
        deliveryid_label_entry = Entry(root13)
        deliveryid_label_entry.grid(row=2,column=1)
        
        vehicleno_label = Label(root13,text="Vehicle Number",fg="black")
        vehicleno_label.grid(row=3,column=0,padx=5,pady=5)
        vehicleno_label_entry = Entry(root13)
        vehicleno_label_entry.grid(row=3,column=1)

        custid_label = Label(root13,text="Customer ID",fg="black")
        custid_label.grid(row=4,column=0,padx=5,pady=5)
        custid_label_entry = Entry(root13)
        custid_label_entry.grid(row=4,column=1)

        orderid_label = Label(root13,text="Order ID",fg="black")
        orderid_label.grid(row=5,column=0,padx=5,pady=5)
        orderid_label_entry = Entry(root13)
        orderid_label_entry.grid(row=5,column=1)

        deliverycharge_label = Label(root13,text="Delivery Charge",fg="black")
        deliverycharge_label.grid(row=6,column=0,padx=5,pady=5)
        deliverycharge_label_entry = Entry(root13)
        deliverycharge_label_entry.grid(row=6,column=1)

        empid_label = Label(root13,text="Employee id",fg="black")
        empid_label.grid(row=7,column=0,padx=5,pady=5)
        empid_label_entry = Entry(root13)
        empid_label_entry.grid(row=7,column=1)

        deldate_label = Label(root13,text="Delivery date",fg="black")
        deldate_label.grid(row=8,column=0,padx=5,pady=5)
        deldate_label_entry = Entry(root13)
        deldate_label_entry.grid(row=8,column=1)

        deltime_label = Label(root13,text="Delivery Time",fg="black")
        deltime_label.grid(row=9,column=0,padx=5,pady=5)
        deltime_label_entry = Entry(root13)
        deltime_label_entry.grid(row=9,column=1)

        def addit():
            
            sql_command="INSERT INTO delivery VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values=(deliveryid_label_entry.get(),vehicleno_label_entry.get(),custid_label_entry.get(),orderid_label_entry.get(),deliverycharge_label_entry.get(),empid_label_entry.get(),deldate_label_entry.get(),deltime_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root13,text="Record Added!!")
            text.grid(row=12,column=0)


            deliveryid_label.grid_forget()
            deliveryid_label_entry.grid_forget()
            
            vehicleno_label.grid_forget()
            vehicleno_label_entry.grid_forget()

            custid_label.grid_forget()
            custid_label_entry.grid_forget()

            orderid_label.grid_forget()
            orderid_label_entry.grid_forget()

            deliverycharge_label.grid_forget()
            deliverycharge_label_entry.grid_forget()

            empid_label.grid_forget()
            empid_label_entry.grid_forget()

            deldate_label.grid_forget()
            deldate_label_entry.grid_forget()

            deltime_label.grid_forget()
            deltime_label_entry.grid_forget() 

            add_details.grid_forget()
            return

        add_details = Button(root13,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=10,column=0)
        
        return

    
    def delete_delivery_entry():

        deleteid_label = Label(root13,text="Delivery ID to be deleted")
        deleteid_entry = Entry(root13)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM delivery WHERE deliveryid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root13,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root13,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root13,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root13,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_delivery_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root13,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_delivery_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)

    root13.mainloop()
    return

def edit_order():
    root14 = tk.Tk()
    root14.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root14.geometry("478x510")
    root14.resizable("FALSE","FALSE")
    root14.configure(bg='#add8e6')


    '''
    ADD TO SQL DATABASE
    '''

    def add_orders_entry():

        orderid_label = Label(root14,text="Order ID",fg="black")
        orderid_label.grid(row=2,column=0,padx=5,pady=5)
        orderid_label_entry = Entry(root14)
        orderid_label_entry.grid(row=2,column=1)

        totalcost_label = Label(root14,text="Total Cost",fg="black")
        totalcost_label.grid(row=8,column=0,padx=5,pady=5)
        totalcost_label_entry = Entry(root14)
        totalcost_label_entry.grid(row=8,column=1)

        foodid_label = Label(root14,text="Food ID",fg="black")
        foodid_label.grid(row=9,column=0,padx=5,pady=5)
        foodid_label_entry = Entry(root14)
        foodid_label_entry.grid(row=9,column=1)
      
        def addit():

                        
            sql_command="INSERT INTO orders VALUES(%s,%s,%s)"
            values=(orderid_label_entry.get(),totalcost_label_entry.get(),foodid_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root14,text="Record Added!!")
            text.grid(row=12,column=0)

            orderid_label.grid_forget()
            orderid_label_entry.grid_forget()
            
            totalcost_label.grid_forget()
            totalcost_label_entry.grid_forget() 

            foodid_label.grid_forget()
            foodid_label_entry.grid_forget()

            add_details.grid_forget()
            return

        add_details = Button(root14,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=10,column=0)
        
        return

    
    def delete_orders_entry():

        deleteid_label = Label(root14,text="Order ID to be deleted")
        deleteid_entry = Entry(root14)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM orders WHERE order_id = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root14,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root14,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root14,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root14,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_orders_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root14,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_orders_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)

    root14.mainloop()
    return

def edit_payment():
    root15 = tk.Tk()
    root15.title("FOOD DELIVERY DATABASE MANAGEMENT")
    root15.geometry("478x510")
    root15.resizable("FALSE","FALSE")
    root15.configure(bg='#add8e6')

    '''
    ADD TO SQL DATABASE
    '''

    def add_payment_entry():

        paymentid_label = Label(root15,text="Payment ID",fg="black")
        paymentid_label.grid(row=2,column=0,padx=5,pady=5)
        paymentid_label_entry = Entry(root15)
        paymentid_label_entry.grid(row=2,column=1)

        paymentmethod_label = Label(root15,text="Payment Method",fg="black")
        paymentmethod_label.grid(row=8,column=0,padx=5,pady=5)
        paymentmethod_label_entry = Entry(root15)
        paymentmethod_label_entry.grid(row=8,column=1)

        custid_label = Label(root15,text="Customer ID",fg="black")
        custid_label.grid(row=9,column=0,padx=5,pady=5)
        custid_label_entry = Entry(root15)
        custid_label_entry.grid(row=9,column=1)

        orderid_label = Label(root15,text="Order ID",fg="black")
        orderid_label.grid(row=10,column=0,padx=5,pady=5)
        orderid_label_entry = Entry(root15)
        orderid_label_entry.grid(row=10,column=1)
      
        def addit():

            sql_command="INSERT INTO payment VALUES(%s,%s,%s,%s)"
            values=(paymentid_label_entry.get(),paymentmethod_label_entry.get(),custid_label_entry.get(),orderid_label_entry.get())
            c.execute(sql_command,values)

            mydb.commit()

            text = Label(root15,text="Record Added!!")
            text.grid(row=12,column=0)


            paymentid_label.grid_forget()
            paymentid_label_entry.grid_forget()
            
            paymentmethod_label.grid_forget()
            paymentmethod_label_entry.grid_forget() 

            custid_label.grid_forget()
            custid_label_entry.grid_forget()

            orderid_label.grid_forget()
            orderid_label_entry.grid_forget()

            add_details.grid_forget()
            return

        add_details = Button(root15,text="Add Details",bg="white",fg="black",command=addit)
        add_details.grid(row=11,column=0)
        
        return

    
    def delete_payment_entry():

        deleteid_label = Label(root15,text="Payment ID to be deleted")
        deleteid_entry = Entry(root15)
        deleteid_label.grid(row=2,column=0)
        deleteid_entry.grid(row=2,column=1)

        def deleteit():

            sql_command="DELETE FROM payment WHERE paymentid = " + deleteid_entry.get()
            c.execute(sql_command)
            mydb.commit()
            
            text = Label(root15,text="Record Deleted!!")
            text.grid(row=2,column=0)

            deleteid_entry.grid_forget()
            deleteid_label.grid_forget()
            delete_details.grid_forget()
            return
        
        delete_details=Button(root15,text="Delete Record",bg="white",fg="black",command=deleteit)
        delete_details.grid(row=3,column=0)

        return

    header = Label(root15,text="ONLINE FOOD DELIVERY SYSTEM",font=("Algerian"),fg='black',bg='#add8e6')
    header.grid(row=0,column=0,columnspan=2,padx=15,pady=15)


    add_button = Button(root15,text ="Add an entry",padx=10,pady=10,fg="black",bg="white",command=add_payment_entry)
    add_button.grid(row=1,column=0,padx=10,pady=10)

    delete_button = Button(root15,text ="Delete an entry",padx=10,pady=10,fg="black",bg="white",command=delete_payment_entry)
    delete_button.grid(row=1,column=2,padx=10,pady=10)

    root15.mainloop()
    return




'''
Creating buttons to show the tables
'''

show_customer_table = Button(root,text="Show Customer Table",padx=10,pady=10,bg='white',command=show_customer)
show_customer_table.grid(row=1,column=0,padx=10,pady=10)

show_employee_table = Button(root,text="Show Employee Table",padx=10,pady=10,bg='white',command=show_employee)
show_employee_table.grid(row=1,column=1,padx=10,pady=10)

show_chef_table = Button(root,text="Show Chef Table",padx=10,pady=10,bg='white',command=show_chef)
show_chef_table.grid(row=1,column=2,padx=10,pady=10)

show_food_table = Button(root,text="Show Food Table",padx=22,pady=10,bg='white',command=show_food)
show_food_table.grid(row=2,column=0,padx=10,pady=10)

show_delivery_table = Button(root,text="Show Delivery Table",padx=16,pady=10,bg='white',command=show_delivery)
show_delivery_table.grid(row=2,column=1,padx=10,pady=10)

show_order_table = Button(root,text="Show Order Table",padx=8,pady=10,bg='white',command=show_order)
show_order_table.grid(row=2,column=2,padx=10,pady=10)

show_payment_table = Button(root,text="Show Payment Table",padx=14,pady=10,bg='white',command=show_payment)
show_payment_table.grid(row=3,column=1,padx=10,pady=10)


'''
Creating buttons for editing the tables
'''

edit_customer_table = Button(root,text="Edit Customer Table",padx=15,pady=10,bg='white',command=edit_customer)
edit_customer_table.grid(row=4,column=0,padx=10,pady=10)

edit_employee_table = Button(root,text="Edit Employee Table",padx=17,pady=10,bg='white',command=edit_employee)
edit_employee_table.grid(row=4,column=1,padx=10,pady=10)

edit_chef_table = Button(root,text="Edit Chef Table",padx=12,pady=10,bg='white',command=edit_chef)
edit_chef_table.grid(row=4,column=2,padx=10,pady=10)

edit_food_table = Button(root,text="Edit Food Table",padx=26,pady=10,bg='white',command=edit_food)
edit_food_table.grid(row=5,column=0,padx=10,pady=10)

edit_delivery_table = Button(root,text="Edit Delivery Table",padx=20,pady=10,bg='white',command=edit_delivery)
edit_delivery_table.grid(row=5,column=1,padx=10,pady=10)

edit_order_table = Button(root,text="Edit Order Table",padx=10,pady=10,bg='white',command=edit_order)
edit_order_table.grid(row=5,column=2,padx=10,pady=10)

edit_payment_table = Button(root,text="Edit Payment Table",padx=17,pady=10,bg='white',command=edit_payment)
edit_payment_table.grid(row=6,column=1,padx=10,pady=10)

quitit = Button(root,text="Quit",command=root.quit,padx=58,pady=10,bg="white",fg="black")
quitit.grid(row=7,column=1,padx=10,pady=10)

root.mainloop()