from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= "Choose your own adventure API",
    description= "An API for a choose your own adventure game",
    version="0.1.0",
    docs_url="/docs",
    recdocs_url="/redoc",
)
