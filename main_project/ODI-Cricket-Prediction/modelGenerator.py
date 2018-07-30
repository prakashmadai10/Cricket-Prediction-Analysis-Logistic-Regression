from collections import defaultdict

import pandas as pd
import  _pickle as pk
from main_project.LogisticReg import LogisticRegressionDemo
import numpy as np
#
def Venue_Changes(teamA, teamB, venue):  # venue is changed to 1 for teamA, -1 for teamB and 0 for no team.
    d = defaultdict(list)  # creates empty list,if list doesnot exists
    country = ''
    print(venue)
    with open('stadium/stadiums', 'r') as f:
        lines = f.read().splitlines()
        length = len(lines)
        i = 0
        while i < length:
            line = lines[i]
            if line == '$':
                country = lines[i + 1]
                i += 1
            else:
                d[country].append(line)
                i += 1

    if venue in (d['Australia']) or venue in (d['Bangladesh']) or venue in (d['England']) or venue in (
    d['India']) or venue in (d['New Zealand']) or venue in (d['Pakistan']) or venue in (d['South Africa']) or venue in (
    d['Sri Lanka']) or venue in (d['West Indies']) or venue in (d['Zimbabwe']):
        if venue in (d[teamA]):
            return 1
        if venue in (d[teamB]):
            return -1
    else:
        return 2
    return 0


def Toss_Changes(teamA, teamB, Toss):
    if Toss == teamA:
        return 1
    return 0


def Toss_Decision_Changes(Toss, Toss_Decision):
    if (((Toss == 1) & (Toss_Decision == 'bat')) or ((Toss == 0) & (Toss_Decision == 'field'))):
        return 1
    return 0


def Win_Prob_Of_TeamA(df, teamA, teamB):
    # playOffAandB=df[((df['TeamA']==teamA)&(df['TeamB']==teamB) | (df['TeamA']==teamB)&(df['TeamB']==teamA))]
    #
    playOffAandB = df.sort_values(by='Date', ascending=[0])
    # print(playOffAandB)
    # playOffAandB = playOffAandB.head(10)

    Awin = playOffAandB[(playOffAandB['Winner'] == 1)]
    a = len(Awin)
    p = len(playOffAandB)

    if p == 0:
        return 0
    return a / p


def Win_prob_on_venue(df1, venue, Toss_Decision):
    prevMatches = df1[(df1['Venue'] == venue)]#takes data on that venue
    #print(prevMatches)
    prevMatches = prevMatches.sort_values(by='Date', ascending=[0])
    # prevMatches = prevMatches.head(10)

    #print(prevMatches)

    if Toss_Decision == 1:#team1 won the and choose the bat first
        Awin = prevMatches[(prevMatches['Toss_Decision'] == prevMatches['Winner'])]
        #print(Awin)
    else:
        Awin = prevMatches[(prevMatches['Toss_Decision'] != prevMatches['Winner'])]

    #print(Awin.head())
    a = len(Awin)
    p = len(prevMatches)

    if p == 0:
        return 0
    return a / p


def strength_based_on_batBowl_avg(df, TeamA, TeamB):
    playOffAandB=df[((df['TeamA']==TeamA) & (df['TeamB']==TeamB) | (df['TeamA']==TeamB) & (df['TeamB']==TeamA))]
    playOffAandB = playOffAandB.sort_values(by='Date', ascending=[0])

    playOffAandB = playOffAandB['Strength'].iloc[0]
    #print(playOffAandB)

    return playOffAandB


def pastPerformance(df1, teamA, teamB, bat_avg):
    prevA = df1[((df1['TeamA'] == teamA) | (df1['TeamB'] == teamA))]
    #print(prevA)
    prevA = prevA.sort_values(by='Date', ascending=[0])
    prevA = prevA.head(10)

    form_A = 0
    cntA = 0
    for index, row in prevA.iterrows():
        name = str(row['MatchID']) + '.csv'  # "657643" #657645
        #print(name)
        df = pd.read_csv("Dataset/PlayerInfo/" + name)
        df['Bat_Avg'] = df['Bat_Avg'].replace('-', bat_avg)

        total_A = 0
        cntA = cntA + 1
        team_list = df[(df['Country'] == teamA)]
        for index1, row1 in team_list.iterrows():
            total_A = total_A + float(row1['Bat_Avg'])
        form_A = form_A + total_A / 11

    prevB = df1[((df1['TeamA'] == teamB) | (df1['TeamB'] == teamB))]
    prevB = prevB.sort_values(by='Date', ascending=[0])
    prevB = prevB.head(10)

    form_B = 0
    cntB = 0
    for index, row in prevB.iterrows():
        name = str(row['MatchID']) + '.csv'  # "657643" #657645
        df = pd.read_csv("Dataset/PlayerInfo/" + name)
        df['Bat_Avg'] = df['Bat_Avg'].replace('-', bat_avg)
        total_B = 0
        cntB = cntB + 1
        team_list = df[(df['Country'] == teamB)]
        for index1, row1 in team_list.iterrows():
            total_B = total_B + float(row1['Bat_Avg'])
        form_B = form_B + total_B / 11

    # print form_A, form_B, df1.loc[i, 'MatchID']
    if cntA == 0:
        cntA = 1
        formA = bat_avg
    if cntB == 0:
        cntB = 1
        formB = bat_avg
    return form_A / cntA - form_B / cntB

