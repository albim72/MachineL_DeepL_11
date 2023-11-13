import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    'jablka':[3,5,6,2,0,1],
    'gruszki':[8,4,3,11,2,3],
    'winogrona':[2,1,1,1,2,3]
}

pu = pd.DataFrame(data)
print(pu)

pu2 = pd.DataFrame(data,index=['Leon','Olga','Piotr','Nadia','Maria','Marek'])
print(pu2)

tofile = pu2.to_csv('owoce.csv')
print(pu2.info())

print("______________________________________")
dffirma = pd.read_csv('firma.csv')
print(dffirma)

print("______________________________________")

t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2*np.pi*t)


fig,ax = plt.subplots()
ax.plot(t,s)
ax.set(xlabel='czas [s]', ylabel='napięcie prądu [mv]', title = ' pomiar napięcia prądu w czasie...')
ax.grid()
fig.savefig('test.png')
plt.show()
