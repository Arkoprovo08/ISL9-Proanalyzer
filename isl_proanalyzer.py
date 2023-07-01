import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.graph_objects as go
plt.style.use('ggplot')

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Goalkeeper Analysis
df = pd.read_csv("Goalkeeper_Data.csv")
df = df.set_index('P_id')

df['goals conceded per match'] = df['goals conceded']/df['matches']
cols_for_permatch = ['saves','clean sheets','catches','passes','touches','shots faced','shots on target','clearances']
for i in cols_for_permatch:
    df[i + ' per match'] = (df[i]/df['matches'])
df['clean sheets %'] = (df['clean sheets']/df['matches'])*90
df['goals conceded per match'] = df['goals conceded']/df['matches']
per_match = ['full name','goals conceded','saves', 'clean sheets', 'catches','pass accuracy','touches per match','shots on target', 'clearances','clean sheets %']

per_90_data = df[per_match]
cols_for_radar = ['goals conceded','saves', 'clean sheets', 'catches','pass accuracy', 'touches per match','shots on target', 'clearances','clean sheets %']

#Defender Analysis
df_def = pd.read_csv('def_stats.csv')
df_def = df_def.set_index('P_id')
cols_for_permatch_def = ['passes','touches','clearances']
for i in cols_for_permatch_def:
    df_def[i + ' per match'] = (df_def[i]/df_def['matches'])  
per_match_def = ['full name','pass accuracy','blocks','goal conversion rate','tackles','interceptions','clearances per match','passes per match', 'touches per match']
per_90_data_def = df_def[per_match_def]
cols_for_radar_def = ['pass accuracy','blocks','goal conversion rate','tackles','interceptions','clearances per match','passes per match', 'touches per match']

#Midfielder/Forward Dataset load
df_all = pd.read_csv('mid_data.csv')

#Mid Analysis
df_mid = df_all.tail(11)
df_mid['goals per game%'] = df_mid['goals/game']*100
df_mid['touches per game'] = df_mid['touches']/df_mid['matches']
per_match_mid = ['full name','goals per game%','touches per game','assists','shots','avg passes/game','chances created','pass accuracy', 'interceptions','blocks']
per_90_data_mid = df_mid[per_match_mid]
cols_for_radar_mid = ['touches per game','goals per game%','shots','assists','avg passes/game','chances created','pass accuracy', 'interceptions','blocks']

#Fwd Analysis
df_fwd = df_all.head(13)
df_fwd['goals per game%'] = df_fwd['goals/game']*100
df_fwd['touches per game'] = df_fwd['touches']/df_fwd['matches']
per_match_fwd = ['full name','goals per game%','touches per game','assists','shots','avg passes/game','chances created','pass accuracy', 'interceptions','blocks']
per_90_data_fwd = df_fwd[per_match_fwd]
cols_for_radar_fwd = ['touches per game','goals per game%','shots','assists','avg passes/game','chances created','pass accuracy', 'interceptions','blocks']

#Standings
df_league = pd.read_csv('Standings.csv')

#Fantasy
f1 = pd.read_csv('f1.csv')
fan_fwd = f1.head(13)
fan_fwd = fan_fwd.set_index('Player Id')
fan_fwd = fan_fwd.style.format(precision=1)
fan_mid = f1.tail(11)
fan_mid = fan_mid.set_index('Player Id')
fan_mid = fan_mid.style.format(precision=1)

f2 = pd.read_csv('f2.csv')
fan_def = f2.head(10)
fan_def = fan_def.set_index('Player Id')
fan_def = fan_def.style.format(precision=1)
fan_gk = f2.tail(10)
fan_gk = fan_gk.set_index('Player Id')
fan_gk = fan_gk.style.format(precision=1)

st.title("ISL ProAnalyzer")
st.header("Hero ISL 2022-23 Analysis")
st.image("lsilogolaunch281014.jpg",width = 200)

