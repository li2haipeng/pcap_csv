#!/usr/bin/env python

# Boyang Wang,
# Department of Electrical Enigneering and Computer Science
# University of Cincinnati
# boyang.wang@uc.edu

# Platform Information
# CPU: 3.30 GHz, Intel Core i5-2500
# RAM: 512 MB
# OS: Ubuntu 12.04 (VM, Host:Windows 7)

# Statement
# This .py file is able to generate figures for the paper: Circular Range Search over Encrypted Cloud Data

from pylab import *
import matplotlib.font_manager
import matplotlib.pyplot as plt
import matplotlib

# The purpose of these following three lines is to generate figures without type 3 fonts.
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
# matplotlib.rcParams['text.usetex'] = True

# Set appropriate figure width/height
# figure(figsize=(5.75, 3.75))
fig = plt.figure(figsize=(5.75, 3.75))
# Set appropriate margins, these values are normalized into the range [0, 1]
subplots_adjust(left=0.20, bottom=0.20, right=0.90, top=0.90, wspace=0.1, hspace=0.1)

# Set parameters in the figure


x = [10, 20, 30, 40, 50]

y = [3.0313, 13.029, 23.029, 33.029, 43.029]

yy = [378330, 839946, 1324770, 1812434, 2301663]



# increase each following value by 0.02, so they will be easily observed in the figure
# original values are y_1 = [0.011, 0.010, 0.012, 0.013]
# y_1 = [0.031, 0.030, 0.032, 0.033, 0.045]

# Plot lines in the figure
ax = fig.add_subplot(111)

# Plot lines in the figure
# The first two are the corresponding theoretical results based on complexity
# plot(x, y, '-o', linewidth=1.4, color='blue', markeredgecolor='blue', markerfacecolor='white', markersize=10,
#      markeredgewidth=1.5, label='Without Meddler')
# plot(x, y1, '-s', linewidth=1.4, color='green', markeredgecolor='green', markerfacecolor='white', markersize=10,
#      markeredgewidth=1.5, label='$p=0.2$ (Mild, $T=5000$)')
# plot(x, yy, '-d', linewidth=1.4, color='red', markeredgecolor='red', markerfacecolor='white', markersize=10,
#      markeredgewidth=1.5, label='$p=0.2$ (Spicy, $T=5000$)')
ax.plot(x, y, '-o', linewidth=1.4, color='blue', markeredgecolor='blue', markerfacecolor='blue', markersize=10,
     markeredgewidth=1.5, label='delay')

prop = matplotlib.font_manager.FontProperties(size=16)
leg = legend(loc='upper left', prop=prop)

ax2 = ax.twinx()
ax2.plot(x, yy, '-*', linewidth=1.4, color='red', markeredgecolor='red', markerfacecolor='red', markersize=10,
     markeredgewidth=1.5, label='overhead')



prop = matplotlib.font_manager.FontProperties(size=16)
leg = legend(loc='upper right', prop=prop)

# set the fontsize of the legend
for t in leg.get_texts():
    t.set_fontsize('16')

# set ticker
majorLocator_x = MultipleLocator(10)
majorLocator_y = MultipleLocator(10)
majorLocator_yy = MultipleLocator(500000)
ax.xaxis.set_major_locator(majorLocator_x)
ax2.xaxis.set_major_locator(majorLocator_x)
ax.yaxis.set_major_locator(majorLocator_y)
ax2.yaxis.set_major_locator(majorLocator_yy)


# Set labels for axes
ax.tick_params(labelsize=16)
# plt.yticks(size=16)

# xlim(1, 2000)
# ax.set_xscale('log', basex=10)
# ax.set_xticks([2**12,2**14,2**16,2**18, 2**20])
ax.set_ylim(0, 50)
ax2.set_ylim(300000, 3000000)
xlim(8, 52)
xlabel('Minimum Amount of Time', fontsize=16)
ax.set_ylabel('Delay', fontsize=16)

ax2.set_ylabel('Overhead',fontsize=16)
ax2.tick_params(labelsize=16)
# title('The Total Cost')
# grid(True)

# Save file as .eps
savefig('unfinished_queries.eps', format='eps')
show()
exit(0)