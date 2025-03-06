import sqlite3

DATABASE_FILE = "homeapi.db"

def getDBConnection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.row
    return connection

def initializeDatabase():
    connection = getDBConnection()
    cursor = connection.cursor()

    # create users table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL
        )''')
    
    # create houses table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS houses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        owner_id INTEGER NOT NULL,
        owner_name TEXT NOT NULL,
        address TEXT NOT NULL,
        FOREIGN KEY(owner_id) REFERENCES user(id) ON DELETE CASCADE
    )''')

    # create rooms table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL,
        house_id INTEGER NOT NULL,
        FOREIGN KEY(house_id) REFERENCES houses(id) ON DELETE CASCADE
        )''')

    # create devices table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        room_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY(room_id) REFERENCES rooms(id) on delete cascade
        )''')
        
    connection.commit()
    connection.close()

initializeDatabase()