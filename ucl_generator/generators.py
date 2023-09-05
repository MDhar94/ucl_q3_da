import random

def generate_pots():

    club_pots = {
        'RB Salzburg': {'pot': 3, 'domestic_league_country': 1},
        'Club Brugge KV': {'pot': 4, 'domestic_league_country': 2},
        'Dinamo Zagreb': {'pot': 4, 'domestic_league_country': 3},
        'Viktoria Plzeň': {'pot': 4, 'domestic_league_country': 4},
        'FC København': {'pot': 4, 'domestic_league_country': 5},
        'Manchester City': {'pot': 1, 'domestic_league_country': 6},
        'Liverpool FC': {'pot': 2, 'domestic_league_country': 6},
        'Chelsea FC': {'pot': 2, 'domestic_league_country': 6},
        'Tottenham Hotspur': {'pot': 2, 'domestic_league_country': 6},
        'Paris Saint-Germain': {'pot': 1, 'domestic_league_country': 7},
        'Olympique Marseille': {'pot': 4, 'domestic_league_country': 7},
        'Bayern München': {'pot': 1, 'domestic_league_country': 8},
        'Borussia Dortmund': {'pot': 3, 'domestic_league_country': 8},
        'Bayer Leverkusen': {'pot': 3, 'domestic_league_country': 8},
        'RB Leipzig': {'pot': 2, 'domestic_league_country': 8},
        'Eintracht Frankfurt': {'pot': 1, 'domestic_league_country': 8},
        'Maccabi Haifa': {'pot': 4, 'domestic_league_country': 9},
        'AC Milan': {'pot': 1, 'domestic_league_country': 10},
        'Inter': {'pot': 3, 'domestic_league_country': 10},
        'SSC Napoli': {'pot': 3, 'domestic_league_country': 10},
        'Juventus': {'pot': 2, 'domestic_league_country': 10},
        'AFC Ajax': {'pot': 1, 'domestic_league_country': 11},
        'SL Benfica': {'pot': 3, 'domestic_league_country': 12},
        'FC Porto': {'pot': 1, 'domestic_league_country': 12},
        'Sporting CP': {'pot': 3, 'domestic_league_country': 12},
        'Celtic FC': {'pot': 4, 'domestic_league_country': 13},
        'Rangers': {'pot': 4, 'domestic_league_country': 13},
        'Real Madrid': {'pot': 1, 'domestic_league_country': 14},
        'FC Barcelona': {'pot': 2, 'domestic_league_country': 14},
        'Atlético Madrid': {'pot': 2, 'domestic_league_country': 14},
        'Sevilla FC': {'pot': 2, 'domestic_league_country': 14},
        'Shakhtar Donetsk': {'pot': 3, 'domestic_league_country': 15},
    }

    return club_pots

