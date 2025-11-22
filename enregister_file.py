import pandas as pd
def save_file():
    data = {
        'symbole': ['AAPL', 'GOOGL', 'MSFT'],
        'nom': ['Apple Inc.', 'Alphabet Inc.', 'Microsoft Corp.'],
        'prix': [150.0, 2800.0, 300.0]
    }
    df = pd.DataFrame(data)
    df.to_csv('symboles_prix.csv', index=False)
    print("Fichier enregistré sous le nom 'symboles_prix.csv'")
    

    # def sauvegarder_donnees():
    #     """Sauvegarde les données dans le fichier CSV"""
    #     try:
    #         with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
    #             f.write("Données sauvegardées...\n")
    #         print("✅ Données sauvegardées avec succès!")
    #     except Exception as e:
    #         print(f"Erreur lors de la sauvegarde: {e}")