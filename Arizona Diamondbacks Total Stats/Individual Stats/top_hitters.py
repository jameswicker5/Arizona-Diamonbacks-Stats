import pandas as pd
from individual_stats import IndividualStats

file_path_bat = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Batting_Updated.csv"
ari_bat = pd.read_csv(file_path_bat)
print(ari_bat)


## Luis Gonzalez
ari_lg = IndividualStats(ari_bat)
print('Luis Gonzalez')
ari_lg.get_player('Luis Gonzalez')
ari_lg.total_hitting_stats('Luis Gonzalez')
ari_lg.home_run_stats('Luis Gonzalez')
print()

## Steve Finley
ari_sf = IndividualStats(ari_bat)
print('Steve Finley')
ari_sf.get_player('Steve Finley')
ari_sf.total_hitting_stats('Steve Finley')
ari_sf.home_run_stats('Steve Finley')
print()

## Tony Womack
ari_tw = IndividualStats(ari_bat)
ari_tw.get_player('Tony Womack')
ari_tw.total_hitting_stats('Tony Womack')
ari_tw.home_run_stats('Tony Womack')
print()

## Matt Williams
ari_mw = IndividualStats(ari_bat)
ari_mw.get_player('Matt Williams')
ari_mw.total_hitting_stats('Matt Williams')
ari_mw.home_run_stats('Matt Williams')
print()

## Justin Upton
ari_ju = IndividualStats(ari_bat)
ari_ju.get_player('Justin Upton')
ari_ju.total_hitting_stats('Justin Upton')
ari_ju.home_run_stats('Justin Upton')
print()

## Paul Goldschmidt
ari_pg = IndividualStats(ari_bat)
ari_pg.get_player('Paul Goldschmidt')
ari_pg.total_hitting_stats('Paul Goldschmidt')
ari_pg.home_run_stats('Paul Goldschmidt')
print()

## Christian Walker
ari_cw = IndividualStats(ari_bat)
ari_cw.get_player('Christian Walker')
ari_cw.total_hitting_stats('Christian Walker')
ari_cw.home_run_stats('Christian Walker')
print()

## Ketel Marte
ari_km = IndividualStats(ari_bat)
ari_km.get_player('Ketel Marte')
ari_km.total_hitting_stats('Ketel Marte')
ari_km.home_run_stats('Ketel Marte')
print()

## Corbin Carroll
ari_cc = IndividualStats(ari_bat)
ari_cc.get_player('Corbin Carroll')
ari_cc.total_hitting_stats('Corbin Carroll')
ari_cc.home_run_stats('Corbin Carroll')
print()