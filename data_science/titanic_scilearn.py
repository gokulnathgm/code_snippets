import pandas as pd

df = pd.read_csv('titanic_data.csv')
#print df.columns
df.drop(df.columns[[0,6,7,8,9,10,11]], axis=1, inplace=True)
df.to_csv('titanic_data_refined.csv')
#print df.columns
#print df['Age']
#print df.mean('Age')
#df.fillna(df.mean())
#print df['Age']


