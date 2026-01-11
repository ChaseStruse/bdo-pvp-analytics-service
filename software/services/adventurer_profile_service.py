from .aos_service import get_matches_by_adventurer_name_service

def calculate_adventurer_stats(current_adventurer_stats, stats):
	current_adventurer_stats["avgKills"] += stats.kills
	current_adventurer_stats["avgDeaths"] += stats.deaths
	current_adventurer_stats["avgCC"] += stats.cc
	current_adventurer_stats["avgDealt"] += stats.dealt
	current_adventurer_stats["avgTaken"] += stats.taken
	current_adventurer_stats["avgHealed"] += stats.healed

	return current_adventurer_stats


def calculate_averages(adventurers_stats, matches_played):
	adventurers_stats["avgKills"] /= matches_played
	adventurers_stats["avgDeaths"] /= matches_played
	adventurers_stats["avgCC"] /= matches_played
	adventurers_stats["avgDealt"] /= matches_played
	adventurers_stats["avgTaken"] /= matches_played
	adventurers_stats["avgHealed"] /= matches_played
	adventurers_stats["winLossRatio"] = adventurers_stats["totalWins"] / matches_played

	return adventurers_stats


def get_adventurer_aos_details(adventurer_name: str):
	matches = get_matches_by_adventurer_name_service(adventurer_name=adventurer_name)

	adventurers_stats = {
		"avgKills": 0.0,
		"avgDeaths": 0.0,
		"avgCC": 0.0,
		"avgDealt": 0.0,
		"avgTaken": 0.0,
		"avgHealed": 0.0,
		"totalMvps": 0,
		"totalAces": 0,
		"winLossRatio": 0.0,
		"totalWins": 0,
		"totalLosses": 0,
	}
	classes_that_bested_you = {}
	for match in matches:
		for player in match.player_stats:
			if player.adventurer_name == match.adventurer_name:
				adventurers_stats = calculate_adventurer_stats(current_adventurer_stats=adventurers_stats, stats=player)
				if match.allied_team_win == True: # pyright: ignore[reportGeneralTypeIssues]
					if player.mvp_ace == "MVP":
						adventurers_stats["totalMvps"] += 1
					adventurers_stats["totalWins"] += 1
				else:
					if player.mvp_ace == "ACE":
						adventurers_stats["totalAces"] += 1
					adventurers_stats["totalLosses"] += 1

			elif player.team == "enemy":
				if match.allied_team_win == False: # pyright: ignore[reportGeneralTypeIssues]
					class_name = player.class_name
					if class_name not in classes_that_bested_you:
						classes_that_bested_you[class_name] = {
							"totalDamageDealt": 0,
							"totalKills": 0
						}
					classes_that_bested_you[class_name]["totalDamageDealt"] += player.dealt
					classes_that_bested_you[class_name]["totalKills"] += player.kills


	print("TOTALS PRIOR TO AVERAGES")
	print(adventurers_stats)
	adventurers_stats = calculate_averages(adventurers_stats=adventurers_stats, matches_played=len(matches))

	adventurers_stats["classesThatBestedYou"] = classes_that_bested_you
	return adventurers_stats

