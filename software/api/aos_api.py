import os
from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from ..services.aos_service import get_match_by_id, insert_match
from ..repositories.aos_repository import create_tables
from sqlalchemy import create_engine

@asynccontextmanager
async def lifespan(app):
	load_dotenv()
	engine = create_engine(os.getenv("DB_URL") or "")
	create_tables(engine)
	yield

app = FastAPI(lifespan=lifespan)


# GET /message
@app.get("/aos/match/{match_id}")
async def get_match(match_id):
	return get_match_by_id(match_id=match_id)

# POST /message
@app.post("/aos/match")
async def post_message(req_body: dict):
      return insert_match(req_body=req_body)
