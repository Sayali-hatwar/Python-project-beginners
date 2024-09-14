from tkinter import *
from tkcalendar import *

# Window application
root = Tk()

# Setting title and dimensions
root.title('Calendar')
root.geometry('600x600')

# Setting calendar
cal = Calendar(root,year=2024,month=9, day = 13)

# pack the calendar widget
cal.pack(pady=50)   # shows padding of calendar at y axis

# run the application
root.mainloop()