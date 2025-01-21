import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from team_stats import TeamStats
file_path_bat = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Batting_Updated.csv"
ari_bat = pd.read_csv(file_path_bat)
print(ari_bat)


age_hits = ari_bat.groupby(['Year', 'Age'])['Hits'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.scatterplot(data=age_hits, x='Year', y='Age', size='Hits', sizes=(20, 200), hue='Hits', palette='plasma')
plt.xlabel('Year')
plt.ylabel('Age')
plt.title('Total Hits per Year by Age')
plt.show()
