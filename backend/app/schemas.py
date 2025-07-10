from pydantic import BaseModel

class ExpertiseInput(BaseModel):
    name: str
    email: str
    expertise: str
    login_time: str
    logout_time: str

class SearchQuery(BaseModel):
    query: str
