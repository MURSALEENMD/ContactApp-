#Main app controller
#import required modules
import database
import contact_list
import gui
#create database if not exists
database.create_db()
#Starting-up app
gui.init()
contact_list.show()
gui.app.mainloop()