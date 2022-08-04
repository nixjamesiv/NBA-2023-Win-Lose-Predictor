class PositionRanking:
    def __init__(self):
        self
    

    def positionRankDF(self, year_team_dict, year, team, position)
        rank_list = []
        exp_list = []
        for row in year_team_dict[(year,team)].index:
            if position == year_team_dict[(year,team)]["Pos"][row]:
                rank_list.append(year_team_dict[(year,team)]["rank"][row])
                exp_list.append(year_team_dict[(year,team)]["Exp"][row])
        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
        rank_exp_pd.sort_values(by="rank")
        return()

    def yearTeamCycle(self):
        # iterates through year and team to cycle through year_team data frames
        for year in years:
            for team in teams:
                # iterates through position to grab different positions in year_team[(year,team)] data frame
                for position in positions:
                    rank_list = []
                    exp_list = []
                    # outer if, elif, else chain takes into acount team name change
                    if team == "OKC" and year in [str(x) for x in range(2001,2009)]:
                        team1 = "SEA"
                        # cycles through year_team[(year,team1)] to find players of certain positions to rank them
                        for row in year_team[(year,team1)].index:
                            if position == year_team[(year,team1)]["Pos"][row]:
                                rank_list.append(year_team[(year,team1)]["rank"][row])
                                exp_list.append(year_team[(year,team1)]["Exp"][row])
                        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                        rank_exp_pd.sort_values(by="rank")
                        # cycles through 1,2 to find given column
                        for num in range(1,3):
                            for pd_row in win_loss_df.index:
                                if team1 == win_loss_df["team"+str(num)][pd_row]:
                                    if year == win_loss_df["game_date"][pd_row]:
                                        print(year_team[(year,team1)], position)
                                        win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                        win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                        try:
                                            win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                            win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                        except:
                                            if position == "point-guard":
                                                position1 = "shooting-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "shooting-guard":
                                                position1 = "point-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "small-forward":
                                                position1 = "power-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "power-forward":
                                                position1 = "small-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            else:
                                                print("-------------------Cry---------------------")
                    elif team == "NOH" and year not in ["2003", "2004", "2005", "2008", "2009", "2010", "2011", "2012", "2013"]:
                        try:
                            if year in ["2006", "2007"]:
                                team1 = "NOK"
                                for row in year_team[(year,team1)].index:
                                    if position == year_team[(year,team1)]["Pos"][row]:
                                        rank_list.append(year_team[(year,team1)]["rank"][row])
                                        exp_list.append(year_team[(year,team1)]["Exp"][row])
                                rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                                rank_exp_pd.sort_values(by="rank")
                                for num in range(1,3):
                                    for pd_row in win_loss_df.index:
                                        if team1 == win_loss_df["team"+str(num)][pd_row]:
                                            if year == win_loss_df["game_date"][pd_row]:
                                                print(year_team[(year,team1)], position)
                                                win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                                win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                                try:
                                                    win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                                    win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                                except:
                                                    if position == "point-guard":
                                                        position1 = "shooting-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "shooting-guard":
                                                        position1 = "point-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "small-forward":
                                                        position1 = "power-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "power-forward":
                                                        position1 = "small-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    else:
                                                        print("-------------------Cry---------------------")
                            else:
                                team1 = "NOP"
                                for row in year_team[(year,team1)].index:
                                    if position == year_team[(year,team1)]["Pos"][row]:
                                        rank_list.append(year_team[(year,team1)]["rank"][row])
                                        exp_list.append(year_team[(year,team1)]["Exp"][row])
                                rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                                rank_exp_pd.sort_values(by="rank")
                                for num in range(1,3):
                                    for pd_row in win_loss_df.index:
                                        if team1 == win_loss_df["team"+str(num)][pd_row]:
                                            if year == win_loss_df["game_date"][pd_row]:
                                                print(year_team[(year,team1)], position)
                                                win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                                win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                                try:
                                                    win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                                    win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                                except:
                                                    if position == "point-guard":
                                                        position1 = "shooting-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "shooting-guard":
                                                        position1 = "point-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "small-forward":
                                                        position1 = "power-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "power-forward":
                                                        position1 = "small-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    else:
                                                        print("-------------------Cry---------------------")
                        except:
                            continue

                    elif team == "MEM" and year == "2001":
                        team1 = "VAN"
                        for row in year_team[(year,team1)].index:
                            if position == year_team[(year,team1)]["Pos"][row]:
                                rank_list.append(year_team[(year,team1)]["rank"][row])
                                exp_list.append(year_team[(year,team1)]["Exp"][row])
                        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                        rank_exp_pd.sort_values(by="rank")
                        for num in range(1,3):
                            for pd_row in win_loss_df.index:
                                if team1 == win_loss_df["team"+str(num)][pd_row]:
                                    if year == win_loss_df["game_date"][pd_row]:
                                        print(year_team[(year,team1)], position)
                                        win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                        win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                        try:
                                            win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                            win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                        except:
                                            if position == "point-guard":
                                                position1 = "shooting-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "shooting-guard":
                                                position1 = "point-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "small-forward":
                                                position1 = "power-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "power-forward":
                                                position1 = "small-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            else:
                                                print("-------------------Cry---------------------")
                    elif team == "CHA" and year in ["2001", "2002", "2003", "2004"] or year in [str(x) for x in range(2015,2023)]:
                        try:
                            if year in [str(x) for x in range(2015,2023)]:
                                team1 = "CHO"
                                for row in year_team[(year,team1)].index:
                                    if position == year_team[(year,team1)]["Pos"][row]:
                                        rank_list.append(year_team[(year,team1)]["rank"][row])
                                        exp_list.append(year_team[(year,team1)]["Exp"][row])
                                rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                                rank_exp_pd.sort_values(by="rank")
                                for num in range(1,3):
                                    for pd_row in win_loss_df.index:
                                        if team1 == win_loss_df["team"+str(num)][pd_row]:
                                            if year == win_loss_df["game_date"][pd_row]:
                                                print(year_team[(year,team1)], position)
                                                win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                                win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                                try:
                                                    win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                                    win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                                except:
                                                    if position == "point-guard":
                                                        position1 = "shooting-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "shooting-guard":
                                                        position1 = "point-guard"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "small-forward":
                                                        position1 = "power-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    elif position == "power-forward":
                                                        position1 = "small-forward"
                                                        rank_list1 = []
                                                        exp_list1 = []
                                                        for row1 in year_team[(year,team1)].index:
                                                            if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                                rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                                exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                        rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                        rank_exp_pd1.sort_values(by="rank")
                                                        win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                        win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                                    else:
                                                        print("-------------------Cry---------------------")
                        except:
                            continue    

                    elif team == "NJN" and year in [str(x) for x in range(2013,2023)]:
                        team1 = "BRK"
                        for row in year_team[(year,team1)].index:
                            if position == year_team[(year,team1)]["Pos"][row]:
                                rank_list.append(year_team[(year,team1)]["rank"][row])
                                exp_list.append(year_team[(year,team1)]["Exp"][row])
                        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                        rank_exp_pd.sort_values(by="rank")
                        for num in range(1,3):
                            for pd_row in win_loss_df.index:
                                if team1 == win_loss_df["team"+str(num)][pd_row]:
                                    if year == win_loss_df["game_date"][pd_row]:
                                        print(year_team[(year,team1)], position)
                                        win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                        win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                        try:
                                            win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                            win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                        except:
                                            if position == "point-guard":
                                                position1 = "shooting-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "shooting-guard":
                                                position1 = "point-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "small-forward":
                                                position1 = "power-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "power-forward":
                                                position1 = "small-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team1)].index:
                                                    if position1 == year_team[(year,team1)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team1)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team1)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            else:
                                                print("-------------------Cry---------------------")
                    else:
                        for row in year_team[(year,team)].index:
                            if position == year_team[(year,team)]["Pos"][row]:
                                rank_list.append(year_team[(year,team)]["rank"][row])
                                exp_list.append(year_team[(year,team)]["Exp"][row])
                        rank_exp_pd = pd.DataFrame({"rank":rank_list,"exp":exp_list})
                        rank_exp_pd.sort_values(by="rank")
                        for num in range(1,3):
                            for pd_row in win_loss_df.index:
                                if team == win_loss_df["team"+str(num)][pd_row]:
                                    if year == win_loss_df["game_date"][pd_row]:
                                        print(year_team[(year,team)], position)
                                        win_loss_df["team"+str(num)+"-1-"+position][pd_row] = rank_exp_pd["rank"][0]
                                        win_loss_df["team"+str(num)+"-1-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][0]
                                        try:
                                            win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd["rank"][1]
                                            win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd["exp"][1]
                                        except:
                                            if position == "point-guard":
                                                position1 = "shooting-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team)].index:
                                                    if position1 == year_team[(year,team)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "shooting-guard":
                                                position1 = "point-guard"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team)].index:
                                                    if position1 == year_team[(year,team)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "small-forward":
                                                position1 = "power-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team)].index:
                                                    if position1 == year_team[(year,team)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            elif position == "power-forward":
                                                position1 = "small-forward"
                                                rank_list1 = []
                                                exp_list1 = []
                                                for row1 in year_team[(year,team)].index:
                                                    if position1 == year_team[(year,team)]["Pos"][row1]:
                                                        rank_list1.append(year_team[(year,team)]["rank"][row1])
                                                        exp_list1.append(year_team[(year,team)]["Exp"][row1])
                                                rank_exp_pd1 = pd.DataFrame({"rank":rank_list1,"exp":exp_list1})
                                                rank_exp_pd1.sort_values(by="rank")
                                                win_loss_df["team"+str(num)+"-2-"+position][pd_row] = rank_exp_pd1["rank"][2]
                                                win_loss_df["team"+str(num)+"-2-"+position+"-exp"][pd_row] = rank_exp_pd1["exp"][2]

                                            else:
                                                print("-------------------Cry---------------------")