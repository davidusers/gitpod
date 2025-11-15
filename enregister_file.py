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