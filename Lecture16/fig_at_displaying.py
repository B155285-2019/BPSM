#!/user/bin/python3

import os, sys
import numpy as np
import matplotlib.pyplot as plt

ecoli = open("ecoli.txt").read().replace('\n', '').upper()[0:100000]
window = 1000

at = []

counter = 0
for start in range(len(ecoli) - window):
	counter +=1
	win = ecoli[start:start+window]
	at.append((win.count('T')+win.count('A'))/window)

plt.figure(figsize=(20,10))
plt.plot(at, label="AT content", linewidth=3, color="purple")
plt.ylabel('Fraction of bases')
plt.xlabel('Position on genome')
plt.legend()
plt.savefig("Lecture16_1st_ex.png",transparent=True)
plt.show()
