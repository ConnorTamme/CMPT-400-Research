import pandas as p
import numpy as np
import matplotlib.pyplot as plt
import sys




data = p.read_csv(sys.argv[1])

#fig,ax = plt.subplots()
fig = plt.figure(figsize =(10, 7))

plt.hist(data, bins=100)

#plt.xticks(np.arange(0.8,6,step=0.2))

# Creating plot
#counts, bins, patches = ax.hist(data)
#ax.set_xticks(bins)

# show plot
plt.savefig("test.png")
plt.show()
