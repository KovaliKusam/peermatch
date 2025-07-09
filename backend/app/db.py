import sqlite3
import numpy as np
import json

# Connect to the SQLite database
conn = sqlite3.connect("peermatch.db", check_same_thread=False)
cur = conn.cursor()

# Create the users table if it doesn't exist
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
    # Convert the embedding to a string representation
    embedding_str = json.dumps(embedding['data'][0]['embedding'])  # Store as JSON string
    with conn:
        cur.execute("""
            INSERT INTO users (name, email, expertise, embedding)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(email) DO UPDATE SET
                expertise = excluded.expertise,
                embedding = excluded.embedding
        """, (name, email, expertise, embedding_str))

def find_similar_experts(input_vector):
    input_embedding = np.array(input_vector['data'][0]['embedding'])
    print("Input embedding shape:", input_embedding.shape)
    
    cur = conn.cursor()
    cur.execute("SELECT name, email, expertise, embedding FROM users")
    results = cur.fetchall()

    similar = []
    for name, email, expertise, embedding_str in results:
        embedding = np.array(json.loads(embedding_str))

        # Check if the dimensions match
        if input_embedding.shape[0] != embedding.shape[0]:
            print(f"Dimension mismatch: input {input_embedding.shape[0]}, db {embedding.shape[0]}")
            continue  # Skip this embedding if dimensions don't match

        # Calculate cosine similarity
        score = float(np.dot(input_embedding, embedding) / (np.linalg.norm(input_embedding) * np.linalg.norm(embedding)))

        similar.append({
            "name": name,
            "email": email,
            "expertise": expertise,
            "similarity": score
        })

    # Sort the results by similarity score in descending order
    similar.sort(key=lambda x: x["similarity"], reverse=True)
    
    return similar[:5]

