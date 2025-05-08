import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import math
import numpy as np
numBins = 10
numExperiments = 5

# Sample data
#data = {
#    'Algorithm': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
#    'Power Usage (%)': [100, 150, 200, 100, 150, 200, 100, 150, 200],
#    '# of Nodes': [10, 20, 30, 15, 25, 35, 20, 30, 40]
#}

#Need to fill this to create heatmap
data = {
    'Algorithm': [],
    'Power Usage (%)': [],
    '# of Nodes': []
}

csvs = ["AODV", "DSR", "OLSR", "DSDV"] #csv for each algorithm
allData = {}

#Collect raw data from csvs
for file in csvs:
    rawData = pd.read_csv("./data/" + file + "-" + sys.argv[1] + ".csv")
    rawData = rawData.astype("float")
    allData[file] = rawData

#Find important values like min and max needed for graphing
flat_list = [float(x) for data in allData.values() for dataPoint in data.values.tolist() for x in dataPoint ]
#maxVal = math.ceil(max(flat_list))
#minVal = math.floor(min(flat_list))
maxVal = 40
minVal = 20
rang = maxVal - minVal
stepSize = (rang)/numBins

#For each algorithm load data with the needed lists
for alg in csvs:
    data['Algorithm'].extend([csvs.index(alg)] * numBins)
    #list comprehension to get lower bound of each step and format it
    data["Power Usage (%)"].extend([f'${round(x,1)} \leq x < {round(x+stepSize,1)}$' for x in np.arange(minVal,maxVal, stepSize)])
    buckets = [0] * numBins
    for dataPoint in [float(x) for data in allData[alg].values.tolist() for x in data]:
        buckets[math.floor((dataPoint-minVal)/stepSize)] += 1.0/numExperiments
    data['# of Nodes'].extend(buckets)
df = pd.DataFrame(data)

# Pivot the data to get the correct format for a heatmap
heatmap_data = df.pivot(index='Power Usage (%)', columns='Algorithm', values='# of Nodes')
heatmap_data = heatmap_data[::-1]
# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu", xticklabels=csvs, cbar_kws={'label': 'Average Node Count'})

title = sys.argv[1].replace('_', ' ') + " | Percent Power Used"

plt.title(title)
plt.ylabel('Power Usage (%)')
plt.xlabel('Algorithm')
plt.tight_layout()


#plt.show()

plt.savefig("./graphs/PowerUsageHeatMaps/" + sys.argv[1] +"-PowerUsage-HeatMap.png")
