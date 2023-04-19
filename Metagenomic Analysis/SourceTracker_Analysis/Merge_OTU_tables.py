# This script is written to merge METAGENOME csv files. Please edit the code for individual domains.

import pandas as pd

# read in csv files
TJ = pd.read_csv("TJ_OTU_metagenome.csv")
fresh = pd.read_csv("freshwater_OTU_metagenome.csv")
gut = pd.read_csv("gut_OTU_metagenome.csv")
ocean = pd.read_csv("ocean_OTU_metagenome.csv")
pacific = pd.read_csv("pacific_OTU_metagenome.csv")
soil = pd.read_csv("soil_OTU_metagenome.csv")
waste = pd.read_csv("wastewater_OTU_metagenome.csv")

# keep only desired columns
TJ = TJ.loc[:, ['species', '1_Radio_Club_8_28_20', '2_Boca_Rio_8_28_20', '3_Radio_Club_11_10_20', '4_Boca_Rio_11_10_20', '5_Radio_Club_12_30_20', '6_Boca_Rio_12_30_20', '7_Radio_Club_1_27_21', '8_Boca_Rio_1_27_21', '9_Radio_Club_3_14_21', '10_Boca_Rio_3_14_21', '12_Boca_Rio_4_14_21', '13_Radio_Club_5_5_21', '14_Boca_Rio_5_5_21']]
fresh = fresh.loc[:, ['species', 'SRR1514963', 'SRR1515032', 'SRR1518285', 'SRR1522964', 'SRR1522971', 'SRR1522973', 'SRR1522974']]
gut = gut.loc[:, ['species', 'ERR866563', 'ERR866564', 'ERR866565', 'ERR866566', 'ERR866568', 'ERR866569', 'ERR866571', 'ERR866572', 'ERR866576', 'ERR866580']]
ocean = ocean.loc[:, ['species', 'ERR770959', 'ERR770962', 'ERR770967', 'ERR770968', 'ERR770974', 'ERR770978', 'ERR770982', 'ERR770983', 'ERR770989', 'ERR770990']]
pacific = pacific.loc[:, ['species', 'ERR599080', 'ERR599091', 'ERR599093', 'ERR599114', 'ERR599118', 'ERR599119', 'ERR599120', 'ERR599142', 'ERR599151', 'ERR599160']]
soil = soil.loc[:, ['species', 'ERR671925', 'ERR671927', 'ERR671929', 'ERR671930', 'ERR671931', 'ERR671932', 'ERR671933', 'ERR671934', 'ERR671937', 'ERR687883']]
waste = waste.loc[:, ['species', 'SRR17408621', 'SRR17408622', 'SRR17408623', 'SRR17408624', 'SRR17408625', 'SRR17408626', 'SRR17408627', 'SRR17408628', 'SRR17408629', 'SRR17408630']]

# merge all OTU tables together
merged1 = ocean.merge(pacific, how='outer')
print(len(merged1.columns))
merged2 = merged1.merge(waste, how='outer')
print(len(merged2.columns))
merged3 = merged2.merge(fresh, how='outer')
print(len(merged3.columns))
merged4 = merged3.merge(soil, how='outer')
print(len(merged4.columns))
merged5 = merged4.merge(gut, how='outer')
print(len(merged5.columns))
final = merged5.merge(TJ, how='outer')
final = final.fillna(0)
print(len(final.columns))
final.to_csv("ALL_OTU_metagenome.csv")