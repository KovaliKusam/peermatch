from pydantic import BaseModel

class ExpertiseInput(BaseModel):
    name: str
    email: str
    expertise: str

class SearchQuery(BaseModel):
    query: str
