# import sqlite3
# import numpy as np
# import json
# import os
# from datetime import datetime, time
# import pytz

# # Construct the path to the database in the backend folder
# db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "peermatch.db")

# def create_connection():
#     """Create a new database connection."""
#     return sqlite3.connect(db_path, check_same_thread=False)

# def create_table():
#     """Create the users table if it doesn't exist."""
#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             name TEXT,
#             email TEXT PRIMARY KEY,
#             password TEXT,
#             expertise TEXT,
#             current_project TEXT,
#             current_project_embedding TEXT,
#             embedding TEXT,
#             login_time TEXT,
#             logout_time TEXT,
#             timezone TEXT
#         )
#         """)
#         conn.commit()

# def insert_user(name, email, password, expertise, current_project, current_project_embedding, embedding, login_time, logout_time, timezone):
#     """Insert or update a user in the database."""
#     print('In insert user')
#     print('Before')
#     print(print_table())

#     try:
#         embedding_str = json.dumps(embedding['data'][0]['embedding']) if embedding and 'data' in embedding else None
#         current_project_embedding_str = json.dumps(current_project_embedding['data'][0]['embedding']) if current_project_embedding and 'data' in current_project_embedding else None

#         with create_connection() as conn:
#             cur = conn.cursor()
#             print("Inserting values:", name, email, expertise, current_project, login_time, logout_time, timezone)
#             cur.execute("""
#                 INSERT INTO users (name, email, password, expertise, current_project, current_project_embedding, embedding, login_time, logout_time, timezone)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#                 ON CONFLICT(email) DO UPDATE SET
#                     name = excluded.name,
#                     password = excluded.password,
#                     expertise = excluded.expertise,
#                     current_project = excluded.current_project,
#                     current_project_embedding = excluded.current_project_embedding,
#                     embedding = excluded.embedding,
#                     login_time = excluded.login_time,
#                     logout_time = excluded.logout_time,
#                     timezone = excluded.timezone
#             """, (name, email, password, expertise, current_project, current_project_embedding_str, embedding_str, login_time, logout_time, timezone))
#             print('Insert successful!')
#             print('After')
#             print()
#             print(print_table())
#     except Exception as e:
#         print('Error during insert:', e)
#         raise

# def find_similar_experts(input_vector):
#     """Find similar experts based on the input embedding vector."""
#     input_embedding = np.array(input_vector['data'][0]['embedding'])
#     print("Input embedding shape:", input_embedding.shape)

#     similar = []
#     now_utc = datetime.utcnow().time()

#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("SELECT name, email, expertise, embedding, login_time, logout_time, timezone FROM users WHERE embedding IS NOT NULL")
#         results = cur.fetchall()

#         for name, email, expertise, embedding_str, login_time, logout_time, timezone in results:
#             try:
#                 embedding = np.array(json.loads(embedding_str))
#                 if input_embedding.shape[0] != embedding.shape[0]:
#                     print("Dimension mismatch: input %d, db %d", input_embedding.shape[0], embedding.shape[0])
#                     continue

#                 score = float(np.dot(input_embedding, embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(embedding)))

#                 # Convert UTC time to user's local time
#                 if login_time and logout_time and timezone:
#                     login_dt = datetime.fromisoformat(login_time)
#                     logout_dt = datetime.fromisoformat(logout_time)

#                     login_utc = login_dt.time()
#                     logout_utc = logout_dt.time()

#                     if login_utc <= now_utc <= logout_utc:
#                         similar.append({
#                             "name": name,
#                             "email": email,
#                             "expertise": expertise,
#                             "similarity": score
#                         })
#             except Exception as e:
#                 print(f"Error processing user {email}: {e}")
#                 continue

#     similar = [x for x in similar if x["similarity"] >= 0.6]
#     similar.sort(key=lambda x: x["similarity"], reverse=True)

#     return similar[:5]

# def fetch_user_expertise():
#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("SELECT expertise, login_time, logout_time FROM users")
#         return cur.fetchall()

# def fetch_user_details():
#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("SELECT name, email, expertise, current_project, current_project_embedding, login_time, logout_time FROM users")
#         return cur.fetchall()

# def clear_user_table():
#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("DELETE FROM users")
#         conn.commit()
#         print("All rows cleared from the users table.")

# def fetch_user_by_email(email):
#     """Fetch a user by email from the database, ignoring users with a None password."""
#     with create_connection() as conn:
#         cur = conn.cursor()
#         print(print_table())
#         cur.execute("""
#             SELECT name, email, password 
#             FROM users 
#             WHERE email = ? AND password IS NOT NULL
#         """, (email,))
#         print(print_table())
#         print()
#         print()
#         print(cur.fetchone())
#         user_data = cur.fetchone()
#         return user_data
    
