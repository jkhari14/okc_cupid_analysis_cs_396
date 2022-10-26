'''
Use Levenshtein distance to convert essays to distance amounts and write them out to a file

'''

import numpy as np
import scipy
import pandas as pd
import matplotlib as mp
from scipy.spatial.distance import hamming
from Levenshtein import distance as lev_dist
import csv
    
f = open('/Users/skim/Documents/Classes/Fall2022/DS Group Project/test_output.txt', "w")
df = pd.read_csv('/Users/skim/Documents/Classes/Fall2022/DS Group Project/okcupid_profiles_63_rows.csv')

essay0_df = df['essay0']

ess1 = essay0_df.iloc[0]
ess2 = essay0_df.iloc[1]

ld = lev_dist(ess1, ess2)

dists = [[''] * essay0_df.shape[0] for _ in range(essay0_df.shape[0])]

essays = ['' for _ in range(essay0_df.shape[0])]
for row in range(len(essay0_df)):
    essays[row] = str(essay0_df.iloc[row])
dists[0][0] = lev_dist(essays[0], essays[0])

for row in range(len(dists)):
    for col in range(len(dists[0])):

        dists[row][col] = lev_dist(essays[row], essays[col])
# write the output to a file
f.write(','.join(str(item) for lst in dists for item in lst))
f.close()