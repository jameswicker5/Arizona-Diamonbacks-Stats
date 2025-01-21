import pandas as pd

class TeamStats:
    def __init__(self, data, salary, year=None):
        self.data = data
        self.year = year
        self.salary = salary
        if self.year:
            self.data = self.data[self.data['Year'] == self.year]
            self.salary = self.salary[self.salary['Year'] == self.year]

    def total_wins(self):
        return self.data['Wins'].sum()

    def total_losses(self):
        return self.data['Losses'].sum()

    def winning_percentage(self):
        total_wins = self.total_wins()
        total_losses = self.total_losses()
        if total_wins + total_losses == 0:
            return 0
        return total_wins / (total_wins + total_losses)

    def total_payroll(self):
        return self.salary['Salary'].sum()
            

    def display_stats(self):
        total_wins = self.total_wins()
        total_losses = self.total_losses()
        total_salary = self.total_payroll()
        year_str = f" for {self.year}" if self.year else " All Time"
        print(f'Total Wins{year_str}: {total_wins}')
        print(f'Total Losses{year_str}: {total_losses}')
        print(f'Winning Percentage{year_str}: {self.winning_percentage():.3f}')
        print(f'Total Payroll{year_str}: ${total_salary:,.2f}')

class TotalTeam:
    def __init__(self, bat, pitch, year=None):
        self.bat = bat
        self.year = year
        self.pitch = pitch
        if self.year:
            self.bat = self.bat[self.bat['Year'] == self.year]
            self.pitch = self.pitch[self.pitch['Year'] == self.year]       
        
    def total_team_stats(self):
        total_runs = self.bat['Runs'].sum()
        total_hits = self.bat['Hits'].sum()
        total_ab = self.bat['At_Bats'].sum()
        total_doubles = self.bat['Doubles'].sum()
        total_triples = self.bat['Triples'].sum()
        total_hr = self.bat['Home_Runs'].sum()
        total_rbi = self.bat['Runs_Batted_In'].sum()
        total_bb = self.bat['Base_On_Balls'].sum()
        total_so = self.bat['Strikeouts'].sum()
        total_sb = self.bat['Stolen_Bases'].sum()
        total_cs = self.bat['Caught_Stealing'].sum()
        total_hbp = self.bat['Times_Hit_By_Pitch'].sum()
        total_sf = self.bat['Sacrifice_Flies'].sum()
        sb_per = (total_sb / (total_sb + total_cs)) * 100
        total_ba = total_hits / total_ab
        total_obp = ((total_hits + total_bb + total_hbp) / (total_ab + total_bb + total_hbp + total_sf))
        total_slg = ((total_hits + total_doubles + total_triples * 2 + total_hr * 3) / total_ab)
        total_ops = total_obp + total_slg
        year_str = f" for {self.year}" if self.year else " All Time"
        print(f'Team Total At-Bats{year_str}: {total_ab}')
        print(f'Team Total Runs Scored{year_str}: {total_runs}')
        print(f'Team Total Hits{year_str}: {total_hits}')
        print(f'Team Total Doubles{year_str}: {total_doubles}')
        print(f'Team Total Triples{year_str}: {total_triples}')
        print(f'Team Total HRs{year_str}: {total_hr}')
        print(f'Team Total RBI\'s{year_str}: {total_rbi}')
        print(f'Team Total Walks{year_str}: {total_bb}')
        print(f'Team Total HBP{year_str}: {total_hbp}')
        print(f'Team Total Strikeouts{year_str}: {total_so}')
        print(f'Team Total Stolen Bases{year_str}: {total_sb}')
        print(f'Team Total Caught Stealing{year_str}: {total_cs}')
        print(f'Team Stolen Base Percentage{year_str}: {sb_per:.2f}%')
        print(f'Team Batting Average{year_str}: {total_ba:.3f}')
        print(f'Team Total OBP{year_str}: {total_obp:.3f}')
        print(f'Team Total Slugging Percentage{year_str}: {total_slg:.3f}')
        print(f'Team Total OPS{year_str}: {total_ops:.3f}')