#Dashbord
st.sidebar.header('Dashboard `ISL ProAnalyzer`')
st.sidebar.subheader('Features')
nav = st.sidebar.radio("",["Home","Goalkeepers Analysis","Defenders Analysis","Midfeilders Analysis","Strikers Analysis",'Create your own fantasy team','About Us'])
if nav == "Home":
    st.header("Home")
    st.video("vi.mp4")
    st.write("The 2022–23 Indian Super League was the ninth season of the Indian Super League, the first season as the only top division,[1] and the 27th season of top-tier Indian football. It commenced on 7 October 2022 and concluded with the final on 18 March 2023.")
    st.write("Jamshedpur were the defending premiers and Hyderabad were the defending champions.Mumbai City won their second League Winners' Shield and ATK Mohun Bagan won their first championship title having defeating Bengaluru in the final.")
    st.markdown("""
## Changes from last season
1. Six instead of four clubs will compete for the playoffs. The top two clubs qualify directly for the playoffs, while the next four sides will play a single-legged match to decide the remaining two teams for the semifinals. The third-ranked team will play against the sixth-ranked team. Similarly, the fourth-ranked team will play against the fifth-ranked team, with the higher-ranked side hosting the match

2. The traditional home and away format has returned.
## Clubs Participating
""")
    st.image("team.png")
    st.markdown("""
    ## Match Results 
    """)
    st.image("Results.png")
    st.markdown("""
    ## Form
    """)
    st.image("Form.png")
    st.markdown("""
    ## Playoffs 
    """)
    st.image("Playoffs.png")
    st.markdown("""
    ## Champions 
    """)
    st.image("atk.jpg",width = 200)
    st.write("ATK Mohun Bagan held their nerves in a tightly contested Hero Indian Super League (ISL) final as they beat Bengaluru FC 4-3 on penalties to lift the Hero ISL title at the Jawaharlal Nehru Stadium in Goa on Saturday. In a game that ended 2-2 in regulation time, ATKMB’s Dimitri Petratos scored all three penalties he took on the night before Vishal Kaith’s save from Bruno Ramires’ penalty in the shootout brought them one step closer. Bengaluru FC’s Pablo Perez then sent his spot-kick over the bar as the Mariners sealed the result in a game where they had unsettled Bengaluru FC right from the start.")
if nav == "Goalkeepers Analysis":

    st.header("Top Goalkeepers of the season")
    #st.table(data)
    st.subheader("Select Analysis")
    graph = st.selectbox("Pick from the list below",["Most Saves","Least Goals Conceded","Most Clean Sheets","Most Touches as a Goalkeeper","Most Passes as a Goalkeeper"])
    if graph == "Most Saves":
        df= df.sort_values(by=['saves'],ascending=False)
        col = ['full name','club','saves']
        st.table(df[col])
        st.subheader("Most Saves")
        fig = plt.figure(figsize = (15, 10))
        name = df['name']
        saves = df['saves'] 
        # creating the bar plot
        plt.bar(name,saves,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 150})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Saves",fontsize = 15)
        plt.title("Most Saves",fontsize = 15)
        st.pyplot()
    if graph == "Least Goals Conceded":
        df= df.sort_values(by=['goals conceded per match'],ascending=True)
        col = ['full name','club','goals conceded per match']
        st.table(df[col])
        st.subheader("Least Goals Conceded")
        fig = plt.figure(figsize = (15, 10))
        name = df['name']
        goals_conceded_per_match = df['goals conceded per match'] 
        # creating the bar plot
        plt.bar(name,goals_conceded_per_match,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 150})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Goals conceded per 90",fontsize = 15)
        plt.title("Goals conceded per 90",fontsize = 15)
        st.pyplot()
    if graph == "Most Clean Sheets":
        df= df.sort_values(by=['clean sheets'],ascending=False)
        col = ['full name','club','clean sheets']
        st.table(df[col])
        st.subheader("Most Clean Sheets")
        fig = plt.figure(figsize = (15, 10))
        name = df['name']
        clean_sheets = df['clean sheets'] 
        # creating the bar plot
        plt.bar(name,clean_sheets,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 150})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Clean sheets",fontsize = 15)
        plt.title("Most Clean sheets",fontsize = 15)
        st.pyplot()
    if graph == "Most Touches as a Goalkeeper":
        df= df.sort_values(by=['touches'],ascending=False)
        col = ['full name','club','touches']
        st.table(df[col])
        st.subheader("Most Touches as a Goalkeeper")
        fig = plt.figure(figsize = (15, 10))
        name = df['name']
        touches = df['touches'] 
        # creating the bar plot
        plt.bar(name,touches,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 150})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("touches",fontsize = 15)
        plt.title("Most Touches",fontsize = 15)
        st.pyplot()
    if graph == "Most Passes as a Goalkeeper":
        df= df.sort_values(by=['passes'],ascending=False)
        col = ['full name','club','passes']
        st.table(df[col])
        st.subheader("Most Passes as a Goalkeeper")
        fig = plt.figure(figsize = (15, 10))
        name = df['name']
        pas = df['passes'] 
        # creating the bar plot
        plt.bar(name,pas,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 150})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Passes",fontsize = 15)
        plt.title("Most Passes",fontsize = 15)
        st.pyplot()
    st.subheader("Stats comparison")
    player1 = st.selectbox("Choose goalkeepers you want to compare",["Gurpreet Sandhu","Vishal Kaith","Phurba Lachenpa","Mirshad Michu","Amrinder Singh","Kamaljit Singh","Gurmeet Singh","Prabhsukhan Gill","Dheeraj Moirangthem","Arindam Bhattacharja"])
    player2 = st.selectbox("",["Gurpreet Sandhu","Vishal Kaith","Phurba Lachenpa","Mirshad Michu","Amrinder Singh","Kamaljit Singh","Gurmeet Singh","Prabhsukhan Gill","Dheeraj Moirangthem","Arindam Bhattacharja"])
    if player1 == player2:
        st.error("Please compare between different players")     
    else:
        # Initiate the plotly go figure
        fig = go.Figure()
        # Add Radar plots for different players:
        fig.add_trace(go.Scatterpolar(r=per_90_data.loc[(per_90_data["full name"] == player1),
        cols_for_radar].sum(),theta=cols_for_radar,fill='toself',name=player1))
        fig.add_trace(go.Scatterpolar(r=per_90_data.loc[(per_90_data["full name"] == player2), 
        cols_for_radar].sum(),theta=cols_for_radar,fill='toself',name=player2))
        # Additional properties for the plot:
        fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",polar=dict(radialaxis=dict(
        visible=True,)),showlegend=True)
        st.write(fig)
