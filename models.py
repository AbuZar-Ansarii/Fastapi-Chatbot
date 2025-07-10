from pydantic import BaseModel


# Pydantic request and response models
class Query(BaseModel):
    query: str

class QueryResponse(BaseModel):
    question: str
    answer: str
