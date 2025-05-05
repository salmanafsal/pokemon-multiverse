from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=151"

async def fetch_pokemon_details(client, url):
    response = await client.get(url)
    data = response.json()
    return {
        "name": data["name"],
        "image": data["sprites"]["front_default"]
    }

@app.get("/", response_class=HTMLResponse)
async def get_pokemon(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(POKEAPI_URL)
        data = response.json()
        pokemon_results = data.get("results", [])
        
        # Fetch details for each Pokémon concurrently
        tasks = [fetch_pokemon_details(client, p["url"]) for p in pokemon_results]
        pokemon_list = await asyncio.gather(*tasks)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "pokemon_list": pokemon_list
    })
