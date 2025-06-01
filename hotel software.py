from sqlite3 import *
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from datetime import *

#Db and table created.
#used function just to check db and table exists
def set_up():  
    con=None
    try:
        con=connect("UdipiExpress.db")
        sql='create table if not exists Menu(sr_no real, name text, price real)'
        sql1='create table if not exists orders(inv_no real, platform text, qty real, item text, price real, total real, table_no real)'
        cursor=con.cursor()
        cursor.execute(sql)
        cursor.execute(sql1)
        con.commit()
    except Exception as e:
        print("issue",e)
        con.rollback()
    finally:                      
        if con is not None:
          con.close
set_up()
 
"""inseted value in menu table.
Uncomment when new item to be added in Menu table"""

# con=None
# try:
#         con=connect("UdipiExpress.db")
#         sql='insert into Menu values(?,?,?)'
#         sr_no=int(input("Enter Sr.no: "))
#         name=input("Enter Item Name: ")
#         price=float(input("Enter price: "))
#         cursor=con.cursor()
#         cursor.execute(sql,(sr_no,name,price))
#         con.commit()
# except Exception as e:
#         print("issue",e)
#         con.rollback()
# finally:
#     if con is not None:
#         con.close

#Functions

#Function to get data from menu table to Item ComboBox

def item_combobox():
    con=None
    try:
        con=connect("UdipiExpress.db")
        sql='SELECT name FROM Menu'
        cursor=con.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
        return [row[0] for row in data]  #pull data from menu table.
    except Exception as e:
        print("issue",e)
        con.rollback()
    finally:                      
        if con is not None:
            con.close

food=item_combobox()

#GUI Design
root=Tk()
root.geometry("1000x800")
root.title("Bill Generator")
root.configure(bg="#F8D395")
root.resizable(False,False)
 
 #Logo
image= Image.open(r"C:\Users\Jay\Desktop\Hotel Bill generator + DB\Udupi Express Logo_2.png")
resized_image = image.resize((300, 150))
photo = ImageTk.PhotoImage(resized_image)
image_label=Label(root,image=photo)
image_label.pack(pady=10)

#Font's
f=("Cambria",16)

dt=datetime.now()
d=(dt.strftime("%x"))
t=(dt.strftime("%X"))

#Date & Time
date_label=Label(root,text=d,font=f,bg="#F8D395",fg="#1F2916")
date_label.place(x=850,y=50)
time_label=Label(root,text=t,font=f,bg="#F8D395",fg="#1F2916")
time_label.place(x=850,y=80)

#Combobox List
table_no=[1,2,3,4,5,6,7,8,9,10]
server_no=[1000,2000,3000,4000]
platform=["Dine-in","Take away","Swiggy","Zomato","Other"]

#ComboBox Place
table_no_cb=ttk.Combobox(root,values=table_no,font=f)
table_no_cb.set("Select Table No.")
table_no_cb.place(x=100,y=300)

server_no_cb=ttk.Combobox(root,values=server_no,font=f)
server_no_cb.set("Select Server No.")
server_no_cb.place(x=400,y=300)

platform_cb=ttk.Combobox(root,values=platform,font=f)
platform_cb.set("Select Option")
platform_cb.place(x=400,y=400)

item_cb=ttk.Combobox(root,values=food,font=f)
item_cb.set("Select Option")
item_cb.place(x=100,y=400)

#ComboBox Label
table_label=Label(root,text="Table",font=f,bg="#F8D395",fg="#1F2916")
table_label.place(x=100,y=250)

server_label=Label(root,text="Server",font=f,bg="#F8D395",fg="#1F2916")
server_label.place(x=400,y=250)

platform_label=Label(root,text="Platform",font=f,bg="#F8D395",fg="#1F2916")
platform_label.place(x=400,y=350)

item_label=Label(root,text="Item",font=f,bg="#F8D395",fg="#1F2916")
item_label.place(x=100,y=350)

root.mainloop()