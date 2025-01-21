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

ari_bat_2001 = ari_bat[ari_bat['Year'] == 2001]
ari_sal_2001 = ari_sal[ari_sal['Year'] == 2001]
ari_rec_2001 = ari_rec[ari_rec['Year'] == 2001]
ari_pitch_2001 = ari_pitch[ari_pitch['Year'] == 2001] 

## Record and Payroll
ari_2001_szn = TeamStats(ari_rec, ari_sal, year=2001)
ari_2001_szn.display_stats()
avg_sal_2001 = np.sum(ari_sal_2001['Salary']) / len(ari_sal_2001)
print(f'Average Salary in 2001: ${avg_sal_2001:,.2f}')
print()

## Top 5 Salaries
top_5_sal = ari_sal_2001.nlargest(5, 'Salary')
print(f'Top 5 Salaries 2001: \n{top_5_sal}')

## Payroll Spread (Visual)
salary_per_2001 = (ari_sal_2001['Salary'] / np.sum(ari_sal_2001['Salary'])) * 100
## 2% threshold for players who do not qualify (for visual purposes)
threshold = 2
threshold_salaries = ari_sal_2001[salary_per_2001 < threshold]['Salary'].sum()
threshold_per = (threshold_salaries / np.sum(ari_sal_2001['Salary'])) * 100
main_salaries = ari_sal_2001[salary_per_2001 >= threshold]

## labels and sizes for plot
labels = list(main_salaries['Name']) + ['Other']
sizes = list((main_salaries['Salary'] / np.sum(ari_sal_2001['Salary'])) * 100) + [threshold_per]


## Plot
plt.figure(figsize=(12,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('2001 Arizona Diamondbacks Salaries')
plt.legend(title="Player and Percentage", bbox_to_anchor=(1, 0.5), loc="center left")
plt.show()

# Team Batting Average
ari_team_stats_2001 = TotalTeam(ari_bat, ari_pitch, year=2001)
ari_team_stats_2001.total_team_stats()

