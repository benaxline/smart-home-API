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


houses: List[House] = []
rooms: List[Room] = []
devices: List[Device] = []
users: List[User] = []


# house
def createHouse(house: House):
    pass


def getAllHouses() -> List[House]:
    pass


def findHouseByID(house_id: int) -> Optional[House]:
    # find house and return 
    # None if not found
    pass


def deleteHouse(house_id: int) -> bool:
    # house = # find house
    # if house is found 
    pass
 

def updateHouse(house_id: int, 
                address: Optional[str] = None, 
                owner_name: Optional[str] = None, 
                name: Optional[str] = None) -> bool:
    # create house
    # change the elements
    pass


# Room
def createRoom(room: Room):
    pass

def findRoomByID(room_id: int) -> Optional[Room]:
    # find room, else None
    pass


def deleteRoom(room_id: int) -> bool:
    # find room
    # remove element from list
    pass


def updateRoom(room_id: int,
               name: Optional[str] = None) -> bool:
    # find room
    # update elements
    pass


# devices
def createDevice(device: Device):
    # create device
    pass


def findDeviceByid(device_id: int) -> Optional[Device]:
    # find device
    pass
        

def deleteDevice(device_id: int) -> bool:
    # find device
    # remove from list
    pass
    

def updateDevice(device_id: int,
                 name: Optional[str] = None) -> bool:
    # find device 
    # update elements
    pass
