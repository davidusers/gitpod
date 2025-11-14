# Logique pour ajouter l'action au portfolio
# symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
# import pandas as pd
# def ajouter_action_au_portfolio(portfolio):
#     while True:
#         symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
#         if symbol == 'Q':
#             break
#         df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
#         if symbol in df['symbole'].values:
#             print(f"L'action {symbol} a été ajoutée à votre portfolio.")
#             portfolio.append(symbol)
#             break
#         else:
#             print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
#     return portfolio

#affiche la somme de deux nombres
a=int(input("entrez un nombre a:"))

b=int(input("entrez un nombre b:"))
c=a+b
print("la somme de a et b est egale a :",c)