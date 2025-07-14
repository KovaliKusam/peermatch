from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ExpertiseInput, SearchQuery, UserRegister
from app.db import insert_user, find_similar_experts, create_table
from app.embeddings import get_embedding
import bcrypt  # Import bcrypt for password hashing

app = FastAPI()
create_table()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(user: UserRegister):
    """Register a new user and insert their data into the database."""
    # Hash the password
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    try:
        insert_user(
            user.name,
            user.email,
            hashed_password,
            expertise=None,  # Placeholder, expertise will be added later
            current_project=None,  # Placeholder, current project will be added later
            current_project_embedding=None,  # Placeholder, project embedding will be added later
            embedding=None,  # Placeholder, expertise embedding will be added later
            login_time=None,  # Placeholder, login time will be added later
            logout_time=None  # Placeholder, logout time will be added later
        )
        print('User registered successfully')
    except Exception as e:
        print('Error during registration:', e)
        raise HTTPException(status_code=500, detail="Database insert error")

    return {"message": "User registered successfully"}

@app.post("/submit_expertise")
def submit_expertise(data: ExpertiseInput):
    """Submit user expertise and insert it into the database."""
    print('Called get embeddings')
    
    # Get the embedding for the user's expertise
    vector = get_embedding(data.expertise)
    
    if vector is not None and 'data' in vector and len(vector['data']) > 0:
        expertise_embedding = vector
    else:
        raise HTTPException(status_code=400, detail="Invalid expertise embedding")  # Raise error if embedding is invalid
    
    # Get the embedding for the user's current project
    project_vector = get_embedding(data.current_project)
    
    if project_vector is not None and 'data' in project_vector and len(project_vector['data']) > 0:
        current_project_embedding = project_vector
    else:
        current_project_embedding = None  # Set to None if invalid
    
    print('Embedding retrieved successfully')
    
    # Insert user data into the database
    try:
        insert_user(
            data.name,
            data.email,
            password=None,  # Password should not be updated here
            expertise=data.expertise,
            current_project=data.current_project,
            current_project_embedding=current_project_embedding,  # Use the embedding for the current project
            embedding=expertise_embedding,  # Use the embedding for the expertise
            login_time=data.login_time,
            logout_time=data.logout_time
        )
        print('User data inserted successfully')
    except Exception as e:
        print('Error during insert:', e)
        raise HTTPException(status_code=500, detail="Database insert error")

    # Find similar experts only if expertise embedding is valid
    similar_experts = find_similar_experts(expertise_embedding)
    return {"message": "Expertise submitted", "similar_experts": similar_experts}

@app.post("/find_experts")
def find_experts(data: SearchQuery):
    """Find similar experts based on the input query."""
    vector = get_embedding(data.query)
    
    if vector is None or 'data' not in vector:
        raise HTTPException(status_code=400, detail="Failed to retrieve valid embedding")
    
    similar_experts = find_similar_experts(vector)
    return similar_experts