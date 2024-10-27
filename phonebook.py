import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

class Phonebook:
    def __init__(self, file_path="phonebook.json"):
        self.file_path = file_path
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.contacts = {contact["name"]: Contact(**contact) for contact in data}
        except FileNotFoundError:
            print("No contacts found.")
            pass

    def save_contacts(self):
        with open(self.file_path, "w") as file:
            json.dump([contact.to_dict() for contact in self.contacts.values()], file)

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        self.save_contacts()
        print(f"Added contact: {contact.name}")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Removed contact: {name}")

    def search_contact(self, name):
        return self.contacts.get(name)

phonebook = Phonebook()
phonebook.add_contact(Contact("Nimal Bandara", "123-456-7890", "nimalB@gmail.com"))
phonebook.add_contact(Contact("Kamal Herath", "111-423-9687", "kamall@gmail.com"))
phonebook.add_contact(Contact("John de Silva", "923-275-4242", "dejohn@gmail.com"))
phonebook.remove_contact("Kamal Herath")
contact = phonebook.search_contact("John de Silva")
print(contact.to_dict())
