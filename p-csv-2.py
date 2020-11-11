import pandas as pd
df = pd.read_csv('result.csv')
#df = df.dataframe
#print (df['gender'] [df.marks < 55])
#print (df[df.marks < 55])

#print (pd.DataFrame)
#print df(df.marks < 80)
#print (df.marks.mean)
#print (df.groupby('gender'))
print (df.groupby ( 'marks'))
#print df.groupby('gender').size()
