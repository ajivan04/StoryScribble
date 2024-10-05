import sqlite3

def create_library():
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('./library.db')

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Create Users table
    cur.execute('''CREATE TABLE IF NOT EXISTS Users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )''')

    # Create Stories table
    cur.execute('''CREATE TABLE IF NOT EXISTS Stories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES Users (id)
                )''')

    # Create Pages table
    cur.execute('''CREATE TABLE IF NOT EXISTS Pages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    story_id INTEGER,
                    image_path TEXT,
                    text TEXT,
                    FOREIGN KEY (story_id) REFERENCES Stories (id)
                )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()
