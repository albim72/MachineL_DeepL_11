import pandas as pd


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
