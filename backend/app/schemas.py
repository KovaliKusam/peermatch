from pydantic import BaseModel
from typing import Optional, List

class ExpertiseInput(BaseModel):
    name: str
    email: str
    expertise: str
    current_project: str
    login_time: str
    logout_time: str

class SearchQuery(BaseModel):
    query: str

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str