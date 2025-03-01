from pydantic import BaseModel, EmailStr
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str


class House(BaseModel):
    id: int
    name: str
    owner_id: int
    owner_name: str
    address: str


class Room(BaseModel):
    id: int
    name: str
    house_id: int


class Device(BaseModel):
    id: int
    type: str
    room_id: int
    status: str