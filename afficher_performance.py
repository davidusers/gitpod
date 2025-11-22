import pandas as pd
donnees={
    'action':[],
    'performance':[]
}
def afficher_performance_action():
    df_portfolio = pd.DataFrame(donnees["action"])
    df_prix_actuel = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
    
    performances = []
    
    for index, row in df_portfolio.iterrows():#permet de parcourir chaque ligne du dataframe
        symbole = row['symbole']#obtenir le symbole de l'action
        nombre_action = row['nombre_action']#obtenir le nombre d'action
        #si le nombre d'action existe deja faire la somme (le l'ancien et le nouveau)
        if symbole in df_portfolio['symbole'].values:
            nombre_action += df_portfolio[df_portfolio['symbole'] == symbole]['nombre_action'].sum()
            
        prix_achat = row['prix_achat']#obtenir le prix d'achat
        
        prix_actuel_row = df_prix_actuel[df_prix_actuel['symbole'] == symbole]#permet de filtrer le dataframe des prix actuels pour obtenir la ligne correspondant au symbole
        if not prix_actuel_row.empty:#verifier si la ligne existe
            prix_actuel = prix_actuel_row.iloc[0]['prix']#obtenir le prix actuel
            performance = (prix_actuel - prix_achat) * nombre_action



            performances.append({
                'symbole': symbole,
                'nombre_action': nombre_action,
                'prix_achat': prix_achat,
                'prix_actuel': prix_actuel,
                'Gain/perte': performance
            })
    
    df_performances = pd.DataFrame(performances)
    print(df_performances)
