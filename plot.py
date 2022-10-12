import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha = 'center')

def displayPlot(cases, prices):
	addlabels(cases, prices)
	plt.xticks(rotation = 35)
	plt.yticks(fontsize = 6)
	plt.xlabel('Case')
	plt.ylabel('Price')
	plt.tick_params(axis='x', which='major', labelsize=6)
	plt.title('CSGO Case Prices')
	plt.bar(cases, prices)
	plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
	plt.show()