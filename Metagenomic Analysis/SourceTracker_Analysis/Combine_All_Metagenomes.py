# This script is written to merge METAGENOME csv files. Please edit the code for individual domains.

import pandas as pd

# read in csv files
ocean = pd.read_csv("ocean_OTU_metagenome.csv")
pacific = pd.read_csv("pacific_OTU_metagenome.csv")
wastewater = pd.read_csv("waste_OTU_metagenome.csv")
soil = pd.read_csv("soil_OTU_metagenome.csv")
fresh = pd.read_csv("fresh_OTU_metagenome.csv")
gut = pd.read_csv("gut_OTU_metagenome.csv")
TJ = pd.read_csv("TJ_OTU_metagenome.csv")

# merge all together
merged1 = ocean.merge(pacific, how='outer')
print(len(merged1.index))
merged2 = merged1.merge(wastewater, how='outer')
print(len(merged2.index))
merged3 = merged2.merge(fresh, how='outer')
print(len(merged3.index))
merged4 = merged3.merge(soil, how='outer')
print(len(merged4.index))
merged5 = merged4.merge(gut, how='outer')
final = merged5.merge(TJ, how='outer')
final = final.fillna(0)
print(len(final.columns))
final.to_csv("ALL_OTU_metagenome.csv")