def return_team_data():

    teams = {
        'RB Salzburg': {'Pot': 3, 'UEFA Ranking (22/23)': 71, 'DL Ranking (21/22)': 91.67, 'Country Coef': 38.85, 'Country': 'Austria'},
        'Club Brugge KV': {'Pot': 4, 'UEFA Ranking (22/23)': 38.5, 'DL Ranking (21/22)': 93.75, 'Country Coef': 30.6, 'Country': 'Belgium'},
        'Dinamo Zagreb': {'Pot': 4, 'UEFA Ranking (22/23)': 49.5, 'DL Ranking (21/22)': 90, 'Country Coef': 27.15, 'Country': 'Croatia'},
        'Viktoria Plzeň': {'Pot': 4, 'UEFA Ranking (22/23)': 31, 'DL Ranking (21/22)': 93.75, 'Country Coef': 27.8, 'Country': 'Czech Republic'},
        'FC København': {'Pot': 4, 'UEFA Ranking (22/23)': 40.5, 'DL Ranking (21/22)': 91.7, 'Country Coef': 27.175, 'Country': 'Denmark'},
        'Manchester City': {'Pot': 1, 'UEFA Ranking (22/23)': 134, 'DL Ranking (21/22)': 95, 'Country Coef': 106.641, 'Country': 'England'},
        'Liverpool FC': {'Pot': 2, 'UEFA Ranking (22/23)': 134, 'DL Ranking (21/22)': 90, 'Country Coef': 106.641, 'Country': 'England'},
        'Chelsea FC': {'Pot': 2, 'UEFA Ranking (22/23)': 123, 'DL Ranking (21/22)': 85, 'Country Coef': 106.641, 'Country': 'England'},
        'Tottenham Hotspur': {'Pot': 2, 'UEFA Ranking (22/23)': 83, 'DL Ranking (21/22)': 80, 'Country Coef': 106.641, 'Country': 'England'},
        'Paris Saint-Germain': {'Pot': 1, 'UEFA Ranking (22/23)': 112, 'DL Ranking (21/22)': 94.44, 'Country Coef': 60.081, 'Country': 'France'},
        'Olympique Marseille': {'Pot': 4, 'UEFA Ranking (22/23)': 44, 'DL Ranking (21/22)': 88.89, 'Country Coef': 60.081, 'Country': 'France'},
        'Bayern München': {'Pot': 1, 'UEFA Ranking (22/23)': 138, 'DL Ranking (21/22)': 94.44, 'Country Coef': 75.213, 'Country': 'Germany'},
        'Borussia Dortmund': {'Pot': 3, 'UEFA Ranking (22/23)': 78, 'DL Ranking (21/22)': 88.89, 'Country Coef': 75.213, 'Country': 'Germany'},
        'Bayer Leverkusen': {'Pot': 3, 'UEFA Ranking (22/23)': 53, 'DL Ranking (21/22)': 83.3, 'Country Coef': 75.213, 'Country': 'Germany'},
        'RB Leipzig': {'Pot': 2, 'UEFA Ranking (22/23)': 83, 'DL Ranking (21/22)': 77.78, 'Country Coef': 75.213, 'Country': 'Germany'},
        'Eintracht Frankfurt': {'Pot': 1, 'UEFA Ranking (22/23)': 61, 'DL Ranking (21/22)': 38.9, 'Country Coef': 75.213, 'Country': 'Germany'},
        'Maccabi Haifa': {'Pot': 4, 'UEFA Ranking (22/23)': 24.5, 'DL Ranking (21/22)': 92.85, 'Country Coef': 24.375, 'Country': 'Israel'},
        'AC Milan': {'Pot': 1, 'UEFA Ranking (22/23)': 38, 'DL Ranking (21/22)': 95, 'Country Coef': 76.902, 'Country': 'Italy'},
        'Inter': {'Pot': 3, 'UEFA Ranking (22/23)': 67, 'DL Ranking (21/22)': 90, 'Country Coef': 76.902, 'Country': 'Italy'},
        'SSC Napoli': {'Pot': 3, 'UEFA Ranking (22/23)': 66, 'DL Ranking (21/22)': 85, 'Country Coef': 76.902, 'Country': 'Italy'},
        'Juventus': {'Pot': 2, 'UEFA Ranking (22/23)': 107, 'DL Ranking (21/22)': 80, 'Country Coef': 76.902, 'Country': 'Italy'},
        'AFC Ajax': {'Pot': 1, 'UEFA Ranking (22/23)': 82.5, 'DL Ranking (21/22)': 94.44, 'Country Coef': 49.3, 'Country': 'Netherlands'},
        'SL Benfica': {'Pot': 3, 'UEFA Ranking (22/23)': 61, 'DL Ranking (21/22)': 83.33, 'Country Coef': 53.382, 'Country': 'Portugal'},
        'FC Porto': {'Pot': 1, 'UEFA Ranking (22/23)': 80, 'DL Ranking (21/22)': 94.44, 'Country Coef': 53.382, 'Country': 'Portugal'},
        'Sporting CP': {'Pot': 3, 'UEFA Ranking (22/23)': 55.5, 'DL Ranking (21/22)': 88.89, 'Country Coef': 53.382, 'Country': 'Portugal'},
        'Celtic FC': {'Pot': 4, 'UEFA Ranking (22/23)': 33, 'DL Ranking (21/22)': 91.7, 'Country Coef': 36.9, 'Country': 'Scotland'},
        'Rangers': {'Pot': 4, 'UEFA Ranking (22/23)': 50.25, 'DL Ranking (21/22)': 83.3, 'Country Coef': 36.9, 'Country': 'Scotland'},
        'Real Madrid': {'Pot': 1, 'UEFA Ranking (22/23)': 124, 'DL Ranking (21/22)': 95, 'Country Coef': 96.141, 'Country': 'Spain'},
        'FC Barcelona': {'Pot': 2, 'UEFA Ranking (22/23)': 114, 'DL Ranking (21/22)': 90, 'Country Coef': 96.141, 'Country': 'Spain'},
        'Atlético Madrid': {'Pot': 2, 'UEFA Ranking (22/23)': 105, 'DL Ranking (21/22)': 85, 'Country Coef': 96.141, 'Country': 'Spain'},
        'Sevilla FC': {'Pot': 2, 'UEFA Ranking (22/23)': 91, 'DL Ranking (21/22)': 80, 'Country Coef': 96.141, 'Country': 'Spain'},
        'Shakhtar Donetsk': {'Pot': 3, 'UEFA Ranking (22/23)': 71, 'DL Ranking (21/22)': 93.75, 'Country Coef': 31.8, 'Country': 'Ukraine'}}

    return teams

def generate_groups(club_pots):

    num_groups = 8

    pots = {}
    for team, data in club_pots.items():
        pot = data['pot']
        if pot not in pots:
            pots[pot] = []
        pots[pot].append(team)

    groups = [[] for _ in range(num_groups)]

    for pot, teams_in_pot in pots.items():
        random.shuffle(teams_in_pot)

    for group_idx in range(num_groups):
        for pot in sorted(pots.keys()):
            available_teams = [
                team for team in pots[pot] if
                club_pots[team]['domestic_league_country'] not in [club_pots[t]['domestic_league_country'] for t in groups[group_idx]]
            ]
            if available_teams:
                selected_team = random.choice(available_teams)
                groups[group_idx].append(selected_team)
                pots[pot].remove(selected_team)

    for group in groups:
        if len(group) < 4:
            group.append([val[0] for val in [pots[team] for team in pots] if len(val) > 0][0])

    return groups
