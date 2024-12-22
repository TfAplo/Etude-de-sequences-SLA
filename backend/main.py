from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import sequences, index

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sequences.router, prefix="/sequences", tags=["Sequences"])
app.include_router(index.router)