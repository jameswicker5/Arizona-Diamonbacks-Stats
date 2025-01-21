import pandas as pd
from individual_stats import IndividualStats

file_path_pitch = r"C:\Users\james\OneDrive\Desktop\Portfolio\Arizona Diamondbacks Total Stats\ARI_Pitching_Updated.csv"

ari_pitch = pd.read_csv(file_path_pitch)

## Randy Johnson
ari_rj = IndividualStats(ari_pitch)
ari_rj.total_pitching_stats('Randy Johnson')
print()

## Curt Schilling
ari_cs = IndividualStats(ari_pitch)
ari_cs.total_pitching_stats('Curt Schilling')
print()

## Zack Greinke
ari_zg = IndividualStats(ari_pitch)
ari_zg.total_pitching_stats('Zack Greinke')
print()

## Brandon Webb
ari_bw = IndividualStats(ari_pitch)
ari_bw.total_pitching_stats('Brandon Webb')
print()

## Ian Kennedy
ari_ik = IndividualStats(ari_pitch)
ari_ik.total_pitching_stats('Ian Kennedy')
print()

## Zac Gallen
ari_zac_gal = IndividualStats(ari_pitch)
ari_zac_gal.total_pitching_stats('Zac Gallen')
print()

## Madison Bumgarner
ari_mb = IndividualStats(ari_pitch)
ari_mb. total_pitching_stats('Madison Bumgarner')
print()

## Patrick Corbin
ari_pc = IndividualStats(ari_pitch)
ari_pc.total_pitching_stats('Patrick Corbin')
print()

## Merrill Kelly
ari_mk = IndividualStats(ari_pitch)
ari_mk.total_pitching_stats('Merrill Kelly')
print()


