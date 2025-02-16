from pydantic import BaseModel, EmailStr
import random
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
    owner_name = str
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


houses: List[House] = []
rooms: List[Room] = []
devices: List[Device] = []
users: List[User] = []


# house
def createHouse(house: House):
    houses.append(house)


def getAllHouses() -> List[House]:
    return houses


def findHouseByID(house_id: int) -> Optional[House]:
    # find house and return 
    # None if not found
    for house in houses:
        if house.id == house_id:
            return house
    return None


def deleteHouse(house_id: int) -> bool:
    # house = # find house
    # if house is found 
    house = findHouseByID(house_id=house_id)
    if house:
        houses.remove(house)
        return True
    else:
        return False
 

def updateHouse(house_id: int, 
                address: Optional[str] = None, 
                owner_name: Optional[str] = None, 
                name: Optional[str] = None) -> bool:
    house = findHouseByID(house_id=house_id)
    if house:
        if address is not None:
            house.address = address
        if owner_name is not None:
            house.owner_name = owner_name
        if name is not None:
            house.name = name
        return True
    else: 
        return False


# Room
def createRoom(room: Room):
    rooms.append(room)


def findRoomByID(room_id: int) -> Optional[Room]:
    # find room, else None
    for room in rooms:
        if room.id == room:
            return room
    return None


def deleteRoom(room_id: int) -> bool:
    room = findRoomByID(room_id=room_id)
    if room:
        rooms.remove(room)
        return True
    else:
        return False


def updateRoom(room_id: int,
               name: Optional[str] = None) -> bool:
    room = findRoomByID(room_id=room_id)
    if room:
        if name is not None:
            room.name = name
        return True
    return False

# devices
def createDevice(device: Device):
    devices.append(device)


def findDeviceByid(device_id: int) -> Optional[Device]:
    for device in devices:
        if device.id == device_id:
            return device
        else:
            return None
        

def deleteDevice(device_id: int) -> bool:
    device = findDeviceByid(device_id=device_id)
    if device:
        devices.remove(device)
        return True
    else:
        return False
    

def updateDevice(device_id: int,
                 name: Optional[str] = None) -> bool:
    device = findDeviceByid(device_id=device_id)
    if device:
        if name is not None:
            device.name = name
        return True
    return False
