from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ExpertiseInput, SearchQuery, UserRegister, UserLogin
from app.db import insert_user, find_similar_experts, create_table, fetch_user_by_email
from app.embeddings import get_embedding
import bcrypt
from datetime import datetime

app = FastAPI()
create_table()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register")
def register(user: UserRegister):
    """Register a new user and insert their data into the database."""
    print(user)
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    try:
        insert_user(
            name=user.name,
            email=user.email,
            password=hashed_password,
            expertise=None,
            current_project=None,
            current_project_embedding=None,
            embedding=None,
            login_time=None,
            logout_time=None
        )
        print('User registered successfully')
    except Exception as e:
        print('Error during registration:', e)
        raise HTTPException(status_code=500, detail="Database insert error")

    return {"message": "User registered successfully"}

@app.post("/submit_expertise")
def submit_expertise(data: ExpertiseInput):
    """Submit user expertise and insert it into the database."""
    print('In function')
    
    # Get the embedding for the user's expertise
    vector = get_embedding(data.expertise)
    if vector is not None and 'data' in vector and len(vector['data']) > 0:
        expertise_embedding = vector
    else:
        raise HTTPException(status_code=400, detail="Invalid expertise embedding")

    # Get the embedding for the user's current project
    project_vector = get_embedding(data.current_project)
    if project_vector is not None and 'data' in project_vector and len(project_vector['data']) > 0:
        current_project_embedding = project_vector
    else:
        current_project_embedding = None

    print('Embedding retrieved successfully')

    # Convert login/logout times to UTC (removed timezone handling)
    login_time_utc = data.login_time
    logout_time_utc = data.logout_time

    try:
        insert_user(
            name=data.name,
            email=data.email,
            password=None,
            expertise=data.expertise,
            current_project=data.current_project,
            current_project_embedding=current_project_embedding,
            embedding=expertise_embedding,
            login_time=login_time_utc,
            logout_time=logout_time_utc
        )
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.post("/login")
def login(user: UserLogin):
    """Login a user and return a success message or error."""
    print('In login')
    try:
        # Fetch user from the database
        user_data = fetch_user_by_email(user.email)
        print('Fetched data:', user_data)

        # Check if user_data is None or empty
        if user_data is None:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        # Check the password
        stored_password = user_data[2]  # Assuming the password is the third column
        print('Stored password:', stored_password)

        if not bcrypt.checkpw(user.password.encode('utf-8'), stored_password.encode('utf-8')):
            raise HTTPException(status_code=400, detail="Invalid email or password")

        return {"message": "Login successful"}

    except Exception as e:
        print('Error during login:', e)
        raise HTTPException(status_code=500, detail="Error during login process")