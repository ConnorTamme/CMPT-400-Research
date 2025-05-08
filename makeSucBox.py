import matplotlib.pyplot as plt
import numpy as np
import sys

data = {}

csvs = ["AODV",  "DSR", "OLSR", "DSDV"]
colors = ["skyblue", "orange", "yellow", "red"]


fig = plt.figure(figsize =(10, 7))
for alg in csvs:
    file = open("./data/" + alg + "-" + sys.argv[1]+ "-SuccessRate.csv", 'r')
    Lines = file.readlines()
    data[alg] = [float(x.strip('\n')) for x in Lines[1:]]


# Create the box plot
fig, ax = plt.subplots(figsize=(8, 6))

# Extract the data from the dictionary values for the box plot
data_values = list(data.values())

# Create the box plot
ax.boxplot(data_values)

# Set the x-tick labels to the dictionary keys
ax.set_xticklabels(data.keys())

ax.set_yticks(np.arange(0, 101, 10))

# Add labels and title
ax.set_xlabel('Protocol')
ax.set_ylabel('Success Rate (%)')
ax.set_title(sys.argv[1].replace('_', ' ') + " | Sending Success Rate")
# Show the plot
plt.tight_layout()
#plt.show()

plt.savefig("./graphs/SuccessRateBoxGraphs/" + sys.argv[1] + "-SuccessRate-Box.png")
