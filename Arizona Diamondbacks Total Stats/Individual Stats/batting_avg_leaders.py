import pandas as pd
import numpy as np
from individual_stats import IndividualStats

file_path_bat = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Batting_Updated.csv"
ari_bat = pd.read_csv(file_path_bat)
print(ari_bat)

## Top D-backs Batting Average Seasons (Min. 300 Plate Appearances)

top_bat_avg_szn = ari_bat.sort_values(by='Batting_Average', ascending=False)

## Index into top_bat_avg_szn with min. 300 PA
top_bat_avg_300 = top_bat_avg_szn[top_bat_avg_szn['Plate_Appearances'] >= 300]
print(top_bat_avg_300.head(10))
print(top_bat_avg_300['Batting_Average'].head(10))


## Min. 500 PA
top_bat_avg_500 = top_bat_avg_szn[top_bat_avg_szn['Plate_Appearances'] >= 500]
print(top_bat_avg_500.head(10))
print(top_bat_avg_500['Batting_Average'].head(10))