def testPredict(df1, testData, TeamA, TeamB):
    df1 = df1[((df1['TeamA']==TeamA)&(df1['TeamB']==TeamB) | (df1['TeamA']==TeamB)&(df1['TeamB']==TeamA))]
    predictors = ['Toss', 'Toss_Decision', 'Venue', 'HTH', 'WinningPerDes', 'Strength', 'latest_form']
    alg = LogisticRegressionDemo(lr=0.1, num_iter=1000)

    df = df1[['Toss', 'Toss_Decision', 'Venue', 'HTH', 'WinningPerDes', 'Strength', 'latest_form', 'Winner']]
    train_predictors = (df[predictors])
    train_target = df["Winner"]
    alg.fit(train_predictors, train_target)

    with open('my_dumped_classifier.pkl', 'wb') as fid:
       pk.dump(alg, fid)

        # load it again
    with open('my_dumped_classifier.pkl', 'rb') as fid:
        alg = pk.load(fid)

    test_predictions = alg.predict(testData)
    #print(test_predictions[0])
    return test_predictions[0]


# main Function

def startPrediction(teamA_input, teamB_input, venue_input, toss_input, tossDecision_input):
    df = pd.read_csv('OutputOfAllModified.csv')
    if teamB_input < teamA_input:
        teamB_input, teamA_input = teamA_input, teamB_input

    TeamA = teamA_input
    TeamB = teamB_input
    Toss = toss_input
    Toss_Decision = tossDecision_input
    Venue = venue_input

    Venue = Venue_Changes(TeamA, TeamB, Venue)
    mad=''
    HTH=''
    WinningPerDes=''
    latest_form=''
    str12='a'

    if (Venue != 2):
        str12='b'
        Toss = Toss_Changes(TeamA, TeamB, Toss)#if team ais a toss winner then it will return 1
        Toss_Decision = Toss_Decision_Changes(Toss, Toss_Decision)#if team1 is toss winner and choose bat returns 1

        HTH = Win_Prob_Of_TeamA(df, TeamA, TeamB)
    # print(HTH)

        WinningPerDes = Win_prob_on_venue(df, Venue, Toss_Decision)
        #print(WinningPerDes)

        bat_avg = 22.6046511628
        # bowl_avg = 29.7670682731

        Strength = strength_based_on_batBowl_avg(df, TeamA, TeamB)
    # print(Strength)

        latest_form = pastPerformance(df, TeamA, TeamB, bat_avg)
    # print(latest_form)

        print("teamA : " + TeamA)
        print(" ")
        print("teamB :" + TeamB)
        print(" ")
        print("winning probability of TeamA based on HTH: " + str(HTH))
        print(" ")
        print("winning probability of Team batting first : " + str(WinningPerDes))
        print(" ")
        print("Latest Form: Team A Performance - Team B Performance : " + str(latest_form))
        print(" ")
        print("Stregth " + str(Strength))
        print(" ")
        print("Performance is calculated based on team's batting average")
        print(" ")
        dict = {'Toss': Toss, 'Toss_Decision': Toss_Decision, 'Venue': Venue, 'HTH': HTH, 'WinningPerDes': WinningPerDes,
            'Strength': Strength, 'latest_form': latest_form}

        testData = pd.DataFrame(dict, index=["result"])
    # print(testData)

        if testPredict(df, testData, TeamA, TeamB) == 1:
            mad=teamA_input
            #return teamA_input, str(HTH), str(WinningPerDes), str(latest_form)
        else:
            mad=teamB_input
        #return teamB_input, str(HTH), str(WinningPerDes), str(latest_form)

    return mad, str(HTH), str(WinningPerDes), str(latest_form),str12