from pydantic import BaseModel, EmailStr
import random


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = random.randint(0, 10000)  # allows for 10001 users

    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def getPhone(self):
        return self.phone
    
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email

    def setPhone(self, phone):
        self.phone = phone

    def delete(self):
        self.remove
        
    
    

    