import os
import sqlite3

# Buat folder database kalau belum ada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER = BASE_DIR

DB_NAME = os.path.join(DB_FOLDER, 'game.db')

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect()
    c = conn.cursor()
    
    #Buat Table Players
    
    c.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                user_id INTEGER
            )
            ''')
    
    #Buat Table Player Attribute
    c.execute('''
            CREATE TABLE IF NOT EXISTS player_attributes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                role TEXT,
                health INTEGER,
                base_damage INTEGER,
                skill_damage INTEGER,
                ultimate_damage INTEGER,
                inventory TEXT
            )
            ''')
    
    #Buat Table Weapons
    c.execute('''
            CREATE TABLE IF NOT EXISTS weapons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                damage_bonus INTEGER,
                type TEXT,s
                rarity TEXT
            )
            ''')
    
    #Buat Table Weapons
    c.execute('''
            CREATE TABLE IF NOT EXISTS enemies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                role TEXT,
                health INTEGER,
                basic_damage INTEGER,
                skill_damage INTEGER,
                ultimate_damage INTEGER
            )
            ''')
    conn.commit()
    conn.close()
    
