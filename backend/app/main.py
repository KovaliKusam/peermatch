# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.schemas import ExpertiseInput, SearchQuery
# from app.db import insert_user, find_similar_experts
# from app.embeddings import get_embedding

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/submit_expertise")
# def submit_expertise(data: ExpertiseInput):
#     print()
#     print()
#     print()
#     print('A')
#     print()
#     print()
#     print('Called get embeddings')
#     vector = get_embedding(data.expertise)
#     print()
#     print()
#     print()
#     print('vector done')
#     print()
#     print()
#     print()
#     print('Called insert')
#     print()
#     print()
#     print(data.name, data.email, data.expertise, data.login_time, data.logout_time)
#     insert_user(data.name, data.email, data.expertise, vector, data.login_time, data.logout_time)
#     print()
#     print()
#     print('done with call')
#     print()
#     print()
#     print()
#     return {"message": "Expertise submitted"}

# @app.post("/find_experts")
# def find_experts(data: SearchQuery):
#     vector = get_embedding(data.query)
#     return find_similar_experts(vector)

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ExpertiseInput, SearchQuery
from app.db import insert_user, find_similar_experts
from app.embeddings import get_embedding

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit_expertise")
def submit_expertise(data: ExpertiseInput):
    """Submit user expertise and insert it into the database."""
    print('Called get embeddings')
    
    # Get the embedding for the user's expertise
    vector = get_embedding(data.expertise)
    
    if vector is None or 'data' not in vector:
        raise HTTPException(status_code=400, detail="Failed to retrieve valid embedding")
    
    print('Embedding retrieved successfully')
    
    # Insert user data into the database
    try:
        insert_user(data.name, data.email, data.expertise, vector, data.login_time, data.logout_time)
        print('User data inserted successfully')
    except Exception as e:
        print('Error during insert:', e)
        raise HTTPException(status_code=500, detail="Database insert error")

    return {"message": "Expertise submitted"}

@app.post("/find_experts")
def find_experts(data: SearchQuery):
    """Find similar experts based on the input query."""
    vector = get_embedding(data.query)
    
    if vector is None or 'data' not in vector:
        raise HTTPException(status_code=400, detail="Failed to retrieve valid embedding")
    
    similar_experts = find_similar_experts(vector)
    return similar_experts