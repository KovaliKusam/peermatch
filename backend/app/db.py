import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Establish the connection
conn = psycopg2.connect(
    dbname="peermatch",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
conn.autocommit = True  # optional: avoids needing conn.commit() every time

# Function to insert or update a user
def insert_user(name, email, expertise, embedding):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users (name, email, expertise, embedding)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (email) DO UPDATE 
            SET expertise = EXCLUDED.expertise, embedding = EXCLUDED.embedding
        """, (name, email, expertise, embedding))

# Function to find similar users based on vector similarity
def find_similar_experts(embedding):
    embedding_str = "[" + ",".join(map(str, embedding)) + "]"
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT name, email, expertise, 1 - (embedding <=> %s::vector) AS similarity
            FROM users
            ORDER BY similarity DESC
            LIMIT 5;
        """, [embedding_str])
        return cur.fetchall()
