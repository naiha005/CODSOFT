import json
from tkinter import *
from tkinter import messagebox

# contact dic
contacts = {}


# update contacts
def update_data():
    name = name_entry.get()
    if name in contacts:
        contacts[name]["phone_no"] = phone_no_entry.get()
        contacts[name]["email"] = email_entry.get()
        name_entry.delete(0, 'end')
        phone_no_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        view_contacts()
    else:
        messagebox.showinfo("Error", "Contact not found.")


# delete contact
def delete_data():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        name_entry.delete(0, 'end')
        phone_no_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        view_contacts()
    else:
        messagebox.showinfo("Error", "Contact not found.")


# view contacts 
def view_contacts():
    contact_listbox.delete(0, 'end')
    for name, info in contacts.items():
        contact_listbox.insert('end', f"{name} - {info['phone_no']}")


# save data
def add_data():
    name = name_entry.get()
    phone_no = phone_no_entry.get()
    email = email_entry.get()

    # contacts = {name: {
    #     'phone_no': phone_no,
    #     'email': email,
    # }}

    if len(name) == 0 or len(email) == 0 or len(phone_no) == 0:
        messagebox.showinfo(title="Opps", message="Please fill all the fields")
    else:
            if name not in contacts:
                contacts[name] = {"phone_no": phone_no, "email": email}
                name_entry.delete(0, 'end')
                phone_no_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                view_contacts()
            else:
                messagebox.showinfo("Error", "Contact already exists with that name.")


# search data
def search_data():
    search_term = name_entry.get()
    found = False
    contact_listbox.delete(0, 'end')
    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone_no']:
            contact_listbox.insert('end', f"{name} - {info['phone_no']}")
            found = True
    if not found:
        contact_listbox.insert('end', "No matching contacts found.")


# ------- ui step up ---------------
window =Tk()
window.title("Contact Book")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

contact_book_label = Label(text="Contact Book", font=('Helvetica bold', 24))
contact_book_label.grid(row=0, column=1)

# label
contact_name_label = Label(text="Name", pady=10)
contact_name_label.grid(row=1, column=0)

contact_number_label = Label(text="Phone No", pady=10)
contact_number_label.grid(row=2, column=0)

contact_email_label = Label(text="Email", pady=10)
contact_email_label.grid(row=3, column=0)

space_label = Label(text="", pady=10)
space_label.grid(row=4, column=0)

# Enteries
name_entry = Entry(width=32, highlightthickness=0)
name_entry.focus()
name_entry.grid(row=1, column=1)

phone_no_entry = Entry(width=32, highlightthickness=0)
phone_no_entry.grid(row=2, column=1)

email_entry = Entry(width=32, highlightthickness=0)
email_entry.grid(row=3, column=1)

# buttons
search_btn = Button(text="Search", command=search_data)
search_btn.grid(row=1, column=2, sticky='W')

save_btn = Button(text="save", command=add_data)
save_btn.grid(row=4, column=0, columnspan=2)

update_btn = Button(text="Update", command=update_data)
update_btn.grid(row=4, column=1, columnspan=3)

delete_btn = Button(text="Delete", command=delete_data)
delete_btn.grid(row=4, column=3, columnspan=4)


# display box
contact_listbox = Listbox()
contact_listbox.grid(row=7, column=0, columnspan=4)

window.mainloop()