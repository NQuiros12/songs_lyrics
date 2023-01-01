#Import libraries
#uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import functions as fn
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def home():
    return """<html>
                <h1>Argentina</h1>
            </html>"""
@app.get("/artista/{artista}", response_class=HTMLResponse)
async def cancion_nro(artista:str):
    return fn.search_lyrics(artista)

