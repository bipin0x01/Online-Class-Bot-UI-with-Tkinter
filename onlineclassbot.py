from tkinter import *

window = Tk()  # create a window
window.geometry("850x450")  # Set the window size to 500px X 300px
# set minimum window size value
window.minsize(850, 450)
# set maximum window size value
window.maxsize(850, 450)
window.title("Online Class Bot by Bipin Thapa")  # Application Title


def label(name, row, column, padingx, padingy):
    Label(window, text=name).grid(
        row=row, column=column, padx=padingx, pady=padingy)


def input(width, row, column, colspan, padx, pady):
    Entry(window, width=width, borderwidth=2).grid(
        row=row, column=column, columnspan=colspan, padx=padx, pady=pady)


label('Subject Name', '0', '0', '0', '3')  # Subject Name Label
subject = Entry(window, width=20, borderwidth=2)
subject.grid(row=1, column=0, columnspan=2, padx=10, pady=3)
label('Start Time', '0', '2', '0', '0')  # Start Time Label
Spinbox(window, from_=1, to=12, width=7, wrap=True).grid(row=1, column=2)
label('End Time', '0', '4', '0', '0')  # End Time Label
Spinbox(window, from_=1, to=12, width=7, wrap=True).grid(row=1, column=4)
#Spinbox(window, from_=0, to=59, width=3, wrap=True).grid(row=1, column=5)
#Spinbox(window, from_=0, to=59, width=5).grid(row=1, column=7)
label('Classroom Link', '2', '0', '0', '0')  # Classroom Link Label
input('35', '3', '0', '4', '0', '3')  # Classroom Link Input
label('Credits', '0', '6', '0', '0')

credits = Listbox(window, width=42, height=15)
credits.grid(row=1, column=6, rowspan=5, columnspan=2)
credits.insert(
    1, "This program is made for fun and educational")
credits.insert(
    2, " purpose only. It can be used to automatically")
credits.insert(3, " join the entered class in specified time.")
credits.insert(4, " Instructions")
credits.insert(5, " #Add the subject, class time and class link. It")
credits.insert(
    6, " will only work If the class link is always same")
credits.insert(7, " and doesnot change with time.")
credits.insert(8, " #Click on \"Add Subject\" Button")
credits.insert(9, " Class data will be added to the list.")
credits.insert(10, " #Tick other preffered checkboxes.")
credits.insert(11, " #Then Click on \"Start Bot\" button.")
credits.insert(12, "")
credits.insert(13, "")
credits.insert(14, "       Made for fun with love by Bipin Thapa ❤")


def subjectlist_parser():
    subjectlist = subject.get()
    print(subjectlist)
    subject.clipboard_clear()


Button(window, text="Add Subject", command=subjectlist_parser).grid(
    row=3, column=4)  # Add Subject Button


Checkbutton(window, width=15, text=" Record the sessions.").grid(
    row=6, column=6, columnspan=2)
Checkbutton(window, width=30, text=" Stop bot after completing all sessions.").grid(
    row=7, column=6, columnspan=2)
Button(window, text="Start Bot", width=10).grid(row=8, column=6)
Button(window, text="Stop Bot", width=10).grid(row=8, column=7)

Listbox(window, height=17, width=55).grid(
    row=5, column=0, columnspan=6, rowspan=6, pady=10, padx=10)

window.mainloop()
