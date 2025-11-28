import pandas as pd
# Logique pour ajouter l'action au portfolio
def ajout_action():
    #ici on vas prendre le choix du menu principal
    while True:
        symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
        nombre=input("Entrez le nombre d'actions à ajouter: ")
        prix_achat=input("Entrez le prix d'achat par action: ")
        if symbol == 'Q':
            break
        df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
        if symbol not in df['symbole'].values:
            print(f"L'action symbol n'a été trouve à votre portfolio.")
            return
        # Validation du nombre d'actions
        try:
            nombre=int(input("entrez le nombre d'action a ajouter: "))
            if nombre <=0:
                print("le nombre d'action  doit un nombre entier positif")
                return
        except ValueError:
            print("ERREUR: Veuillez entrer un nombre entier valide pour le nombre d'actions.")
            return
        # Validation du prix d'achat
        try:
            prix_dachat=float(input("entrez le prix d'achat par action: "))
            if prix_dachat <=0:
                print("le prix d'achat doit un nombre positif")
                return
        except ValueError:
            print("ERREUR: Veuillez entrer un nombre valide pour le prix d'achat.")
            return
        #calcul du nouveau prix moyen si l'action existe deja
        if symbol in df["symbole"].values:
            ancien_nombre=df["nombre"]
            ancien_prix=df["prix_achat"]
            nouveau_nombre=ancien_nombre + nombre
            nouveau_prix_moyen=((ancien_prix * ancien_nombre)+(prix_dachat * nombre))/nouveau_nombre
            df["nombre"]=nouveau_nombre
            df["prix_achat"]=nouveau_prix_moyen
            print(f"Action {symbol} mise à jour: {ancien_nombre} -> {nouveau_nombre} actions")
            print(f"Prix moyen mis à jour: {ancien_prix:.2f}$ -> {nouveau_prix_moyen:.2f}$")
        else:
            #ajout d'une nouvelle action
            df=symbol
            df["nombre"]=nombre
            df["prix_achat"]=prix_achat
            print(f"Action {symbol} ajoutée avec succès!")
        break
ajout_action()
    #sauvegardons les donnees ajouter 
    


            
