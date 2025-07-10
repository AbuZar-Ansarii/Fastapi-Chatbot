from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Query,QueryResponse
from work import bot_system

# Initialize FastAPI app
app = FastAPI(title="Mini Chat Bot")

# Enable CORS (required for frontend access like Streamlit or React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base route
@app.get("/home")
def base():
    return {"response": "Everything now is ok..."}

# Query route
@app.post("/query", response_model=QueryResponse)
async def bot_response(request: Query):
    result = bot_system.query_response(request.query)
    return QueryResponse(
        question=result["question"],
        answer=result["answer"]
    )



