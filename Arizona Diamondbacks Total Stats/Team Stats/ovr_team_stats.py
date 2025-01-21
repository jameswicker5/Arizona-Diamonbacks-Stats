import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from team_stats import TeamStats, TotalTeam



file_path_bat = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Batting_Updated.csv"
file_path_rec = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\Arizona_Record.csv"
file_path_sal = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\Arizona_Salaries.csv"
file_path_pitch = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Pitching_Updated.csv"

ari_bat = pd.read_csv(file_path_bat)
ari_pitch = pd.read_csv(file_path_pitch)
ari_rec = pd.read_csv(file_path_rec)
ari_sal = pd.read_csv(file_path_sal)

for year in ari_bat['Year'].unique():
    ari_szn = TeamStats(ari_rec, ari_sal, year=year)
    ari_szn.display_stats()
    print()

    ari_team_stats = TotalTeam(ari_bat, ari_pitch, year=year)
    ari_team_stats.total_team_stats()
    print()

