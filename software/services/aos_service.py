import uuid
from datetime import datetime
from ..repositories.aos_repository import get_match_data_by_id, insert_match_data, get_matches_data_by_adventurer_name
from ..models.aos_request import Match, PlayerStats

def convert_req_body_to_model(req_body):
	match = Match(
		match_type=req_body["matchType"],
		adventurer_name=req_body["adventurerName"],
		match_date=datetime.strptime(req_body["matchDate"], "%m/%d/%y").date(),
		allied_team_win=req_body["alliedTeamWin"]

	)

	players = []
	for player in req_body["players"]:
		player_stats = PlayerStats(
			team=player["team"],
			adventurer_name=player["adventurerName"],
			class_name=player["className"],
			kills=player["kills"],
			deaths=player["deaths"],
			cc=player["cc"],
			dealt=player["dealt"],
			taken=player["taken"],
			healed=player["healed"],
			mvp_ace=player["mvpAce"]
		)
		players.append(player_stats)

	match.player_stats = players
	return match


def get_match_by_id(match_id):
	match_id_uuid = uuid.UUID(match_id)
	return get_match_data_by_id(match_id=match_id_uuid)

def get_matches_by_adventurer_name_service(adventurer_name):
	return get_matches_data_by_adventurer_name(adventurer_name=adventurer_name)

def insert_match(req_body):
	match = convert_req_body_to_model(req_body=req_body)
	return insert_match_data(match_data=match)