# def print_table():
#     with create_connection() as conn:
#         cur = conn.cursor()
#         cur.execute("""SELECT name, email, password, expertise, current_project, login_time, logout_time, timezone FROM users""")
#         print(cur.fetchall())

# # print(print_table())

import sqlite3
import numpy as np
import json
import os
from datetime import datetime, date

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
            password TEXT,
            expertise TEXT,
            current_project TEXT,
            current_project_embedding TEXT,
            embedding TEXT,
            login_time TEXT,
            logout_time TEXT
        )
        """)
        conn.commit()

def insert_user(name, email, password, expertise, current_project, current_project_embedding, embedding, login_time, logout_time):
    """Insert or update a user in the database."""
    print('In insert user')
    print('Before')
    print(print_table())

    try:
        embedding_str = json.dumps(embedding['data'][0]['embedding']) if embedding and 'data' in embedding else None
        current_project_embedding_str = json.dumps(current_project_embedding['data'][0]['embedding']) if current_project_embedding and 'data' in current_project_embedding else None

        with create_connection() as conn:
            cur = conn.cursor()
            print("Inserting values:", name, email, expertise, current_project, login_time, logout_time)
            cur.execute("""
                INSERT INTO users (name, email, password, expertise, current_project, current_project_embedding, embedding, login_time, logout_time)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(email) DO UPDATE SET
                    name = excluded.name,
                    password = excluded.password,
                    expertise = excluded.expertise,
                    current_project = excluded.current_project,
                    current_project_embedding = excluded.current_project_embedding,
                    embedding = excluded.embedding,
                    login_time = excluded.login_time,
                    logout_time = excluded.logout_time
            """, (name, email, password, expertise, current_project, current_project_embedding_str, embedding_str, login_time, logout_time))
            print('Insert successful!')
            print('After')
            print()
            print(print_table())
    except Exception as e:
        print('Error during insert:', e)
        raise

def find_similar_experts(input_vector):
    """Find similar experts based on the input embedding vector."""
    input_embedding = np.array(input_vector['data'][0]['embedding'])
    print("Input embedding shape:", input_embedding.shape)

    similar = []
    print('A')
    now_utc = datetime.now()
    print(now_utc)

    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, email, expertise, embedding, login_time, logout_time FROM users WHERE embedding IS NOT NULL")
        results = cur.fetchall()

        for name, email, expertise, embedding_str, login_time, logout_time in results:
            try:
                embedding = np.array(json.loads(embedding_str))
                if input_embedding.shape[0] != embedding.shape[0]:
                    print("Dimension mismatch: input %d, db %d", input_embedding.shape[0], embedding.shape[0])
                    continue

                score = float(np.dot(input_embedding, embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(embedding)))

                # Check if the user is logged in
                if login_time and logout_time:
                    # Assume today's date if the time is provided without a date
                    today_date = date.today().isoformat()
                    if ':' in login_time and len(login_time) == 8:  # e.g., '11:00:00'
                        login_time = f"{today_date}T{login_time}"
                    if ':' in logout_time and len(logout_time) == 8:  # e.g., '11:00:00'
                        logout_time = f"{today_date}T{logout_time}"

                    login_dt = datetime.fromisoformat(login_time)
                    logout_dt = datetime.fromisoformat(logout_time)

                    if login_dt <= now_utc <= logout_dt:
                        similar.append({
                            "name": name,
                            "email": email,
                            "expertise": expertise,
                            "similarity": score
                        })
            except Exception as e:
                print(f"Error processing user {email}: {e}")
                continue

    similar = [x for x in similar if x["similarity"] >= 0.6]
    similar.sort(key=lambda x: x["similarity"], reverse=True)

    return similar[:5]

def fetch_user_expertise():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT expertise, login_time, logout_time FROM users")
        return cur.fetchall()

def fetch_user_details():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT name, email, expertise, current_project, current_project_embedding, login_time, logout_time FROM users")
        return cur.fetchall()

def clear_user_table():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users")
        conn.commit()
        print("All rows cleared from the users table.")

def fetch_user_by_email(email):
    """Fetch a user by email from the database, ignoring users with a None password."""
    with create_connection() as conn:
        cur = conn.cursor()
        print(print_table())
        cur.execute("""
            SELECT name, email, password 
            FROM users 
            WHERE email = ? AND password IS NOT NULL
        """, (email,))
        print(print_table())
        print()
        print()
        # print(cur.fetchone())
        user_data = cur.fetchone()
        print(user_data)
        return user_data
    
def print_table():
    with create_connection() as conn:
        cur = conn.cursor()
        cur.execute("""SELECT name, email, password, expertise, current_project, login_time, logout_time FROM users""")
        print(cur.fetchall())

# print(print_table())