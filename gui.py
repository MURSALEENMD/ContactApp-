 #import module
from msilib.schema import Icon
from operator import iconcat
from tkinter import *
#loading gui
def load():
 # create an outer frame with padding around window to put all other content
 global container, action_frame
 container = Frame(app)
 container.grid(row=0, column=0, padx=0, rowspan=10, pady=10)
 # establish and grid a frame for action buttons NEW, EDIT, DELETE, CLEAR
 action_frame = Frame(app)
 action_frame.grid(row=10, column=0, padx=0, sticky=EW)
#clear frames
def clear_frames():
 container.destroy()
 action_frame.destroy()
#Intialize application at start-up
def init():
    global app
    app = Tk()
 #define font
    app.option_add("*font", "Helvetica 10")
 #Fixed window
    app.resizable(height=False, width=False)
 #define window height and width
    app.geometry('{0}x{1}'.format(300, 375))
 #define window title
    app.title("Contact Book")
 # define tkinter string vars for form fields
    global text_id, text_name, text_email, text_phone, text_address
    text_id = StringVar()
    text_name = StringVar()
    text_email = StringVar()
    text_phone = StringVar()
    text_address = StringVar()
    #define icon
    app.iconbitmap(app, default ="assets/contact_list.ico")
 # create list for form fields and put variables in list
    global contact_fields
    contact_fields = [text_id, text_name, text_email, text_phone, text_address]
    