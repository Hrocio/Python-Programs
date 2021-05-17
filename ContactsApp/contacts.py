from tkinter import *
from tkinter import filedialog
import tkinter.messagebox


def dialog(opti):
    '''Here the "about" information is included'''
    if opti == 1:
        tkinter.messagebox.showinfo("Welcome to Contact App\n",
                                "\nContacts ""App."" \nDeveloped by Hilda Martin \nFor CSE107 2019")
# Menu functions


def saving():
    '''Here is where the "saving as" option goes. root title'''
    global ArchiveJobs, Table
    if ArchiveJobs == "":
        save_as(2)
        root.title("Application to manage the firm’s contacts. " + ArchiveJobs)
    scribe()


def formating():
    '''This formats content.It is in the "Archive" menu'''
    global ArchiveJobs, Table
    if ArchiveJobs != "":
        file = archive_in_usage("r")
        content = file.read()
    if ArchiveJobs != "" and content != "":
        action = tkinter.messagebox.askyesno("Warning\n", "\nDelete contact?")
        if action == True:
            delete_content()
            cleaning(1)
    else:
        tkinter.messagebox.showinfo("Warning\n", "\nEmpty File")


def exiting():
    '''This will exit the program and display a goodbye message
    it is in the "Archive" menu
    '''
    global root
    action = tkinter.messagebox.askyesno("Warning\n",
                                   "\n Any unsaved changes will be lost. Goodbye")
    if action == True:
        root.destroy()


def archive_in_usage(permissions):
    '''Archiving and control it returns the function'''
    global ArchiveJobs
    archive_in_usage = open(ArchiveJobs, permissions)
    return archive_in_usage


def reading():
    '''Here is where the boxes to add name, email or phone number goes
    0 name, 1 email, 2 phone
    '''
    global Table
    Table.delete("1.0", END)
    file = archive_in_usage("r")
    content = file.read()
    var_temp = ["", "", "", "", ""]
    control = 0  # 0 name, 1 email, 2 phone
    for i in range(len(content)-1):

        if content[i] == "," and content[i+1] == "":
            control = control+1
        elif content[i] == "\n":
            control = 0
            Table.insert(INSERT, "\t\t" + str(var_temp[0]) +
                         "\t\t\t\t\t" + str(var_temp[1]) + "\t\t\t\t\t" + str(
                                                         var_temp[2]) + " \n")
            var_temp[0] = ""; var_temp[1] = ""; var_temp[2] = ""
        elif content[i] != "" or content[i] != "":
            var_temp[control] = var_temp[control] + content[i]
    file.close()


def scribe():
    '''This function allows to edit. It notifies the user'''
    global Table
    file = archive_in_usage("w")
    content = Table.get("1.0", END)
    var_temp = ""
    for i in range(len(content)):
        if content[i] == "\t" and content[i - 1] != "\t" and content[i - 1] != "\n":
            var_temp = var_temp + ","
        elif content[i] != "\t":
            var_temp = var_temp + str(content[i])
    file.write(var_temp)
    file.close()
    print("New contact was added correctly")


def delete_content():
    '''This function deletes content. It notifies the user'''
    file = archive_in_usage("w")
    file.close()
    print("Content deleted correctly")


def new():  # Manage directories
    '''This function starts a new job. It prevents the user from leaving unsaved work'''
    global ArchiveJobs
    if (ArchiveJobs == "" and Table.get("2.0", END) != "\n") or \
            (ArchiveJobs != "" and Table.get("2.0", END) != "\n"):
        action = tkinter.messagebox.askyesno("Warning\n", "\nAny unsaved changes will be lost.")
        if action == True:
            ArchiveJobs = ""
            cleaning(1)
            root.title("Window: New Document")
    else:
        ArchiveJobs = ""
        cleaning(1)
        root.title("Window: New Document")


def oppenig():
    '''This function opens files saved as txt or cvs'''
    global ArchiveJobs, root
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select file", filetypes=(("Excel Archives", "*.csv"),
                                                                             ("all files", "*.*")))
    ArchiveJobs = filename
    reading()
    root.title("Info " + ArchiveJobs)
    print(ArchiveJobs)


def save_as(opti):
    '''This function can save the work as a txt or cvs'''
    global ArchiveJobs
    filename = filedialog.asksaveasfile(mode="a",
                                        title="Save as", filetypes=(("Excel Archives", "*.csv"),
                                        ("Text Archives", "*.txt"), ("All Archives", "*.*")),
                                        defaultextension=".csv")
    ArchiveJobs = filename.name
    if opti == 1:
        root.title("Info " + ArchiveJobs)
        scribe()


