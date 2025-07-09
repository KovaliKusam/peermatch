from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ExpertiseInput, SearchQuery
from app.db import insert_user, find_similar_experts
from app.embeddings import get_embedding
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.post("/submit_expertise")
def submit_expertise(data: ExpertiseInput):
    vector = get_embedding(data.expertise)
    insert_user(data.name, data.email, data.expertise, vector)
    return {"message": "Expertise submitted"}
 
@app.post("/find_experts")
def find_experts(data: SearchQuery):
    vector = get_embedding(data.query)
    return find_similar_experts(vector)