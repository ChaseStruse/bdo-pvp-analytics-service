import os
from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from ..repositories.aos_repository import create_tables
from sqlalchemy import create_engine

@asynccontextmanager
async def lifespan(app):
	load_dotenv()
	engine = create_engine(os.getenv("DB_URL") or "")
	create_tables(engine)
	yield


app = FastAPI(lifespan=lifespan)

# Import all route modules to register their routes
from . import aos_api
from . import adventurer_profile_api