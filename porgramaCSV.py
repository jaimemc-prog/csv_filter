import os
import pandas as pd


df = pd.read_csv('prueba.csv')

df['description']=df['description'].str.replace('\n','<br>')

df['description']=df['description'].apply(lambda x: "<p>" + str(x))

df['description']=df['description'].apply (lambda x: str(x) + "</p>")
df.to_csv('pruebahtml.csv',index = False)
