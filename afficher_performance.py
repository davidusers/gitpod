# Afficher les performances de l'action
import pandas as pd
def afficher_performance_action(symbol):
    df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
    if symbol in df['symbole'].values:
        action_details = df[df['symbole'] == symbol].iloc[0]
        print(f"Performances de l'action {symbol}:")
        print(f"Nom: {action_details['nom']}")
        print(f"Prix: {action_details['prix']}")
        # Ajouter d'autres détails de performance si disponibles
    else:
        print(f"L'action {symbol} n'a pas été trouvée dans les données disponibles.")
afficher_performance_action("AAPL")