if nav == "Defenders Analysis":
    st.header("Top Defenders of the season")
    #st.table(data)
    st.subheader("Select Analysis")
    graph = st.selectbox("Pick from the list below",["Most Clearances","Most Interceptions","Most Tackles","Most Blocks","Least fouls committed"])
    if graph == "Most Clearances":
        df_def = df_def.sort_values(by=['clearances'],ascending = False)
        col = ['full name','club','clearances']
        st.table(df_def[col])
        st.subheader("Most Clearances")
        fig = plt.figure(figsize = (15, 10))
        name = df_def['name']
        clear = df_def['clearances'] 
        # creating the bar plot
        plt.bar(name,clear,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Clearances",fontsize = 15)
        plt.title("Most Clearances",fontsize = 15)
        st.pyplot()
    if graph == "Most Interceptions":
        df_def = df_def.sort_values(by=['interceptions'],ascending = False)
        col = ['full name','club','interceptions']
        st.table(df_def[col])
        st.subheader("Most Interceptions")
        fig = plt.figure(figsize = (15,10))
        name = df_def['name']
        inter = df_def['interceptions'] 
        # creating the bar plot
        plt.bar(name,inter,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("interceptions",fontsize = 15)
        plt.title("Most Interceptions",fontsize = 15)
        st.pyplot()
    if graph == "Most Tackles":
        df_def = df_def.sort_values(by=['tackles'],ascending = False)
        col = ['full name','club','tackles']
        st.table(df_def[col])
        st.subheader("Most Tackles")
        fig = plt.figure(figsize = (15,10))
        name = df_def['name']
        tackle = df_def['tackles'] 
        # creating the bar plot
        plt.bar(name,tackle,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("tackles",fontsize = 15)
        plt.title("Most Tackles",fontsize = 15)
        st.pyplot()    
    if graph == "Most Blocks":
        df_def = df_def.sort_values(by=['blocks'],ascending = False)
        col = ['full name','club','blocks']
        st.table(df_def[col])
        st.subheader("Most Blocks")
        fig = plt.figure(figsize = (15,10))
        name = df_def['name']
        block = df_def['blocks'] 
        # creating the bar plot
        plt.bar(name,block,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("blocks",fontsize = 15)
        plt.title("Most Blocks",fontsize = 15)
        st.pyplot()
    if graph == "Least fouls committed":
        df_def = df_def.sort_values(by=['fouls'])
        col = ['full name','club','fouls']
        st.table(df_def[col])
        st.subheader("Least fouls committed")
        fig = plt.figure(figsize = (15,10))
        name = df_def['name']
        foul = df_def['fouls'] 
        # creating the bar plot
        plt.bar(name,foul,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("fouls",fontsize = 15)
        plt.title("Least fouls committed",fontsize = 15)
        st.pyplot()    
    st.subheader("Stats comparison")
    player1 = st.selectbox("Choose defenders you want to compare",['Sandesh Jhingan','Odei Onaindia','Lalchungnunga','Brendan Hamill','Anwar Ali','Mourtada Fall','Mehtab Singh','Carlos Delgado','Pratik Chaudhari','Aaron Evans'])
    player2 = st.selectbox("",['Sandesh Jhingan','Odei Onaindia','Lalchungnunga','Brendan Hamill','Anwar Ali','Mourtada Fall','Mehtab Singh','Carlos Delgado','Pratik Chaudhari','Aaron Evans'])
    if player1 == player2:
        st.error("Please compare between different players")     
    else:
        # Initiate the plotly go figure
        fig = go.Figure()
        # Add Radar plots for different players:
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_def.loc[(per_90_data_def["full name"] == player1), cols_for_radar_def].sum(),
        theta=cols_for_radar_def,fill='toself',name=player1))
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_def.loc[(per_90_data_def["full name"] == player2), cols_for_radar_def].sum(),
        theta=cols_for_radar_def,fill='toself',name=player2))

        # Additional properties for the plot:
        fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
        polar=dict(radialaxis=dict(visible=True,)),
        showlegend=True)
        st.write(fig)
