#import modules
from tkinter import *
from database import db_connect
import gui
import add_contact
import view_contact
#load contact list
con_list=[]
def load_contactlist():
 # clear contact list
 con_list.clear()
 conn = db_connect()
 with conn:
    cur = conn.cursor()
 query = "SELECT ID, name FROM tbl_contactlist ORDER BY LOWER(name) ASC"
 cur.execute(query)
 rows = cur.fetchall()
 conn.close()
 for row in rows:
 # put each ID and name into tuple and add to list
    con_list.append((row[0], row[1]))
#render contact list
def show():
    #load gui
 gui.load()
 # add contactlist Listbox with scroll bar
 sb = Scrollbar(gui.container , orient=VERTICAL)
 global contactlist_box
 contactlist_box = Listbox(gui.container, exportselection=0, yscrollcommand=sb.set, width=28,
 selectmode=SINGLE)
 contactlist_box.bind('<<ListboxSelect>>', lambda event: select_entry())
 sb.config(command=contactlist_box.yview)
 contactlist_box.grid(row=1, column=0, rowspan=9, padx=(10, 0), sticky=NSEW)
 sb.grid(row=1, column=1, rowspan=9, sticky=N + S + E)
 #loading contacts into list box
 load_contactlist()
 if len(con_list)>0:
 # put name list into listbox
    for rec in con_list:
     i=rec[0]
    name=rec[1]
    contactlist_box.insert(i, name)
 else:
    #No entry
   contactlist_box.insert(0, 'No Contacts')
 # button for ADD contact and grid it to the action_frame
 btn_add_person = Button(gui.action_frame, text="Add New Contact", command=lambda:
add_person(), relief=GROOVE, bg='#dcdcdc')
 btn_add_person.pack(side=RIGHT, pady=20)
#selection event function for list box
def select_entry():
 curr_rec=contactlist_box.curselection()
 index = curr_rec[0]
 #fetching the selected record from table
 query_id = (con_list[index][0],)
 conn = db_connect()
 with conn:
    cur = conn.cursor()
 sql_query = "SELECT * FROM tbl_contactlist WHERE ID = ?"
 cur.execute(sql_query, query_id)
 entry = cur.fetchone()
 conn.close()
 for i in range(len(gui.contact_fields)):
   gui.contact_fields[i].set(entry[i])
 gui.clear_frames()
 view_contact.show()
#click eventon function for Add New Contact button
def add_person():
 gui.clear_frames()
 add_contact.form()