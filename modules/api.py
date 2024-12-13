import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()

BRAWLHALLA_API_KEY = os.environ.get("BRAWLHALLA_API_KEY")

async def fetch_player_ranked_stats(brawlhalla_id):
    url = f"https://api.brawlhalla.com/player/{brawlhalla_id}/ranked?api_key={BRAWLHALLA_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def fetch_player_stats(brawlhalla_id):
    url = f"https://api.brawlhalla.com/player/{brawlhalla_id}/stats?api_key={BRAWLHALLA_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()