if nav == "Midfeilders Analysis":
    st.header("Top Midfielders of the season")
    #st.table(data)
    st.subheader("Select Analysis")
    graph = st.selectbox("Pick from the list below",["Most Assists","Most Goals",
    "Highest goal conversion rate","Most Crosses","Most Chances created","Most Passes",])
    if graph == "Most Assists":
        df_mid = df_mid.sort_values(by=['assists'],ascending=False)        
        col = ['full name','club','assists']
        st.table(df_mid[col])
        st.subheader("Most Assists")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        assist = df_mid['assists'] 
        # creating the bar plot
        plt.bar(name,assist,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Assists",fontsize = 15)
        plt.title("Most Assists",fontsize = 15)
        st.pyplot()
    if graph == "Most Goals":
        df_mid = df_mid.sort_values(by=['goals'],ascending=False)
        col = ['full name','club','goals']
        st.table(df_mid[col])
        st.subheader("Most Goals")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        goal = df_mid['goals'] 
        # creating the bar plot
        plt.bar(name,goal,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Goals",fontsize = 15)
        plt.title("Most Goals",fontsize = 15)
        st.pyplot()
    if graph == "Highest goal conversion rate":
        df_mid = df_mid.sort_values(by=['goal conversion rate'],ascending=False)
        
        st.subheader("Highest goal conversion rate")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        goal_con = df_mid['goal conversion rate'] 
        # creating the bar plot
        plt.bar(name,goal_con,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("goal conversion rate",fontsize = 15)
        plt.title("Highest goal conversion rate",fontsize = 15)
        st.pyplot()
    if graph == "Most Crosses":
        df_mid = df_mid.sort_values(by=['crosses'],ascending=False)
        col = ['full name','club','crosses']
        st.table(df_mid[col])
        st.subheader("Most Crosses")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        cr = df_mid['crosses'] 
        # creating the bar plot
        plt.bar(name,cr,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("crosses",fontsize = 15)
        plt.title("Most Crosses",fontsize = 15)
        st.pyplot()
    if graph == "Most Chances created":
        df_mid = df_mid.sort_values(by=['chances created'],ascending=False)        
        col = ['full name','club','chances created']
        st.table(df_mid[col])
        st.subheader("Most Chances created")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        ch = df_mid['chances created'] 
        # creating the bar plot
        plt.bar(name,ch,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Chances created",fontsize = 15)
        plt.title("Most Chances created",fontsize = 15)
        st.pyplot()
    if graph == "Most Passes":
        df_mid = df_mid.sort_values(by=['passes'],ascending=False)
        col = ['full name','club','passes']
        st.table(df_mid[col])
        st.subheader("Most Crosses")
        fig = plt.figure(figsize = (15,10))
        name = df_mid['name']
        pa = df_mid['passes'] 
        # creating the bar plot
        plt.bar(name,pa,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("passes",fontsize = 15)
        plt.title("Most Passes",fontsize = 15)
        st.pyplot()
    st.subheader("Stats comparison")
    player1 = st.selectbox("Choose midfielders you want to compare",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'])
    player2 = st.selectbox("",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'])
    if player1 == player2:
        st.error("Please compare between different players")     
    else:
        # Initiate the plotly go figure
        fig = go.Figure()
        # Add Radar plots for different players:
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_mid.loc[(per_90_data_mid["full name"] == player1), cols_for_radar_mid].sum(),
        theta=cols_for_radar_mid,fill='toself',name=player1))
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_mid.loc[(per_90_data_mid["full name"] == player2), cols_for_radar_mid].sum(),
        theta=cols_for_radar_mid,fill='toself', name=player2))

        # Additional properties for the plot:
        fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
        polar=dict(radialaxis=dict(visible=True,)),showlegend=True)
        st.write(fig)
if nav == "Strikers Analysis":
    st.header("Top Strikers of the season")
    #st.table(data)
    st.subheader("Select Analysis")
    graph = st.selectbox("Pick from the list below",["Most Goals","Most Assists","Most Shots",
    "Most Chances created","Most Passes"])
    if graph == "Most Goals":
        df_fwd = df_fwd.sort_values(by=['goals'],ascending=False)        
        col = ['full name','club','goals']
        st.table(df_fwd[col])
        st.subheader("Most Goals")
        fig = plt.figure(figsize = (15,10))
        name = df_fwd['name']
        g0 = df_fwd['goals'] 
        # creating the bar plot
        plt.bar(name,g0,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Goals",fontsize = 15)
        plt.title("Most Goals",fontsize = 15)
        st.pyplot()
    if graph == "Most Assists":
        df_fwd = df_fwd.sort_values(by=['assists'],ascending=False)        
        st.subheader("Most Assists")
        col = ['full name','club','assists']
        st.table(df_fwd[col])
        fig = plt.figure(figsize = (15,10))
        name = df_fwd['name']
        assist = df_fwd['assists'] 
        # creating the bar plot
        plt.bar(name,assist,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Assists",fontsize = 15)
        plt.title("Most Assists",fontsize = 15)
        st.pyplot()
    if graph == "Most Shots":
        df_fwd = df_fwd.sort_values(by=['shots'],ascending=False)        
        col = ['full name','club','shots']
        st.table(df_fwd[col])
        st.subheader("Most Shots")
        fig = plt.figure(figsize = (15,10))
        name = df_fwd['name']
        sht = df_fwd['shots'] 
        # creating the bar plot
        plt.bar(name,sht,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Shots",fontsize = 15)
        plt.title("Most Shots",fontsize = 15)
        st.pyplot()
    if graph == "Most Chances created":
        df_fwd = df_fwd.sort_values(by=['chances created'],ascending=False)        
        col = ['full name','club','chances created']
        st.table(df_fwd[col])
        st.subheader("Most Chances created")
        fig = plt.figure(figsize = (15,10))
        name = df_fwd['name']
        chn = df_fwd['chances created'] 
        # creating the bar plot
        plt.bar(name,chn,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Chances created",fontsize = 15)
        plt.title("Most Chances created",fontsize = 15)
        st.pyplot()
    if graph == "Most Passes":
        df_fwd = df_fwd.sort_values(by=['passes'],ascending=False)        
        col = ['full name','club','passes']
        st.table(df_fwd[col])
        st.subheader("Most Passes")
        fig = plt.figure(figsize = (15,10))
        name = df_fwd['name']
        p = df_fwd['passes'] 
        # creating the bar plot
        plt.bar(name,p,color = 'navy',edgecolor='red',linewidth = 1)
        matplotlib.rcParams.update({'font.size': 250})
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.ylim(0)
        plt.xlabel("Players",fontsize = 15)
        plt.ylabel("Passes",fontsize = 15)
        plt.title("Most Passes",fontsize = 15)
        st.pyplot()
    st.subheader("Stats comparison")
    player1 = st.selectbox("Choose strikers you want to compare",['Diego Mauricio',
 'Cleiton Silva',
 'Dimitri Petratos',
 'Jorge Diaz',
 'Bartholomew Ogbeche',
 'Dimitrios Diamantakos',
 'Lallianzuala Chhangte',
 'Wilmar Gil',
 'Greg Stewart',
 'Naorem Singh',
 'Roy Krishna',
 'Harry Sawyer',
 'Sunil Chhetri'])
    player2 = st.selectbox("",['Diego Mauricio',
 'Cleiton Silva',
 'Dimitri Petratos',
 'Jorge Diaz',
 'Bartholomew Ogbeche',
 'Dimitrios Diamantakos',
 'Lallianzuala Chhangte',
 'Wilmar Gil',
 'Greg Stewart',
 'Naorem Singh',
 'Roy Krishna',
 'Harry Sawyer',
 'Sunil Chhetri'])
    if player1 == player2:
        st.error("Please compare between different players")     
    else:
        # Initiate the plotly go figure
        fig = go.Figure()
        # Add Radar plots for different players:
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_fwd.loc[(per_90_data_fwd["full name"] == player1), cols_for_radar_fwd].sum(),
        theta=cols_for_radar_fwd,fill='toself',name=player1))
        fig.add_trace(go.Scatterpolar(
        r=per_90_data_fwd.loc[(per_90_data_fwd["full name"] == player2), cols_for_radar_fwd].sum(),
        theta=cols_for_radar_fwd,fill='toself', name=player2))

        # Additional properties for the plot:
        fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
        polar=dict(radialaxis=dict(visible=True,)),showlegend=True)
        st.write(fig)
if nav == "Create your own fantasy team":
    st.header("Create your fantasy team")
    st.subheader("You have a Total of 100 points. Make a team of 11 players from the list below. The value of each players are listed")
    #st.subheader("")
    name = st.text_input("Team name")
    
    form = st.selectbox("Select formation",["Select here","4-3-3","3-4-3","4-4-2"])
    points = 100
    eleven = 0
    if form == "4-3-3":
        players = []
        m0 = st.multiselect("Select Goalkeeper",['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.'], max_selections=1)
        st.write("Selected Players:",m0)
        if len(m0)>=1:
            x0 = ['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.']
            v0 = [8.5, 9.5, 9.0, 6.5, 7.0, 6.5, 9.0, 8.0, 7.5, 6.0]
            for i in range (0,10):
                for j in range (0,len(m0)):
                    if x0[i]==m0[j]:
                        points-=v0[i]
                        players.append(x0[i])
        st.write(f"Available Points: {points}")
         
        st.table(fan_gk)

        
        m1 = st.multiselect("Select Defenders",['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans'], max_selections=4)
        st.write("Selected Players:",m1)
        if len(m1)>=1:
            x1 = ['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans']
            v1 = [8.0, 8.0, 7.0, 7.5, 8.0, 7.5, 8.5, 7.0, 7.0, 6.5]
            for i in range (0,10):
                for j in range (0,len(m1)):
                    if x1[i]==m1[j]:
                        points-=v1[i]
                        players.append(x1[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_def)

        m2 = st.multiselect("Select Midfielders",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'], max_selections=3)
        st.write("Selected Players:",m2)
        if len(m2)>=1:
            x2 = ['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous']
            v2 = [8.5, 8.0, 8.5, 9.5, 9.5, 10.0, 10.0, 8.5, 8.5, 10.0, 9.5]
            for i in range (0,11):
                for j in range (0,len(m2)):
                    if x2[i]==m2[j]:
                        points-=v2[i]
                        players.append(x2[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_mid)
        
        m3 = st.multiselect("Select Forwards",['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri'], max_selections=3)
        st.write("Selected Players:",m3)
        if len(m3)>=1:
            x3 = ['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri']
            v3= [9.5, 10.5, 11.0, 9.5, 9.5, 9.5, 11.0, 8.5, 11.0, 8.5, 8.5, 7.0, 8.0]
            f = 0
            for i in range (0,13):
                for j in range (0,len(m3)):
                    if x3[i]==m3[j] and points>=0:
                        points-=v3[i]
                        players.append(x3[i])
                    elif points<0:
                        f = 1
            if f==1:
                st.error('Maximum Limit Exceeded')
                        
        st.write(f"Available Points: {points}") 
        st.table(fan_fwd)
        st.subheader(f"{name}:")
        
        st.table(players)
        eleven = len(players)
        st.write(eleven)
    if form == "3-4-3":
        players = []
        m0 = st.multiselect("Select Goalkeeper",['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.'], max_selections=1)
        st.write("Selected Players:",m0)
        if len(m0)>=1:
            x0 = ['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.']
            v0 = [8.5, 9.5, 9.0, 6.5, 7.0, 6.5, 9.0, 8.0, 7.5, 6.0]
            for i in range (0,10):
                for j in range (0,len(m0)):
                    if x0[i]==m0[j]:
                        points-=v0[i]
                        players.append(x0[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_gk)

        
        m1 = st.multiselect("Select Defenders",['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans'], max_selections=3)
        st.write("Selected Players:",m1)
        if len(m1)>=1:
            x1 = ['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans']
            v1 = [8.0, 8.0, 7.0, 7.5, 8.0, 7.5, 8.5, 7.0, 7.0, 6.5]
            for i in range (0,10):
                for j in range (0,len(m1)):
                    if x1[i]==m1[j]:
                        points-=v1[i]
                        players.append(x1[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_def)

        m2 = st.multiselect("Select Midfielders",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'], max_selections=4)
        st.write("Selected Players:",m2)
        if len(m2)>=1:
            x2 = ['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous']
            v2 = [8.5, 8.0, 8.5, 9.5, 9.5, 10.0, 10.0, 8.5, 8.5, 10.0, 9.5]
            for i in range (0,11):
                for j in range (0,len(m2)):
                    if x2[i]==m2[j]:
                        points-=v2[i]
                        players.append(x2[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_mid)
        
        m3 = st.multiselect("Select Forwards",['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri'], max_selections=3)
        st.write("Selected Players:",m3)
        if len(m3)>=1:
            x3 = ['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri']
            v3= [9.5, 10.5, 11.0, 9.5, 9.5, 9.5, 11.0, 8.5, 11.0, 8.5, 8.5, 7.0, 8.0]
            for i in range (0,13):
                for j in range (0,len(m3)):
                    if x3[i]==m3[j]:
                        points-=v3[i]
                        players.append(x3[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_fwd)
        st.subheader(f"{name}:")
        st.table(players)
        eleven = len(players)
        st.write(eleven)
    if form == "4-4-2":
        players = []
        m0 = st.multiselect("Select Goalkeeper",['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.'], max_selections=1)
        st.write("Selected Players:",m0)
        if len(m0)>=1:
            x0 = ['Gurpreet S.',
 'V.Kaith',
 'P.Lachenpa',
 'M.Michu',
 'Amrinder S.',
 'Kamaljit S.',
 'Gurmeet S.',
 'PS.Gill',
 'Dheeraj M.',
 'Arindam B.']
            v0 = [8.5, 9.5, 9.0, 6.5, 7.0, 6.5, 9.0, 8.0, 7.5, 6.0]
            for i in range (0,10):
                for j in range (0,len(m0)):
                    if x0[i]==m0[j]:
                        points-=v0[i]
                        players.append(x0[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_gk)

        
        m1 = st.multiselect("Select Defenders",['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans'], max_selections=4)
        st.write("Selected Players:",m1)
        if len(m1)>=1:
            x1 = ['Sandesh Jhingan',
 'Odei Onaindia',
 'Lalchungnunga',
 'Brendan Hamill',
 'Anwar Ali',
 'Mourtada Fall',
 'Mehtab Singh',
 'Carlos Delgado',
 'Pratik Chaudhari',
 'Aaron Evans']
            v1 = [8.0, 8.0, 7.0, 7.5, 8.0, 7.5, 8.5, 7.0, 7.0, 6.5]
            for i in range (0,10):
                for j in range (0,len(m1)):
                    if x1[i]==m1[j]:
                        points-=v1[i]
                        players.append(x1[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_def)

        m2 = st.multiselect("Select Midfielders",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'], max_selections=4)
        st.write("Selected Players:",m2)
        if len(m2)>=1:
            x2 = ['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous']
            v2 = [8.5, 8.0, 8.5, 9.5, 9.5, 10.0, 10.0, 8.5, 8.5, 10.0, 9.5]
            for i in range (0,11):
                for j in range (0,len(m2)):
                    if x2[i]==m2[j]:
                        points-=v2[i]
                        players.append(x2[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_mid)
        
        m3 = st.multiselect("Select Forwards",['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri'], max_selections=2)
        st.write("Selected Players:",m3)
        if len(m3)>=1:
            x3 = ['Diego Mauricio','Cleiton Silva','Dimitri Petratos', 'Jorge Diaz',
 'Bartholomew Ogbeche', 'Dimitrios Diamantakos','Lallianzuala Chhangte','Wilmar Gil',
 'Greg Stewart','Naorem Singh','Roy Krishna','Harry Sawyer','Sunil Chhetri']
            v3= [9.5, 10.5, 11.0, 9.5, 9.5, 9.5, 11.0, 8.5, 11.0, 8.5, 8.5, 7.0, 8.0]
            for i in range (0,13):
                for j in range (0,len(m3)):
                    if x3[i]==m3[j]:
                        points-=v3[i]
                        players.append(x3[i])
        st.write(f"Available Points: {points}") 
        st.table(fan_fwd)
        st.subheader(f"{name}:")
        st.table(players)
        eleven = len(players)
        st.write(eleven)
    if eleven != 11 and form !="Select here":
        st.error("Team Not Complete")
    if eleven ==11:
        st.success("You have created your Fantasy team")
    nav3 = st.selectbox("Compare Your Players",["Goalkeeper","Defenders","Midfielders","Strikers"])
    if nav3 == 'Goalkeeper' and eleven == 11:
        st.subheader("Stats comparison")
        player1 = st.selectbox("Choose goalkeepers you want to compare",["Gurpreet Sandhu","Vishal Kaith","Phurba Lachenpa","Mirshad Michu","Amrinder Singh","Kamaljit Singh","Gurmeet Singh","Prabhsukhan Gill","Dheeraj Moirangthem","Arindam Bhattacharja"])
        player2 = st.selectbox("",["Gurpreet Sandhu","Vishal Kaith","Phurba Lachenpa","Mirshad Michu","Amrinder Singh","Kamaljit Singh","Gurmeet Singh","Prabhsukhan Gill","Dheeraj Moirangthem","Arindam Bhattacharja"])
        if player1 == player2:
            st.error("Please compare between different players")     
        else:
            # Initiate the plotly go figure
            fig = go.Figure()
            # Add Radar plots for different players:
            fig.add_trace(go.Scatterpolar(r=per_90_data.loc[(per_90_data["full name"] == player1),
            cols_for_radar].sum(),theta=cols_for_radar,fill='toself',name=player1))
            fig.add_trace(go.Scatterpolar(r=per_90_data.loc[(per_90_data["full name"] == player2), 
            cols_for_radar].sum(),theta=cols_for_radar,fill='toself',name=player2))
            # Additional properties for the plot:
            fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",polar=dict(radialaxis=dict(
            visible=True,)),showlegend=True)
            st.write(fig)
    if nav3 == 'Defenders' and eleven == 11:
        st.subheader("Stats comparison")
        player1 = st.selectbox("Choose defenders you want to compare",['Sandesh Jhingan','Odei Onaindia','Lalchungnunga','Brendan Hamill','Anwar Ali','Mourtada Fall','Mehtab Singh','Carlos Delgado','Pratik Chaudhari','Aaron Evans'])
        player2 = st.selectbox("",['Sandesh Jhingan','Odei Onaindia','Lalchungnunga','Brendan Hamill','Anwar Ali','Mourtada Fall','Mehtab Singh','Carlos Delgado','Pratik Chaudhari','Aaron Evans'])
        if player1 == player2:
            st.error("Please compare between different players")     
        else:
            # Initiate the plotly go figure
            fig = go.Figure()
            # Add Radar plots for different players:
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_def.loc[(per_90_data_def["full name"] == player1), cols_for_radar_def].sum(),
            theta=cols_for_radar_def,fill='toself',name=player1))
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_def.loc[(per_90_data_def["full name"] == player2), cols_for_radar_def].sum(),
            theta=cols_for_radar_def,fill='toself',name=player2))

            # Additional properties for the plot:
            fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
            polar=dict(radialaxis=dict(visible=True,)),
            showlegend=True)
            st.write(fig)
    if nav3 == 'Midfielders' and eleven == 11:
        st.subheader("Stats comparison")
        player1 = st.selectbox("Choose midfielders you want to compare",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'])
        player2 = st.selectbox("",['Carl McHugh',
 'Sahal Samad',
 'Anirudh Thapa',
 'Iker Guarrotxena',
 'Abdenasser El Khayati',
 'Noah Wail Sadaoi',
 'Javier Hernandez',
 'Halicharan Narzary',
 'Borja Herrera',
 'Adrian Luna',
 'Hugo Boumous'])
        if player1 == player2:
            st.error("Please compare between different players")     
        else:
            # Initiate the plotly go figure
            fig = go.Figure()
            # Add Radar plots for different players:
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_mid.loc[(per_90_data_mid["full name"] == player1), cols_for_radar_mid].sum(),
            theta=cols_for_radar_mid,fill='toself',name=player1))
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_mid.loc[(per_90_data_mid["full name"] == player2), cols_for_radar_mid].sum(),
            theta=cols_for_radar_mid,fill='toself', name=player2))

            # Additional properties for the plot:
            fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
            polar=dict(radialaxis=dict(visible=True,)),showlegend=True)
            st.write(fig)
    if nav3 == 'Strikers' and eleven == 11:
        st.subheader("Stats comparison")
        player1 = st.selectbox("Choose strikers you want to compare",['Diego Mauricio',
 'Cleiton Silva',
 'Dimitri Petratos',
 'Jorge Diaz',
 'Bartholomew Ogbeche',
 'Dimitrios Diamantakos',
 'Lallianzuala Chhangte',
 'Wilmar Gil',
 'Greg Stewart',
 'Naorem Singh',
 'Roy Krishna',
 'Harry Sawyer',
 'Sunil Chhetri'])
        player2 = st.selectbox("",['Diego Mauricio',
 'Cleiton Silva',
 'Dimitri Petratos',
 'Jorge Diaz',
 'Bartholomew Ogbeche',
 'Dimitrios Diamantakos',
 'Lallianzuala Chhangte',
 'Wilmar Gil',
 'Greg Stewart',
 'Naorem Singh',
 'Roy Krishna',
 'Harry Sawyer',
 'Sunil Chhetri'])
        if player1 == player2:
            st.error("Please compare between different players")     
        else:
            # Initiate the plotly go figure
            fig = go.Figure()
            # Add Radar plots for different players:
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_fwd.loc[(per_90_data_fwd["full name"] == player1), cols_for_radar_fwd].sum(),
            theta=cols_for_radar_fwd,fill='toself',name=player1))
            fig.add_trace(go.Scatterpolar(
            r=per_90_data_fwd.loc[(per_90_data_fwd["full name"] == player2), cols_for_radar_fwd].sum(),
            theta=cols_for_radar_fwd,fill='toself', name=player2))

            # Additional properties for the plot:
            fig.update_layout(title=f"{player1} vs {player2} ISL 2022-23 analysis",
            polar=dict(radialaxis=dict(visible=True,)),showlegend=True)
            st.write(fig)
    if eleven != 11 :
        st.error("Please complete your Team")
if nav == "About Us":
    st.header("About Us")
    ima = ["arko.png","kushal.png"]
    st.image(ima, width = 300)
    st.markdown(" ### Created by Arkoprovo Ghosh and Kushal Nandi")
    st.subheader("Linkedin Profiles")
    st.write("Arkoprovo Ghosh : [Click here](https://www.linkedin.com/in/arkoprovo-ghosh-36137a206/)")
    st.write("Kushal Nandi : [Click here](https://www.linkedin.com/in/kushal-nandi-982459221/)")
st.sidebar.subheader('Season Team-wise Analysis')
nav2 = st.sidebar.selectbox('Select below', ('Select here','Final Season Standings', 'Fairplay Table'))

if nav2 == "Final Season Standings":
    st.header("Final ISL Season Standings 2022-23")
    st.image('stand.png')
if nav2 == "Fairplay Table":
    st.header("Final ISL Season Fairplay Standings")
    st.image('fairplay.png')

st.sidebar.markdown('''



---
Created by [Arkoprovo Ghosh](https://github.com/Arkoprovo08)
''')