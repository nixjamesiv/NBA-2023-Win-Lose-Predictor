import pandas as pd
class PositionRanking:
    def __init__(self):
        self
    
    
    
    def positionRankDF(self, year_team_dict, year, team, position):
        rank_list = []
        exp_list = []
        #check each row in year_team_dict if position is position
        for row in year_team_dict[(year,team)].index:
            if position == year_team_dict[(year,team)]["Pos"][row]:
                rank_list.append(year_team_dict[(year,team)]["rank"][row])
                exp_list.append(year_team_dict[(year,team)]["Exp"][row])
        #creates rank pd
        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
        #ranks rank pd
        rank_exp_pd.sort_values(by="rank")
        return rank_exp_pd

    
    
    
    def positionRankDFFilter(self, year_team_dict, year, team, position):
        #rank lists/exp lists
        if team == "PHX":
            team1 = "PHO"
            return self.positionRankDF(year_team_dict=year_team_dict, year=year, team=team1, position=position)
        elif team == "BKN":
            team1 = "BRK"
            return self.positionRankDF(year_team_dict=year_team_dict, year=year, team=team1, position=position)
        else:
            return self.positionRankDF(year_team_dict, year, team, position)    

        
     
        
    def positionRanker(self, year, team, position, rank_exp_pd, year_team_dict, df):
        for num in range(1,3):
            for pd_row in df.index:
                if team == df["team"+str(num)][pd_row]:
                    if year == df["game_date"][pd_row]:
                        try:
                            # trys main position to give rank and exp
                            df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                            df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                        except:
                            for position1 in positions:
                                try:
                                    #trys different positions to grab from if there are not 1 of main positions
                                    rank_exp_pd1 = self.positionRankDFFilter(
                                        year_team_dict=year_team_dict, 
                                        year=year, team=team, 
                                        position=position1
                                    )
                                    df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                    df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]
                                    print("1 Success",position1,position)
                                    break
                                except:
                                    print("1 Fail",position1,position)
                        try:
                            # trys main position to give rank and exp
                            df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                            df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                        except:
                            #trys different positions to grab from if there are not 2 of main positions
                            for position1 in positions:
                                try:
                                    rank_exp_pd1 = self.positionRankDFFilter(
                                        year_team_dict=year_team_dict, 
                                        year=year, team=team, 
                                        position=position1
                                    )
                                    df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                    df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]
                                    print("2 Success",position1,position)
                                    break
                                except:
                                    print("2 Fail",position1,position)    
    
    
    
    def fullPositionRanker(self, year_team_dict, year, team, position, df):
        rank_exp_pd = self.positionRankDFFilter(year_team_dict=year_team_dict, year=year, team=team, position=position)
        if team == "PHO":
            team1 = "PHX"
            self.positionRanker(year=year, team=team1, position=position, rank_exp_pd=rank_exp_pd, year_team_dict=year_team_dict, df=df)
            #So the positionRanker works
        elif team == "BRK":
            team1 = "BKN"
            self.positionRanker(year=year, team=team1, position=position, rank_exp_pd=rank_exp_pd, year_team_dict=year_team_dict, df=df)
            #CHO change never actually happens in data
        elif team == "CHO":
            team1 = "CHA"
            self.positionRanker(year=year, team=team1, position=position, rank_exp_pd=rank_exp_pd, year_team_dict=year_team_dict, df=df)
        else:
            self.positionRanker(year=year, team=team, position=position, rank_exp_pd=rank_exp_pd, year_team_dict=year_team_dict, df=df)
    
    
    
    
    def yearTeamCycle(self, years, teams, year_team_dict, positions, df):
        for year in years:
            for team in teams:
                print("1")
                # iterates through position to grab different positions in year_team[(year,team)] data frame
                for position in positions:
                    print("2")
                    # outer if, elif, else chain takes into acount team name change
                    if team == "OKC" and year in [str(x) for x in range(2001,2009)]:
                        team1 = "SEA"
                        print("3")
                        # cycles through year_team[(year,team1)] to fin players of certain positions to rank them
                        self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                    #Team name change NOH
                    elif team == "NOH" and year not in ["2003", "2004", "2005", "2008", "2009", "2010", "2011", "2012", "2013"]:
                        try:
                            if year in ["2006", "2007"]:
                                team1 = "NOK"
                                print("4.1")
                                self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                            else:
                                team1 = "NOP"
                                print("4.2")
                                self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                        except:
                            pass
                    #Team name change MEM
                    elif team == "MEM" and year == "2001":
                        team1 = "VAN"
                        print("5")
                        self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                    #Team name change CHA
                    elif team == "CHA" and (year in ["2001", "2002", "2003", "2004"] or year in [str(x) for x in range(2015,2023)]):
                        try:
                            if year in [str(x) for x in range(2015,2023)]:
                                team1 = "CHO"
                                print("6.1")
                                self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                        except:
                            pass 
                        try:
                            if year in ["2001", "2002"]:
                                team1 = "CHH"
                                print("6.2")
                                self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                        except:
                            pass
                    #Team name change NJN
                    elif team == "NJN" and year in [str(x) for x in range(2013,2023)]:
                        team1 = "BRK"
                        print("7")
                        self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team1, position=position, df=df)
                    else:
                        print("8")
                        self.fullPositionRanker(year_team_dict=year_team_dict, year=year, team=team, position=position, df=df)
                    print(year,team)