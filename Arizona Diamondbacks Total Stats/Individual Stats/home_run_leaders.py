import pandas as pd
import numpy as np

file_path_bat = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Batting_Updated.csv"
ari_bat = pd.read_csv(file_path_bat)

## Top Home Run Leaders
players = ari_bat['Name'].unique() # retrieve all unique names in ari_bat
player_hr_totals = {}  # Empty dictionary to append during calc.

for player in players:
    total_hr = ari_bat[ari_bat['Name'] == player]['Home_Runs'].sum()
    player_hr_totals[player] = total_hr # adding name and total hrs to dictionary

## transform dictionary to pandas Dataframe
hr_totals_df = pd.DataFrame(list(player_hr_totals.items()), columns=['Name', 'Total_HR\'s'])
hr_totals_df_sorted = hr_totals_df.sort_values(by='Total_HR\'s', ascending=False)

## Top 10 All Time
print(hr_totals_df_sorted.head(10))