import pandas as pd 
# importont un autre fichier python appelle ici 
#import menu.py as menu
df=pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
print(df.info())

# import csv
# with open('/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv', mode ='r')as file:
#   csvFile = csv.reader(file)
#   for lines in csvFile:
#         #afficher  10 lignes
#         print(lines)
prix=df["prix"].head(10)
nom=df["nom"].head(10)
symbole=df["symbole"].describe()
#menu.main()



print(symbole) 