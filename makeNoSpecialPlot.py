import pandas as p
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

csvs = ["AODV", "OLSR", "DSR", "DSDV"]
colors = ["skyblue", "orange", "yellow", "red"]
allData = []
# Create a figure and axis

# Plot histograms for each CSV file
for file in csvs:
    data = p.read_csv(file + ".Spec.csv")
    data = data.astype("float")
    allData.append(data)
flat_list = [float(x) for data in allData for dataPoint in data.values.tolist() for x in dataPoint ]
maxVal = math.ceil(max(flat_list))
minVal = math.floor(min(flat_list))
rang = maxVal-minVal
def makeGraph(dataSet, name, color):
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.hist(dataSet, bins=np.arange(minVal,maxVal, rang/70), color=color)#, alpha=0.5, label=file)
    # Add a legend
    mean_value = dataSet.values.mean()
    # Add grid lines for better readability
    ax.grid(True, linestyle='--', alpha=0.7)
    # Add a vertical line for the mean
    plt.axvline(mean_value, color='black', linestyle='dashed', linewidth=2)

    # Add text for the mean value
    plt.text(mean_value, plt.ylim()[1]*0.9, f'Mean: {mean_value:.2f}', color='black', ha='left')

    # Add labels and title
    ax.set_xlabel('Power Usage (%)')
    ax.set_ylabel('Number of Nodes')
    ax.set_xticks(np.arange(minVal-2,maxVal+2,1))
    ax.set_yticks(np.arange(0, len(data.values.tolist()) + 10, 10))
    ax.set_title(sys.argv[1] + " (No sources/sinks) : " + name)

# Customize the x-ticks and y-ticks
# fig = plt.figure(figsize =(10, 7))
# for file in csvs:
#     plt.hist(p.read_csv(file + ".csv"),bins=50,alpha=0.5, label=file)


# plt.legend(loc='upper right')
# #plt.xticks(np.arange(20,40,step=1))
# #fig,ax = plt.subplots()


# #plt.xticks(np.arange(0.8,6,step=0.2))

# # Creating plot
# #counts, bins, patches = ax.hist(data)
# #ax.set_xticks(bins)

# # show plot
    plt.savefig("./graphs/" + sys.argv[1] +name+"NoSS.png")

for i in range(len(csvs)):
    makeGraph(allData[i], csvs[i], colors[i])

