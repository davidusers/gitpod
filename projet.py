import pandas as pd 
import json 
donnees={
    'action':[]
}
# Fichier pour sauvegarder les données
FICHIER_DONNEES = "donnees_gestion.json"
# commeencons par charger les donnees ------------------------------------------------
# cette fonction permet de charger les donnees a partir du fichier csv

def loard_data():
    df=pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
    print(df.head())

    # import csv
    # with open('/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv', mode ='r')as file:
    #   csvFile = csv.reader(file)
    #   for lines in csvFile:
    #         #afficher  10 lignes
    #         print(lines)
    #prix=df["prix"].head(10)
    #nom=df["nom"].head(10)
    #symbole=df["symbole"].describe()
    #print("les prix sont : ",prix)




#-------------------------------------------------------------------------------------------#

#cette fonction permet d'afficher le menu principal 

def affiche_menu_principal():
    while True:
        print("=== 🏢 Gestion de portfolio ===")
        print("1. Ajouter une action")
        print("2. Supprimer une action")
        print("3. Afficher le portfolio")
        print("4. 📊Afficher les performances")
        print("5. 🚪Quitter")
        print()
        print("============================")
        print()
        break
        
#-------------------------------------------------------------------------------------------#
#première option: ajouter une action------------------------------------------------------------------------

def ajout_action():
    # Ici on va prendre le choix du menu principal
    while True:
        symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
        if symbol == 'Q':
            break
            
        nombre_action = int(input("Entrez le nombre d'actions à ajouter: "))
        if nombre_action <= 0:
            print("Le nombre d'actions doit être un entier positif. Veuillez réessayer.")
            continue
        prix_achat =int(input("Entrez le prix d'achat par action: "))
        if prix_achat <= 0:
            print("Le prix d'achat doit être un entier positif. Veuillez réessayer.")
            continue
        
        df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
        
        if symbol in df['symbole'].values:
            print(f"L'action {symbol} a été ajoutée à votre portfolio.")
            
            # Logique pour ajouter l'action au portfolio
            df_action = df[df['symbole'] == symbol].iloc[0]  # pour obtenir les details de l'action
            
            action_ajoutee = {
                'symbole': df_action['symbole'],  
                #'nom': df_action['nom'],
                'prix_achat': prix_achat*2, 
                'nombre_action': nombre_action
            }
            
            # Ici, vous pouvez ajouter la logique pour stocker 'action_ajoutee' dans votre portfolio
            donnees["action"].append(action_ajoutee)#permet d'ajouter l'action dans le dictionnaire

            
            # Sauvegarder dans le fichier
            with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=4)
            #action_ajoutee_df.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False)
            
            # Lire et afficher le fichier mis à jour
            with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
                portfolio_complet = json.load(f)
            #portfolio_complet = pd.read_csv(FICHIER_DONNEES)
                print("\nPortfolio mis à jour:")
                #print(portfolio_complet)
            #convertir le dictionnaire en dataframe pandas
                df_portfolio = pd.DataFrame(donnees["action"])
                print(df_portfolio)
            


            
            break
        else:
            print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
            #sauvegarder les donnees
#-----------------------------------------------------------------------------------------------------------#
# fonction pour supprimer une action ajouter
def suprimmer_action():
    symbol = input("Entrez le symbole de l'action à supprimer (ou 'q' pour quitter): ").upper()
    if symbol == 'Q':
        return
    
    # Charger les données existantes
    try:
        with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
            donnees_existantes = json.load(f)
    except FileNotFoundError:
        print("❌ Aucun portfolio trouvé.")
        return
    
    # Trouver et supprimer l'action
    action_trouvee = False
    for action in donnees_existantes["action"]:
        if action['symbole'] == symbol:
            donnees_existantes["action"].remove(action)
            action_trouvee = True
            break
    
    if action_trouvee:
        # Sauvegarder les données mises à jour
        with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
            json.dump(donnees_existantes, f, ensure_ascii=False, indent=4)
        print(f"✅ L'action {symbol} a été supprimée de votre portfolio.")
    else:
        print(f"❌ L'action {symbol} n'a pas été trouvée dans votre portfolio.")

        
      

def sauvegarder_donnees():
    """Sauvegarde les données dans le fichier CSV"""
    try:
        with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
            f.write("Données sauvegardées...\n")
        print("✅ Données sauvegardées avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")

def sauvegarder_donnees_csv():
            """Sauvegarde les données dans un fichier CSV"""
            try:
                with open('donnees_gestion.csv', 'w', encoding='utf-8') as f:
                    f.write("Données sauvegardées...\n")
                print("✅ Données sauvegardées dans donnees_gestion.csv avec succès!")
            except Exception as e:
                print(f"❌ Erreur lors de la sauvegarde CSV: {e}")

#-----------------------------------------------------------------------------------------------------------#

#creer une fonction qui vas afficher le portefolio sans passer par le imput du symbole
# def afficher_portfolio(symbol):
#     df_portfolio = pd.read_csv(FICHIER_DONNEES)

#     for i in df_portfolio:
#         if i == symbol:
#             print(i)
#             break

        
def afficher_portfolio():

    df_portfolio = pd.DataFrame(donnees["action"])
    print(df_portfolio)
    # df_portfolio = pd.read_csv(FICHIER_DONNEES)

    # for i in df_portfolio:
    #     print(i)
    #     break
#-----------------------------------------------------------------------------------------------------------#




#fonction pour afficher les performances sans symbol
def afficher_performance_action():
    df_portfolio = pd.read_csv(FICHIER_DONNEES)

    for i in df_portfolio:
        print(i)
        break









#fonction pour supprimer une action



#------------------------------------------------------------------------------------------------------------
#creer une foction qui permet de quitter l'application
def quitter_application():
    """Quitte l'application"""
    print("👋 Au revoir!")
    exit()



#-----------------------------------------------------------------------------------------------------------#       
#  fonction principale du menu principal














def menu_principal():
    """Fonction principale du menu"""
    #affiche_menu_principal()
    loard_data()
    
    while True:
        affiche_menu_principal()
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

            afficher_portfolio()
        elif choice == '4':
            #ici on vas appeler la fonction pour afficher les performances
            print("**********************************************************************************************************")
            afficher_performance_action()
            #print("Fonction d'affichage des performances à implémenter.")
        elif choice == '5':
            quitter_application()
            print("🔙 Retour au menu principal.")
            print("👋 Au revoir!")
            break
        else:
            print("❌ Option invalide!")


# Point d'entrée de l'application
if __name__ == "__main__":
    menu_principal()
    