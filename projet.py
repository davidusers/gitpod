import pandas as pd 
# Fichier pour sauvegarder les données
FICHIER_DONNEES = "donnees_gestion.csv"
# commeencons par charger les donnees ------------------------------------------------
# cette fonction permet de charger les donnees a partir du fichier csv

def loard_data():
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




#-------------------------------------------------------------------------------------------#

#cette fonction permet d'afficher le menu principal 

def affiche_menu_principal():
    while True:
        print("=== Gestion de portfolio ===")
        print("1. Ajouter une action")
        print("2. Supprimer une action")
        print("3. Afficher le portfolio")
        print("4. Afficher les performances")
        print("5. Quitter")
        print()
        print("============================")
        print()
        choice = input("Entrez votre choix (1-5): ")
        
#-------------------------------------------------------------------------------------------#
#première option: ajouter une action------------------------------------------------------------------------

def ajout_action():
    # Ici on va prendre le choix du menu principal
    while True:
        symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
        if symbol == 'Q':
            break
            
        nombre = input("Entrez le nombre d'actions à ajouter: ")
        prix_achat = input("Entrez le prix d'achat par action: ")
        
        df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
        
        if symbol in df['symbole'].values:
            print(f"L'action {symbol} a été ajoutée à votre portfolio.")
            
            # Logique pour ajouter l'action au portfolio
            df_action = df[df['symbole'] == symbol].iloc[0]  # pour obtenir les details de l'action
            
            action_ajoutee = {
                'symbole': df_action['symbole'],  # Retirer les crochets [] - c'est un string, pas une liste
                #'nom': df_action['nom'],
                'prix_achat': prix_achat*21000,
                'nombre': nombre
            }
            
        
            
            # Ici, vous pouvez ajouter la logique pour stocker 'action_ajoutee' dans votre portfolio
            action_ajoutee_df = pd.DataFrame([action_ajoutee])  # Mettre dans une liste pour créer un DataFrame d'une ligne
            
            # Sauvegarder dans le fichier
            action_ajoutee_df.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False)
            
            # Lire et afficher le fichier mis à jour
            portfolio_complet = pd.read_csv(FICHIER_DONNEES)
            print("\nPortfolio mis à jour:")
            print(portfolio_complet)
            


            
            break
        else:
            print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
            #sauvegarder les donnees
#-----------------------------------------------------------------------------------------------------------#
#fonction pour sauvegarder les donnees

def sauvegarder_donnees():
    """Sauvegarde les données dans le fichier CSV"""
    try:
        with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
            f.write("Données sauvegardées...\n")
        print("✅ Données sauvegardées avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")

#-----------------------------------------------------------------------------------------------------------#

#creer une fonction qui vas afficher le portefolio
def afficher_portfolio(symbol):
    # Logique pour afficher le portfolio
    if not symbol:
        print("Votre portfolio est vide.")
        return
        
    df_portfolio = pd.read_csv(FICHIER_DONNEES)
    print("LE data est : ",df_portfolio)
#-----------------------------------------------------------------------------------------------------------#
#fonction pour supprimer une action


def suprimmer_action():
    afficher_portfolio(symbol=None)
    """Supprime un client"""
    df_portfolio = pd.read_csv(FICHIER_DONNEES)
    print("\n--- Supprimer un client ---")
    
    try:
        #/n permet de sauter une ligne pour une meilleure lisibilité
        symbole = input("Symbole de l'action à supprimer: ").strip().upper()
        if symbole in  df_portfolio ['symbole'].values:
            df_portfolio = df_portfolio[df_portfolio['symbole'] != symbole]
            df_portfolio.to_csv(FICHIER_DONNEES, index=False)
            print(f"✅ L'action {symbole} a été supprimée avec succès!")
        if not symbole:
            print("❌ action non trouvé!")
            return
    except Exception as e:
        print(f"❌ Erreur: {e}")
        
        # Logique de suppression ici




#-----------------------------------------------------------------------------------------------------------#       
#fonction principale du menu










def menu_principal():
    """Fonction principale du menu"""
    loard_data()
    
    while True:
        choice = input("Entrez votre choix (1-5): ")
        #ici on vas gerer les differentes options du menu principal
        if choice == '1':
            #ici on vas appeler la fonction pour ajouter une action
            ajout_action()
        elif choice == '2':
            #ici on vas appeler la fonction pour supprimer une action

            suprimmer_action()
        elif choice == '3':
            #ici on vas appeler la fonction pour afficher le portefolio
            symbol = input("Entrez le symbole de l'action à afficher (ou 'q' pour quitter): ").upper()
            if symbol == 'Q':
                continue
            afficher_portfolio(symbol)
        elif choice == '4':
            #ici on vas appeler la fonction pour afficher les performances
            print("Fonction d'affichage des performances à implémenter.")
        elif choice == '5':
            #quitter l'application

            sauvegarder_avant_quitter = input("Voulez-vous sauvegarder avant de quitter? (o/n): ")
            if sauvegarder_avant_quitter.lower() == 'o':
                print("💾 Sauvegarde des modifications...")
                # Logique de sauvegarde ici
                sauvegarder_donnees()

            print("🔙 Retour au menu principal.")
            print("👋 Au revoir!")
            break
        else:
            print("❌ Option invalide!")


# Point d'entrée de l'application
if __name__ == "__main__":
    menu_principal()
    