def adding(name, email, phone, company, notes):
     '''This function Adds new content to the contact book.'''
     global Table
     Table.insert(INSERT, "\n" + str(name.get()) + "\t\t\t " +
                  str(email.get()) + "\t\t\t"+str(phone.get()) + "\t\t\t"+str(company.get()) +
                  "\t\t\t "+str(notes.get()) + " \n")


def cleaning(opti):
    '''This function delete entries from the user'''
    global Table, Vname, Vemail, Vphone, Vcompany, Vnotes
    if opti == 1:
        Table.delete("1.0", END)
    Vname.set("")
    Vemail.set("")
    Vphone.set("")
    Vcompany.set("")
    Vnotes.set("")
# Main and Menu declaration
ArchiveJobs = ""
root = Tk()
root.title("Info: New Document")
Vname = StringVar()
Vemail = StringVar()
Vphone = StringVar()
Vcompany = StringVar()
Vnotes = StringVar()
menu = Menu(root)
root.config(menu=menu)
archive = Menu(menu, tearoff=0)
archive.add_command(label="New", command=new)
archive.add_command(label="Open", command=oppenig)
archive.add_command(label="Save", command=saving)
archive.add_command(label="Save as", command=lambda: save_as(1))
archive.add_command(label="Formatting Archive", command=formating)
archive.add_separator()
archive.add_command(label="Exit", command=exit)
print('Goodbye')
About_It = Menu(menu, tearoff=0)
menu.add_cascade(label="Archive", menu=archive)
About_It.add_command(label="Author", command=lambda: dialog(1))
menu.add_cascade(label="About", menu=About_It)
# Using the Pack Manager
container = Frame(root, width=1000, height="520").pack()
# Declaring graphic elements and setting up the GUI
title = Label(container, text="Welcome to NMTLabs Contacts Book",
              font=("Times", 20), fg="blue").place(x=375, y=0)
Ename = Label(container, text="Name: ", font=("Times", 12),
              fg="blue").place(x=10, y=20)
Cname = Entry(container, textvariable=Vname, font=("Times", 12),
              fg="blue", width=20).place(x=90, y=21)
Eemail = Label(container, text="Email: ", font=("Times", 12),
               fg="blue").place(x=10, y=60)
Cemail = Entry(container, textvariable=Vemail, font=("Times", 12),
               fg="blue", width=20).place(x=90, y=61)
Ephone = Label(container, text="Phone: ", font=("Times", 12),
               fg="blue").place(x=10, y=90)
Cphone = Entry(container, textvariable=Vphone, font=("Times", 12),
               fg="blue", width=20).place(x=90, y=91)
Ecompany = Label(container, text="Company: ", font=("Times", 12),
               fg="blue").place(x=10, y=120)
Ccompany = Entry(container, textvariable=Vcompany, font=("Times", 12),
               fg="blue", width=20).place(x=90, y=121)
Enotes = Label(container, text="Notes: ", font=("Times", 12),
               fg="blue").place(x=10, y=150)
Cnotes = Entry(container, textvariable=Vnotes, font=("Times", 12),
               fg="blue", width=20).place(x=90, y=151)
frame = Frame(container)
frame.place(x=10, y=170)
Ttable = Label(frame, text="Name\t\t\t Email \t\t\t Phone \t\t\t Company \t\t\t Notes",
               font=("Times", 12), fg="blue")
Ttable.pack(side=TOP, fill=X)
Table = Text(frame, width=120, height=20)
Table.pack(side=LEFT)
scrool = Scrollbar(frame, command=Table.yview)
scrool.pack(side=RIGHT, fill=Y)
Table.insert(END, "\nArturo Salazar\t\t\taharturo@gmail.com"
                        "\t\t\t555-555-5555\t\t\tAnalitica \t\t\tHe likes art")
Table.insert(END, "\nElon Musk\t\t\temusk@spacex.comy"
                        "\t\t\t555-453-6723\t\t\tSpaceX\t\t\tHe is rich")
Table.insert(END, "\nLarry Page\t\t\tlpage@gmail.com"
                        "\t\t\t555-853-0653\t\t\tGoogle\t\t\tHe is also rich")
Table.insert(END, "\nTim Cooke\t\t\ttcook@apple.com"
                        "\t\t\t555-133-0419\t\t\tapple\t\t\tNew")
Table.config(yscrollcommand=scrool.set)
Badd = Button(container, text="Add", command=lambda: adding(Vname,
                Vemail, Vphone, Vcompany, Vnotes)).place(x=300, y=50)
Bclean = Button(container, text="Delete", command=lambda:
                cleaning(2)).place(x=300, y=100)

if __name__ == '__main__':
    root.mainloop()
