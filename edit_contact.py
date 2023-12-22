#import modules
from tkinter import *
import gui
from database import db_connect
import contact_list
#render contact add form
def form():
 gui.load()
 Label(gui.container, text="Edit Contact") \
 .grid(row=0, column=0, padx=65, pady=5, sticky=W, columnspan=3)
 Label(gui.container, text="Name") \
 .grid(row=1, column=0,padx=10,pady=5, sticky=W, columnspan=3)
 # create a hidden entry field to store the ID of each contactlist entry
 Entry(gui.container, text=gui.text_id, width=0) \
 .grid(row=1, column=1, columnspan=3)
 # put the name entry field on top of the ID field
 Entry(gui.container, text=gui.text_name, width=30) \
 .grid(row=2, column=0, padx=10, pady=2, columnspan=3)
 Label(gui.container, text="e-mail") \
 .grid(row=3, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the email entry field
 Entry(gui.container, text=gui.text_email, width=30) \
 .grid(row=4, column=0, padx=10, pady=2, columnspan=3)
 Label(gui.container, text="Phone") \
 .grid(row=5, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the phone entry field
 Entry(gui.container, text=gui.text_phone, width=30) \
 .grid(row=6, column=0, padx=10, pady=2, columnspan=3)
 Label(gui.container, text="Address") \
 .grid(row=7, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the address entry field
 Entry(gui.container, text=gui.text_address, width=30) \
 .grid(row=8, column=0, padx=10, pady=2, columnspan=3)
 # button for CLOSE form and grid it to the action_frame
 btn_back = Button(gui.action_frame, text="Back", command=lambda: close(), relief=GROOVE,
 bg='#dcdcdc')
 btn_back.grid(row=0, column=0, pady=10, padx=10)
 # button for EDIT contact and grid it to the action_frame
 btn_save = Button(gui.action_frame, text="Save", command=lambda: save(), relief=GROOVE,
 bg='#dcdcdc')
 btn_save.grid(row=0, column=1, pady=10, padx=45)
 # button for CANCEL editing grid it to the action_frame
 btn_cancel = Button(gui.action_frame, text="Cancel", command=lambda: clear(), relief=GROOVE,bg='#dcdcdc')
 btn_cancel.grid(row=0, column=2, pady=10, padx=10)
#save() of save button
def save():
 # return if first name or last name empty
 if gui.text_name.get() == "" :
   return
 # put input fields into tuple
 insert_row = (gui.text_name.get(), gui.text_email.get(),
 gui.text_phone.get(), gui.text_address.get(), gui.text_id.get())
 conn = db_connect()
 with conn:
    cur = conn.cursor()
 sql_query = "UPDATE tbl_contactlist SET name=?, email=?, phone=?, address=?"\
 "WHERE id=?"
 cur.execute(sql_query, insert_row)
 conn.commit()
 conn.close()
 gui.clear_frames()
 contact_list.show()
#cancel() of reset button
def clear():
 for field in gui.contact_fields:
    field.set('')
 gui.clear_frames()
 contact_list.show()
#close() of back nutton
def close():
 gui.clear_frames()
 contact_list.show()