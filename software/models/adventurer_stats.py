class AdventurerStats():
	def __init__(self, avg_kills=0, avg_deaths=0, avg_cc=0, avg_dealt=0, avg_taken=0, 
			  	 avg_healed=0, win_loss_ratio=0) -> None:
		self.avg_kills = avg_kills
		self.avg_deaths = avg_deaths
		self.avg_cc = avg_cc
		self.avg_dealt = avg_dealt
		self.avg_taken = avg_taken
		self.avg_healed = avg_healed
		self.total_wins = 0
		self.total_losses = 0
		self.total_mvps = 0
		self.total_aces = 0
		self.win_loss_ratio = win_loss_ratio
		self.classes_that_bested_you = {}

	def calculate_adventurer_stats(self, stats):
		self.avg_kills += stats.kills
		self.avg_deaths += stats.deaths
		self.avg_cc += stats.cc
		self.avg_dealt += stats.dealt
		self.avg_taken += stats.taken
		self.avg_healed += stats.healed

	def calculate_averages(self, matches_played):
		self.avg_kills /= matches_played
		self.avg_deaths /= matches_played
		self.avg_cc /= matches_played
		self.avg_dealt /= matches_played
		self.avg_taken /= matches_played
		self.avg_healed /= matches_played
		self.win_loss_ratio = self.total_wins / matches_played

	def convert_to_json(self):
		return {
			"avgKills": self.avg_kills,
			"avgDeaths": self.avg_deaths,
			"avgCC": self.avg_cc,
			"avgDealt": self.avg_dealt,
			"avgTaken": self.avg_taken,
			"avgHealed": self.avg_healed,
			"winLossRatio": self.win_loss_ratio,
			"totalWins": self.total_wins,
			"totalLosses": self.total_losses,
			"totalMvps": self.total_mvps,
			"totalAces": self.total_aces,
			"classesThatBestedYou": self.classes_that_bested_you
		}