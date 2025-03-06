from pydantic import BaseModel, EmailStr
from typing import List, Optional


class User(BaseModel):
    name: str
    email: EmailStr
    phone: str


class UserResponse(User):
    id: int


class House(BaseModel):
    name: str
    owner_id: int
    owner_name: str
    address: str


class HouseResponse(House):
    id: int


class Room(BaseModel):
    name: str
    house_id: int


class RoomResponse(Room):
    id: int


class Device(BaseModel):
    type: str
    room_id: int
    status: str


class DeviceResponse(Device):
    id: int