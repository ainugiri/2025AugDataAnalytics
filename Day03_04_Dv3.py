import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# numpy - numerical python - library for numerical computations - array, matrix, random numbers, etc


# xval = np.array([0,6,12])
# yval = np.array([0, 25,75])

# plt.plot(xval, yval, color='darkred', marker='o', linestyle='dotted')    # draw points in the diagram
# plt.xlabel('Overs')
# plt.ylabel('Runs')
# plt.title('Team Performance')
# plt.grid(axis='y', linestyle='--', linewidth=5)
# plt.show()



overs = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
TeamAruns = np.array([0,6,9,18,27,40,55,70,85,100,115,130,145,160,175,190,205,220,235,250,265])

TeamBruns = np.array([0,8,15,22,30,38,50,65,70,95,110,112,140,143,170,171,191,215,230,245,260])
plt.subplot(2,1,1)
plt.plot(overs,TeamAruns, marker='o', label='TeamA', color='darkblue')
plt.subplot(2,1,2)
plt.plot(overs,TeamBruns, marker='o', label='TeamB', color='darkgreen')
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Team Performance')
plt.grid(axis='y', linestyle='--', linewidth=1)
plt.legend()
plt.show()