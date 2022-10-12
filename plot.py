import matplotlib.pyplot as plt
from time_data import *

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha = 'center')

def displayPlot(cases, prices):
	addlabels(cases, prices)
	plt.xticks(rotation = 90)
	plt.yticks(fontsize = 6)
	plt.xlabel('Case')
	plt.ylabel('Price')
	plt.tick_params(axis='x', which='major', labelsize=5)
	plt.title(f'CSGO Case Prices {mdy}')
	plt.bar(cases, prices)
	plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
	plt.show()