import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\Jinitha\\OneDrive\\Documents\\Python\\Finds\\data.csv")
print(data)

concept = np.array(data)[:, :-1]
print(concept)

target= np.array(data)[:, -1]
print(target)

def train(con,tar):
	for i, val in enumerate(tar):
		if val == 'yes':
			specific_hypo= con[i].copy()
			break
	for i, val in enumerate(con):
		if tar[i]=='yes':
			for x in range(len(specific_hypo)):
				if val[x] != specific_hypo[x]:
					specific_hypo[x]='?'
				else:
					pass

	return specific_hypo
print(train(concept,target))





