import streamlit as st
import pandas as pd
import plotly.express as px

from ucl_generator.generators import generate_groups, generate_pots, return_team_data
from ucl_generator.match_simulators import run_group_stage, run_knockouts

# if "txt_input" not in st.session_state.input:
#     st.session_state.txt_input = None

st.header('Multiple simulation generator')

simulation_n = st.text_input('Please enter how many simulations to run:',"")
winners = {}

if simulation_n != "":

    for i in range(int(simulation_n)):

        pots = generate_pots()
        groups = generate_groups(pots)

        teams = return_team_data()
        group_winners, group_standings = run_group_stage(teams=teams, groups=groups)

        group_winners = pd.DataFrame(group_winners)

        knockout_results = run_knockouts(group_standings, teams)

        winner = knockout_results[-1]

        if winner in winners.keys():
            winners[winner] += 1

        else:
            winners[winner] = 1

    winner_df = pd.DataFrame(winners
                            , index=[1]).transpose().rename(columns={1:'Wins'}).sort_values(by=['Wins']
                                                                                            , ascending=False)

    winner_chart = px.bar(winner_df,labels={"value": "Number of wins","index": "Teams"})

    st.plotly_chart(winner_chart)
