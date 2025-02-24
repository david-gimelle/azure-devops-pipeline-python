import uvicorn
from fastapi.middleware.cors import CORSMiddleware  
from app.routes import app
from config import Config

# Enable CORS for the entire application
app.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.corsAllowedOrigin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)