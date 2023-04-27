import multipleRegressionModule as data
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
gold = data.getData()
newGold =  {'years':gold['years'],
            'ogółem':gold['ogółem'],
            'grubizna':gold['grubizna']}
df = pd.DataFrame(newGold)
print("Fajne dane do skalowania: ")
print(df)
X = df[['years','ogółem','grubizna']]
print("Nowsze dane już po skalowaniu: ")
scaledX = scale.fit_transform(X)
print(scaledX)