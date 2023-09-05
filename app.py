import streamlit as st
import pandas as pd

from ucl_generator.generators import generate_groups, generate_pots, return_team_data
from ucl_generator.match_simulators import run_group_stage, run_knockouts

st.header('UCL Tournament Simulator')

# Session state variables
if "pots" not in st.session_state:
    st.session_state.pots = None
if "groups" not in st.session_state:
    st.session_state.groups = None
if "teams" not in st.session_state:
    st.session_state.teams = None
if "group_winners" not in st.session_state:
    st.session_state.group_winners = None
if "group_standings" not in st.session_state:
    st.session_state.group_standings = None
if "finalists" not in st.session_state:
    st.session_state.finalists = None
if "knockouts" not in st.session_state:
    st.session_state.knockouts = None

if st.session_state.pots is not None:
    pots = st.session_state.pots
if st.session_state.teams is not None:
    teams = st.session_state.teams
if st.session_state.group_standings is not None:
    group_standings = st.session_state.group_standings
if st.session_state.finalists is not None:
    finalists = st.session_state.finalists
if st.session_state.knockouts is not None:
    knockout_viz = st.session_state.knockouts

# Generate groups
if st.button('Generate Groups!'):

    st.subheader("Groups")

    st.session_state.pots = generate_pots()
    st.session_state.groups = generate_groups(st.session_state.pots)

    df = pd.DataFrame(st.session_state.groups).transpose()
    df.columns = [f"Group {columns+1}"for columns in df.columns]

    df1 = df.iloc[:,:4]
    df2 = df.iloc[:,4:]

    st.dataframe(df1)
    st.dataframe(df2)

# Run group stage match predictions
if st.session_state.groups is not None:

    if st.button('Run Group Stage'):

        st.subheader("Group winners / runners-up")

        st.session_state.teams = return_team_data()
        st.session_state.group_winners, st.session_state.group_standings = run_group_stage(teams=st.session_state.teams
                                                                                        , groups=st.session_state.groups)

        st.session_state.group_winners = pd.DataFrame(st.session_state.group_winners)
        df3 =  st.session_state.group_winners.iloc[:,:4]
        df4 =  st.session_state.group_winners.iloc[:,4:]

        df3.index = ['Winner','Runner-up']
        df4.index = ['Winner','Runner-up']

        st.table(df3)
        st.table(df4)

# Run knockout round group predictions
if st.session_state.group_winners is not None:

    if st.button('Run Knockout Rounds'):

        knockout_results = run_knockouts(st.session_state.group_standings
                                        , st.session_state.teams)

        finalists = list(knockout_results[-2].values())

        st.session_state.finalists = finalists

        knockout_viz = {'Round of 16':{},
                        'Quarter-finals':{},
                        'Semi-finals':{},
                        'Final':[]}

        for knockout_round, viz_dict in zip(knockout_results,knockout_viz.keys()):

            if type(knockout_round) is dict:

                for key, value in list(knockout_round.items()):

                    knockout_viz[viz_dict][f"{key[0]} vs {key[1]}"] = [value]

                knockout_viz[viz_dict] = pd.DataFrame(knockout_viz[viz_dict]).transpose().reset_index()
                knockout_viz[viz_dict].rename(columns={"index":"Match",0:'Winner'},inplace=True)

                st.subheader(viz_dict)
                st.write(knockout_viz[viz_dict])

            else:

                knockout_viz[viz_dict].append(knockout_round)

        st.session_state.knockouts = knockout_viz

if st.session_state.knockouts is not None:

    if st.button(f'Run final: {finalists[0]} vs {finalists[1]}'):

        st.balloons()
        st.header(f"{st.session_state.knockouts['Final'][0]} are champions!")
