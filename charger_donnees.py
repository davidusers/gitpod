import csv
import pandas as pd
# def load_data(file_path):
#     """
#     Charge les données depuis un fichier CSV.

#     Args:
#         file_path (str): Le chemin vers le fichier CSV.

#     Returns:
#         list: Une liste de dictionnaires représentant les lignes du fichier CSV.
#     """
#     with open('/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv', mode='r', encoding='utf-8') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row)
# load_data('/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv')

#-----------------------------------methode alternative avec pandas---------------------------------------
def load_data_pandas(file_path):
    
    df = pd.read_csv(file_path)
    print(df.head())  # Affiche les premières lignes du DataFrame
    return df.head()
load_data_pandas('/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv')