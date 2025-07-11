import sqlite3
import numpy as np
import json
import os
from datetime import datetime

# Construct the path to the database in the backend folder
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "peermatch.db")

def create_connection():
    """Create a new database connection."""
    return sqlite3.connect(db_path, check_same_thread=False)

def create_table():
    """Create the users table if it doesn't exist."""
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            email TEXT PRIMARY KEY,
            expertise TEXT,
            embedding TEXT,
            login_time TEXT,
            logout_time TEXT
        )
        """)
        conn.commit()

def insert_user(name, email, expertise, embedding, login_time, logout_time):
    """Insert a user into the database."""
    print('In insert user')
    
    try:
        embedding_str = json.dumps(embedding['data'][0]['embedding'])

        with create_connection() as conn:
            cur = conn.cursor()
            print("Inserting values:", name, email, expertise, login_time, logout_time)
            cur.execute("""
                INSERT INTO users (name, email, expertise, embedding, login_time, logout_time)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(email) DO UPDATE SET
                    name = excluded.name,
                    expertise = excluded.expertise,
                    embedding = excluded.embedding,
                    login_time = excluded.login_time,
                    logout_time = excluded.logout_time
            """, (name, email, expertise, embedding_str, login_time, logout_time))
            print('Insert successful!')
    except Exception as e:
        print('Error during insert:', e)

def find_similar_experts(input_vector):
    """Find similar experts based on the input embedding vector."""
    input_embedding = np.array(input_vector['data'][0]['embedding'])
    print("Input embedding shape:", input_embedding.shape)

    similar = []
    current_time = datetime.now()  # Get the current time

    with create_connection() as conn:
        cur = conn.cursor()
        # Retrieve login_time and logout_time along with user details
        cur.execute("SELECT name, email, expertise, embedding, login_time, logout_time FROM users")
        results = cur.fetchall()

        for name, email, expertise, embedding_str, login_time, logout_time in results:
            embedding = np.array(json.loads(embedding_str))

            # Check if the dimensions match
            if input_embedding.shape[0] != embedding.shape[0]:
                print("Dimension mismatch: input %d, db %d", input_embedding.shape[0], embedding.shape[0])
                continue  # Skip this embedding if dimensions don't match

            # Calculate cosine similarity
            score = float(np.dot(input_embedding, embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(embedding)))

            # Convert login_time and logout_time to datetime objects for comparison
            login_time_dt = datetime.fromisoformat(login_time)
            logout_time_dt = datetime.fromisoformat(logout_time)

            # Check if current time is between login and logout times
            if login_time_dt <= current_time <= logout_time_dt:
                similar.append({
                    "name": name,
                    "email": email,
                    "expertise": expertise,
                    "similarity": score
                })

    # Sort the results by similarity score in descending order
    similar = [x for x in similar if x["similarity"] >= 0.6]
    similar.sort(key=lambda x: x["similarity"], reverse=True)

    return similar[:5]

def fetch_user_expertise():
    """Fetch and return expertise from users."""
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT expertise, login_time, logout_time FROM users")
        users = cur.fetchall()
        return users

def clear_user_table():
    """Clear all rows in the users table without altering its structure."""
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users")  # This will delete all rows in the users table
        conn.commit()  # Commit the changes to the database
        print("All rows cleared from the users table.")

# Fetch and print expertise from users
users = fetch_user_expertise()
print("User expertise:", users)
