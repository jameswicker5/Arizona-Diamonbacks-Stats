import numpy as np
import pandas as pd
class IndividualStats:
    def __init__(self, data, year=None):
        self.data = data
        self.year = year

    def get_player(self, name):
        return self.data[self.data['Name'] == name]

    def home_run_stats(self, name):
        player_data = self.get_player(name)
        tot_hr = player_data['Home_Runs'].sum()
        tot_ab = player_data['At_Bats'].sum()
        tot_games = player_data['Games'].sum()
        abhr = tot_ab / tot_hr
        print(f'{name} hit {tot_hr} home runs across {tot_games} games')
        print(f'He had {abhr:.2f} ABs per home run')

    def total_pitching_stats(self, name):
        player_data = self.get_player(name)
        avg_age = player_data['Age'].mean()
        years_played = player_data['Year'].nunique()
        tot_wins = player_data['Wins'].sum()
        tot_losses = player_data['Losses'].sum()
        tot_win_per = tot_wins / (tot_wins + tot_losses)
        tot_ip = player_data['Innings_Pitched'].sum()
        tot_er = player_data['Earned_Runs'].sum()
        tot_era = (tot_er / tot_ip) * 9
        tot_games = player_data['Games_Played'].sum()
        tot_games_started = player_data['Games_Started'].sum()
        tot_shutouts = player_data['Shutouts'].sum()
        tot_saves = player_data['Saves'].sum()
        tot_so = player_data['Strikeouts'].sum()
        tot_hbp = player_data['Hit_By_Pitch'].sum()
        tot_bat_faced = player_data['Batters_Faced'].sum()
        tot_wa = player_data['Walks_Allowed'].sum()
        tot_wp = player_data['Wild_Pitches'].sum()
        tot_balks = player_data['Balks'].sum()

        print(f'Player: {name}')
        print(f'Average Age: {avg_age:.2f}')
        print(f'Years Played: {years_played}')
        print(f'Total Wins: {tot_wins}')
        print(f'Total Losses: {tot_losses}')
        print(f'Winning Percentage: {tot_win_per:.3f}')
        print(f'Total Games: {tot_games}')
        print(f'Total Games Started: {tot_games_started}')
        print(f'Total Batters Faced: {tot_bat_faced}')
        print(f'Total Innings Pitched: {tot_ip:.1f}')
        print(f'Total Earned Runs: {tot_er}')
        print(f'Total Earned Run Average: {tot_era:.2f}')
        print(f'Total Shutouts: {tot_shutouts}')
        print(f'Total Saves: {tot_saves}')
        print(f'Total Strikeouts: {tot_so}')
        print(f'Total Hit By Pitch: {tot_hbp}')
        print(f'Total Walks Allowed: {tot_wa}')
        print(f'Total Wild Pitches: {tot_wp}')
        print(f'Total Balks: {tot_balks}')

    def total_hitting_stats(self, name):
        player_data = self.get_player(name)
        tot_hits = player_data['Hits'].sum()
        tot_hr = player_data['Home_Runs'].sum()
        tot_rbi = player_data['Runs_Batted_In'].sum()
        tot_2b = player_data['Doubles'].sum()
        tot_3b = player_data['Triples'].sum()
        tot_1b = player_data['Hits'].sum() - player_data['Doubles'].sum() - player_data['Triples'].sum() - player_data['Home_Runs'].sum()
        tot_ab = player_data['At_Bats'].sum()
        tot_games = player_data['Games'].sum()
        tot_so = player_data['Strikeouts'].sum()
        tot_bb = player_data['Base_On_Balls'].sum()
        tot_ab = player_data['At_Bats'].sum()
        tot_ba = tot_hits / tot_ab
        tot_sb = player_data['Stolen_Bases'].sum()
        tot_cs = player_data['Caught_Stealing'].sum()
        cs_per = tot_cs / (tot_cs + tot_sb)
        tot_hbp = player_data['Times_Hit_By_Pitch'].sum()
        tot_ibb = player_data['Intentional_Bases_on_Balls'].sum()
        tot_slug = (tot_hits + tot_2b + (2 * tot_3b) + (3 * tot_hr)) / tot_ab
        so_rate = tot_so / tot_ab
        bb_rate = tot_bb / tot_ab
        years_played = player_data['Year'].nunique()
        tot_sf = player_data['Sacrifice_Flies'].sum()
        tot_obp = (tot_hits + tot_bb + tot_hbp) / (tot_ab + tot_bb + tot_hbp + tot_sf)
        avg_age = player_data['Age'].mean()
        print(f'Player: {name}')
        print(f'Average Age: {avg_age}')
        print(f'Years Played: {years_played}')
        print(f'Total Games: {tot_games}')
        print(f'Total At-Bats: {tot_ab}')
        print(f'Total Batting Average: {tot_ba:.3f}')
        print(f'Total Hits: {tot_hits}')
        print(f'Total Home Runs: {tot_hr}')
        print(f'Total Runs Batted In: {tot_rbi}')
        print(f'Total Doubles: {tot_2b}')
        print(f'Total Triples: {tot_3b}')
        print(f'Total Singles: {tot_1b}')
        print(f'Total Strikeouts: {tot_so}')
        print(f'Total Walks: {tot_bb}')
        print(f'Total Stolen Bases: {tot_sb}')
        print(f'Total Caught Stealing: {tot_cs}')
        print(f'Caught Stealing Percentage: {cs_per:.3f}')
        print(f'Total Hit By Pitch: {tot_hbp}')
        print(f'Total Intentional Bases on Balls: {tot_ibb}')
        print(f'Total Slugging Percentage: {tot_slug:.3f}')
        print(f'Strikeout Rate: {so_rate:.3f}')
        print(f'Walk Rate: {bb_rate:.3f}')
        print(f'On-Base Percentage: {tot_obp:.3f}')