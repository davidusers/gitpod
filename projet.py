# import pandas as pd 


# df=pd.read_csv("/home/dav/Bureau/la cite/semestre1/programation python/symboles_prix.csv")
# print(df)

import csv
with open('/home/dav/Bureau/la cite/semestre1/programation python/symboles_prix.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)
