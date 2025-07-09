import sqlite3
import numpy as np
 
conn = sqlite3.connect("peermatch.db", check_same_thread=False)
cur = conn.cursor()
 
# Create table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT PRIMARY KEY,
    expertise TEXT,
    embedding TEXT
)
""")
conn.commit()
 
def insert_user(name, email, expertise, embedding):
    embedding_str = str(embedding.tolist())
    with conn:
        conn.execute("""
            INSERT INTO users (name, email, expertise, embedding)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
                expertise = excluded.expertise,
                embedding = excluded.embedding
        """, (name, email, expertise, embedding_str))
 
def find_similar_experts(input_vector):
    cur = conn.cursor()
    cur.execute("SELECT name, email, expertise, embedding FROM users")
    results = cur.fetchall()
 
    similar = []
    for name, email, expertise, embedding_str in results:
        embedding = np.array(eval(embedding_str))
        score = float(np.dot(input_vector, embedding) / (np.linalg.norm(input_vector) * np.linalg.norm(embedding)))
        similar.append({
            "name": name,
            "email": email,
            "expertise": expertise,
            "similarity": score
        })
 
    similar.sort(key=lambda x: x["similarity"], reverse=True)
    return similar[:5]