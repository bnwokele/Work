# from basketball_reference_scraper.teams import get_roster, get_team_stats, get_opp_stats, get_roster_stats, get_team_misc
# from basketball_reference_scraper.players import get_stats
# import pandas as pd
#
# teams = ['GSW', 'SAS']
# df = get_roster(teams[0], 2019)
# df['team_name'] = teams[0]
# df1 = get_roster(teams[1], 2019)
# df1['team_name'] = teams[1]
# frames = [df, df1]
# df2 = pd.concat(frames)
#
# print(df2)

from nba_api.stats.static import players
from nba_api.stats.endpoints import career_totals_regular_season

nba_players = players.get_players()
active_players = players.get_active_players()
##print('Number of players fetched: {}'.format(len(nba_players)))
#print(nba_players[0]['id'])


id = []
i = 0
while i < len(nba_players):
    x = nba_players[i]['id']
    id.append(x)
    i = i + 1
print(id)
