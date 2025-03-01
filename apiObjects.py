from model import House, Room, Device, User
from typing import List, Optional
from fastapi import FastAPI, HTTPException



app = FastAPI()

house_db: List[House] = []
room_db: List[Room] = []
device_db: List[Device] = []
user_db: List[User] = []


# house
@app.post("/houses/", response_model=House)
def createHouse(house: House):
    house_db.append(house)
    return house

@app.get("/houses/", response_model=List[House])
def getAllHouses():
    return {"Houses" : house_db}


@app.get("/houses/{house_id}", response_model=House)
def findHouseByID(house_id: int):
    for house in house_db:
        if house.id == house_id:
            return house
    raise HTTPException(status_code=404, detail=f"House with {house_id} not found")


@app.delete("/houses/{house_id}", response_model=House)
def deleteHouse(house_id: int):
    for house in house_db:
        if house.id == house_id:
            house_db.remove(house)
            return True
    raise HTTPException(status_code=404, detail="House not found")
 

@app.put("/house/", response_model=House)
def updateHouse(house_id: int, 
                address: Optional[str] = None, 
                owner_name: Optional[str] = None, 
                name: Optional[str] = None) -> bool:
    for house in house_db:
        if house.id == house_id:
            if address:
                house.address = address
            if owner_name:
                house.owner_name = owner_name
            if name:
                house.name = name
        else:
            raise HTTPException(status_code=404, detail="House not found")

# Room
@app.post("/rooms/", response_model=Room)
def createRoom(room: Room):
    room_db.append(room)
    return room


@app.get("/rooms/", response_model=List[Room])
def getRooms():
    return room_db


@app.get("/rooms/{room_id}", response_model=Room)
def findRoomByID(room_id: int):
    for room in room_db:
        if room.id == room_id:
            return room
    raise HTTPException(status_code=404, detail="Room not found")


@app.delete("/rooms/{room_id}", response_model=Room)
def deleteRoom(room_id: int):
    for room in room_db:
        if room.id == room_id:
            room_db.remove(room)
            return Room
    raise HTTPException(status_code=404, detail="Room not found")



@app.put("/rooms/{room_id}", response_model=Room)
def updateRoom(room_id: int,
               name: Optional[str] = None):
    for room in room_db:
        if room.id == room_id:
            if name:
                room.name = name
            return room
    raise HTTPException(status_code=404, detail="Room not found")


# devices
@app.post("/devices/", response_model=Device)
def createDevice(device: Device):
    device_db.append(device)
    return device


@app.get("/device/", response_model=List[Device])
def findDevices():
    return device_db


@app.get("/device/{device_id}", response_model=Device)
def findDeviceByid(device_id: int):
    for device in device_db:
        if device.id == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")
        

@app.delete("/device/{device_id}", response_model=Device)
def deleteDevice(device_id: int):
    for device in device_db:
        if device.id == device_id:
            device_db.remove(device)
            return device
    raise HTTPException(status_code=404, detail="Device not found")
        

@app.put("/device/{device_id}", response_model=Device)
def updateDevice(device_id: int,
                 name: Optional[str] = None) -> bool:
    for device in device_db:
        if device.id == device_id:
            if name:
                device.name = name
            return device
    raise HTTPException(status_code=404, detail="Device not found")
