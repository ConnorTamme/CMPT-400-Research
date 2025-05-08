import pandas as p
import numpy as np
import matplotlib.pyplot as plt
import sys


csvs = ["AODV", "OLSR", "DSR", "DSDV"]
colors = ["skyblue", "orange", "yellow", "red"]

allData = []

fig = plt.figure(figsize =(10, 7))
for file in csvs:
    file1 = open(file + "SuccessRate.csv", 'r')
    Lines = file1.readlines()
    allData.append(float(Lines[1].strip()))

bars = plt.bar(csvs, allData)
plt.yticks(range(0, 101, 10))
for i in range(len(colors)):
    bars[i].set_color(colors[i])
    bars[i].set_edgecolor('black')
#plt.xticks(range(len(csvs)), csvs, size='small')
#fig,ax = plt.subplots()

# Set the x and y labels
plt.xlabel('Protocol')
plt.ylabel('Success Rate (%)')

# Set the title
plt.title(sys.argv[1] + " : Sending Success Rate")

#plt.xticks(np.arange(0.8,6,step=0.2))

# Creating plot
#counts, bins, patches = ax.hist(data)
#ax.set_xticks(bins)
# show plot
plt.savefig("./graphs/" + sys.argv[1] + "Rate.png")
