from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Form
from fastapi.responses import StreamingResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from middleware.middleware import signJWT, JWTBearer

import os

# Create FastAPI app
app = FastAPI()

PORT = os.getenv("PORT")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Uvicorn!"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Points to the "app" instance in the "main" module
        host="0.0.0.0",  # Accessible on your network
        port= int(PORT),       # Port to listen on
        reload=True      # Enable auto-reload for development
    )