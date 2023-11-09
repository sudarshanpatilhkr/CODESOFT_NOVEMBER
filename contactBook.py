import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Contact List
        self.contacts = []
        
        # GUI Components
        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        
        # Place Components on Grid
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")
        
    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")
            
    def search_contact(self):
        search_term = tk.simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or
                       search_term in contact['Phone']]
            if results:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
    
    def update_contact(self):
        search_term = tk.simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or
                       search_term in contact['Phone']]
            if results:
                selected_contact = results[0]
                updated_name = tk.simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=selected_contact['Name'])
                updated_phone = tk.simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=selected_contact['Phone'])
                updated_email = tk.simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=selected_contact['Email'])
                updated_address = tk.simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=selected_contact['Address'])
                
                selected_contact['Name'] = updated_name if updated_name else selected_contact['Name']
                selected_contact['Phone'] = updated_phone if updated_phone else selected_contact['Phone']
                selected_contact['Email'] = updated_email if updated_email else selected_contact['Email']
                selected_contact['Address'] = updated_address if updated_address else selected_contact['Address']
                
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Update Contact", "No matching contacts found.")
    
    def delete_contact(self):
        search_term = tk.simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts if
                       search_term.lower() in contact['Name'].lower() or
                       search_term in contact['Phone']]
            if results:
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this contact?")
                if confirmation:
                    self.contacts.remove(results[0])
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Delete Contact", "No matching contacts found.")
                
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
