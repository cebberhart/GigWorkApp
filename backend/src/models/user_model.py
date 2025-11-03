#Placeholder User model - represents database table

class User:
    def __init__(self, id, email, password, role):
        self.id = id #User id
        self.email = email #User email
        self.password = password #Password (hash later)
        self.role = role #Role (Client, Worker, Admin)