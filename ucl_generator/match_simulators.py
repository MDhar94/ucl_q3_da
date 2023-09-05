import random
import itertools

def simulate_match(team1, team2, teams, points, results):
    # Extract relevant data for both teams
    data_team1 = teams[team1]
    data_team2 = teams[team2]

    # Simulate the match outcome based on rankings and coefficients with added randomness
    team1_score = (
        data_team1['UEFA Ranking (22/23)'] +
        data_team1['DL Ranking (21/22)'] +
        data_team1['Country Coef'] +
        random.uniform(-10000000, 10000000)  # Add randomness here
    )
    team2_score = (
        data_team2['UEFA Ranking (22/23)'] +
        data_team2['DL Ranking (21/22)'] +
        data_team2['Country Coef'] +
        random.uniform(-10000000, 10000000)  # Add randomness here
    )

    if abs(team1_score - team2_score) < 20:  # Adjust the threshold for a draw
        team1_result, team2_result = 'Draw', 'Draw'
    elif team1_score > team2_score:
        team1_result, team2_result = 'Win', 'Loss'
    else:
        team1_result, team2_result = 'Loss', 'Win'

    # Update points and results for both teams
    if team1_result == 'Win':
        points[team1] += 3
    elif team1_result == 'Draw':
        points[team1] += 1
        points[team2] += 1
    else:
        points[team2] += 3

    results[team1][team1_result] += 1
    results[team2][team2_result] += 1

    return team1_result, team2_result

def run_group_stage(teams, groups):
    # Initialize points and results for each team
    points = {team: 0 for team in teams}
    results = {team: {'Win': 0, 'Draw': 0, 'Loss': 0} for team in teams}

    # Simulate matches in each group
    for group_idx, group_teams in enumerate(groups, start=1):
        for team1, team2 in itertools.combinations(group_teams, 2):
            team1_result, team2_result = simulate_match(team1, team2, teams, points, results)

    # Determine the two winners from each group based on points
    group_winners = {}
    for group_idx, group_teams in enumerate(groups, start=1):
        sorted_teams = sorted(group_teams, key=lambda team: (-points[team], -results[team]['Win']))
        group_winners[f'Group {group_idx}'] = sorted_teams[:2]

    group_results = {}

    for group, winners in group_winners.items():
        group_results[group] = {'1st': winners[0], 'Runner-up': winners[1]}

    return group_winners, group_results

def simulate_knockout(team1, team2, teams):
    # Function to simulate a match and predict the winner

    uefa_ranking_weight = 0.5
    dl_ranking_weight = 0.40
    country_coef_weight = 0.1

    data_team1 = teams[team1]
    data_team2 = teams[team2]

    # Add random variations to each factor
    uefa_ranking_var = random.uniform(-10000000, 10000000)
    dl_ranking_var = random.uniform(-10000000, 10000000)
    country_coef_var = random.uniform(-10000000, 10000000)

    team1_weighted_sum = (
        uefa_ranking_weight * (data_team1['UEFA Ranking (22/23)'] + uefa_ranking_var) +
        dl_ranking_weight * (data_team1['DL Ranking (21/22)'] + dl_ranking_var) +
        country_coef_weight * (data_team1['Country Coef'] + country_coef_var)
    )

    team2_weighted_sum = (
        uefa_ranking_weight * (data_team2['UEFA Ranking (22/23)'] + uefa_ranking_var) +
        dl_ranking_weight * (data_team2['DL Ranking (21/22)'] + dl_ranking_var) +
        country_coef_weight * (data_team2['Country Coef'] + country_coef_var)
    )

    if team1_weighted_sum > team2_weighted_sum:
        return team1
    elif team2_weighted_sum > team1_weighted_sum:
        return team2
    else:
        return random.choice([team1, team2])

def run_knockouts(group_results, teams):

    # Initialize Round of 16 pairings
    round_of_16_pairings = []

    # Create lists of 1st and runner-up teams
    first_teams = [results['1st'] for group, results in group_results.items()]
    runner_up_teams = [results['Runner-up'] for group, results in group_results.items()]

    # Shuffle the lists to randomize pairings
    random.shuffle(first_teams)
    random.shuffle(runner_up_teams)

    # Generate Round of 16 pairings
    for i in range(len(first_teams)):
        first_team = first_teams[i]
        runner_up_team = runner_up_teams[i]

        # Check if the teams are from the same original group
        original_group_first = [group for group, results in group_results.items() if results['1st'] == first_team][0]
        original_group_runner_up = [group for group, results in group_results.items() if results['Runner-up'] == runner_up_team][0]

        if original_group_first != original_group_runner_up:
            round_of_16_pairings.append((first_team, runner_up_team))
        else:
            # If they are from the same group, find a valid pairing
            valid_pairings = [(first_team, team) for team in runner_up_teams if team != runner_up_team and
                            [group for group, results in group_results.items() if results['Runner-up'] == team][0] != original_group_first]
            selected_pairing = random.choice(valid_pairings)
            round_of_16_pairings.append(selected_pairing)

    # Simulate Round of 16 matches and predict winners
    round_of_16_results = {}
    for i, (team1, team2) in enumerate(round_of_16_pairings, start=1):
        winner = simulate_knockout(team1, team2, teams)
        round_of_16_results[(team1, team2)] = winner

    # Initialize the quarter-final pairings based on Round of 16 results
    quarter_final_pairings = [
        (round_of_16_results[round_of_16_pairings[0]], round_of_16_results[round_of_16_pairings[1]]),
        (round_of_16_results[round_of_16_pairings[2]], round_of_16_results[round_of_16_pairings[3]]),
        (round_of_16_results[round_of_16_pairings[4]], round_of_16_results[round_of_16_pairings[5]]),
        (round_of_16_results[round_of_16_pairings[6]], round_of_16_results[round_of_16_pairings[7]])
    ]

    # Simulate quarter-final matches and predict winners
    quarter_final_results = {}
    for i, (team1, team2) in enumerate(quarter_final_pairings, start=1):
        winner = simulate_knockout(team1, team2, teams)
        quarter_final_results[(team1, team2)] = winner

    # Initialize the semi-final pairings based on quarter-final results
    semi_final_pairings = [
        (quarter_final_results[quarter_final_pairings[0]], quarter_final_results[quarter_final_pairings[1]]),
        (quarter_final_results[quarter_final_pairings[2]], quarter_final_results[quarter_final_pairings[3]])
    ]

    # Simulate semi-final matches and predict winners
    semi_final_results = {}
    for i, (team1, team2) in enumerate(semi_final_pairings, start=1):
        winner = simulate_knockout(team1, team2, teams)
        semi_final_results[(team1, team2)] = winner


    # Initialize the final pairing based on semi-final results
    final_pairing = (semi_final_results[semi_final_pairings[0]], semi_final_results[semi_final_pairings[1]])

    # Simulate the final match and predict the winner
    final_result = simulate_knockout(final_pairing[0], final_pairing[1], teams)

    return round_of_16_results, quarter_final_results, semi_final_results, final_result
