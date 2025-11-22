# Logique pour vérifier si l'action est dans le portfolio
import pandas as pd 
def afficher_portfolio(portfolio):
    if not portfolio:
        print("Votre portfolio est vide.")
        return

    df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
    print("Détails de votre portfolio:")
    for symbol in portfolio:
        if symbol in df['symbole'].values:
            action_details = df[df['symbole'] == symbol].iloc[0]
            print(f"Symbole: {action_details['symbole']}, Nom: {action_details['nom']}, Prix: {action_details['prix']}")
        else:
            print(f"L'action {symbol} n'a pas été trouvée dans les données disponibles.")
# Exemple d'utilisation

