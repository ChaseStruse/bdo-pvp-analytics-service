import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.aos_request import Base, Match, PlayerStats

def create_tables(engine):
    Base.metadata.create_all(bind=engine)


def get_match_data_by_id(match_id):
	load_dotenv()
	engine = create_engine(os.getenv("DB_URL") or "")
	Session = sessionmaker(bind=engine)
	session = Session()

	try:
		match = session.query(Match).filter(Match.id == match_id).first()
		if not match:
			return None
		# Load player stats
		player_stats = session.query(PlayerStats).filter(PlayerStats.match_id == match_id).all()
		# Optionally, attach player_stats to match if not already loaded
		match.player_stats = player_stats
		return match
	finally:
		session.close()


def get_matches_data_by_adventurer_name(adventurer_name: str):
	load_dotenv()
	engine = create_engine(os.getenv("DB_URL") or "")
	Session = sessionmaker(bind=engine)
	session = Session()

	try:
		# Use ilike for case-insensitive matching and return all matches
		matches = session.query(Match).filter(Match.adventurer_name.ilike(adventurer_name)).all()
		if not matches:
			return []
		# Attach player stats for each match
		for match in matches:
			player_stats = session.query(PlayerStats).filter(PlayerStats.match_id == match.id).all()
			match.player_stats = player_stats
		return matches
	finally:
		session.close()


def insert_match_data(match_data):
	load_dotenv()
	engine = create_engine(os.getenv("DB_URL") or "")
	Session = sessionmaker(bind=engine)
	session = Session()

	try:
		session.add(match_data)
		session.commit()
		return match_data.id
	except Exception as e:
		session.rollback()
		raise e
	finally:
		session.close()