import pytest
from apiObjects import House, User, Room, Device


def test_CreateHouse():
    houses = []
    house = House(id=1, 
                  name="My House",
                  address="48 Brighton Ave",
                  owner_id=12,
                  owner_name="John")
    house2 = House(id=2, 
                  name="John's House",
                  address="1056 Commonwealth Ave",
                  owner_id=9,
                  owner_name="John")
    houses.append(house)
    houses.append(house2)
    assert house.id == 1
    assert house.name == "My House"
    assert house.address == "48 Brighton Ave"
    assert house.owner_id == 12
    assert house.owner_name == "John"
    assert len(houses) == 2


def test_createUser():
    user = User(id=12,
                name="Ben",
                email="ben@gmail.com",
                phone="555-555-5555")
    
    assert user.id == 12
    assert user.name == "Ben"
    assert user.email == "ben@gmail.com"
    assert user.phone == "555-555-5555"


def test_createRoom():
    room = Room(id=9,
                name="bedroom",
                house_id=12)
    assert room.id == 9
    assert room.name == "bedroom"
    assert room.house_id == 12


def test_createDevice():
    device = Device(id=1,
                    type="google Home mini",
                    room_id=9,
                    status="Active")
    
    assert device.id == 1
    assert device.type == "google Home mini"
    assert device.room_id == 9
    assert device.status == "Active"


