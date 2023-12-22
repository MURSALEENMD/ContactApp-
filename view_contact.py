from tkinter import *
import gui
from database import db_connect
import contact_list
import edit_contact
#show a specific contact info
def show():
 gui.load()
 Label(gui.container, text="View Contact") \
 .grid(row=0, column=0, padx=65, pady=5, sticky=W, columnspan=3)
 Label(gui.container, text="Name") \
 .grid(row=1, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # create a hidden entry field to store the ID of each contactlist entry
 Entry(gui.container, text=gui.text_id, width=0) \
 .grid(row=1, column=1, columnspan=3)
 # put the name on top of the ID field
 Label(gui.container, text=gui.text_name.get()) \
 .grid(row=2, column=0, padx=10, pady=2, columnspan=3, sticky=W)
 Label(gui.container, text="e-mail") \
    .grid(row=3, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the email value
 Label(gui.container, text=gui.text_email.get()) \
 .grid(row=4, column=0, padx=10, pady=2, columnspan=3, sticky=W)
 Label(gui.container, text="Phone") \
 .grid(row=5, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the phone value
 Label(gui.container, text=gui.text_phone.get()) \
 .grid(row=6, column=0, padx=10, pady=2, columnspan=3, sticky=W)
 Label(gui.container, text="Address") \
 .grid(row=7, column=0, padx=10, pady=5, sticky=W, columnspan=3)
 # put the address value
 Label(gui.container, text=gui.text_address.get()) \
 .grid(row=8, column=0, padx=10, pady=2, columnspan=3, sticky=W)
 # button for CLOSE form and grid it to the action_frame
 btn_back = Button(gui.action_frame, text="Back", command=lambda: close(), relief=GROOVE,
 bg='#dcdcdc')
 btn_back.grid(row=0, column=0, pady=10, padx=10)
 # button for ADD contact and grid it to the action_frame
 btn_edit = Button(gui.action_frame, text="Edit", command=lambda: edit(), relief=GROOVE,
 bg='#dcdcdc')
 btn_edit.grid(row=0, column=1, pady=10, padx=45)
 # button for RESET form and grid it to the action_frame
 btn_delete = Button(gui.action_frame, text="Delete", command=lambda: delete(),
relief=GROOVE,
 bg='#dcdcdc')
 btn_delete.grid(row=0, column=2, pady=10, padx=10)
# delete() of delete button
def delete():
 # get the value of ID
 contact_id=gui.text_id.get()
 #create a tuple from contact ID
 del_id=(contact_id,)
 conn = db_connect()
 with conn:
    cur = conn.cursor()
 sql_query = "DELETE FROM tbl_contactlist WHERE id=?"
 cur.execute(sql_query, del_id)
 conn.commit()
 conn.close()
 gui.clear_frames()
 contact_list.show()
# edit() of edit button
def edit():
 gui.clear_frames()
 edit_contact.form()
 # close() of back nutton
def close():
 gui.clear_frames()
 contact_list.show()