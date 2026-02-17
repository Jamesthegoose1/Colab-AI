from fastapi import FastAPI
from core.ai_manager import AIManager
from plugins.music import MusicPlugin
import nest_asyncio
import os

# required for Colab's event loop
nest_asyncio.apply()

app = FastAPI()
ai = AIManager()
music_plugin = MusicPlugin()

# Example request model (you can move to schemas.py)
from pydantic import BaseModel
class MusicRequest(BaseModel):
    style: str = "EDM"

@app.get("/")
def home():
    return {"message": "Colab AI API running!"}

@app.post("/generate_music")
def generate_music(req: MusicRequest):
    track_path = music_plugin.generate(req.style)
    return {"status": "ok", "track_path": track_path}
