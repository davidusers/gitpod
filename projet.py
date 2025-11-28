import pandas as pd 
import json 
donnees={
    'action':[],
    'performance':[]
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
        print("1. ➕  Ajouter une action")
        print("2. ❌ Supprimer une action")
        print("3. 📂 Afficher le portfolio")
        print("4. 📊 Afficher les performances")
        print("5. 🚪 Quitter")
        print()
        print("============================")
        print()
        break
   
        
#-------------------------------------------------------------------------------------------#
#première option: ajouter une action------------------------------------------------------------------------

# def ajout_action():
#     # Ici on va prendre le choix du menu principal
#     while True:
#         symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
#         if symbol == 'Q':
#             break
            
#         nombre_action = int(input("Entrez le nombre d'actions à ajouter: "))
#         if nombre_action <= 0:
#             print("Le nombre d'actions doit être un entier positif. Veuillez réessayer.")
#             continue
#         # verifier si le nombre d'action existe deja pour un element faire la somme de l'ancien et du nouveau  pour chaque ajout
#         if nombre_action in [action['nombre_action'] for action in donnees["action"] if action['symbole'] == symbol]:#verifier si le nombre d'action existe 
#             #faire la somme de l'ancien et du nouveau
#             for action in donnees["action"]:
#                 if action['symbole'] == symbol:
#                     action['nombre_action'] += nombre_action
#             #print(f"Le nombre d'actions pour {symbol} a été mis à jour.")

#             continue  # Passer à la prochaine itération de la boucle principale
#         prix_achat =int(input("Entrez le prix d'achat par action: "))
#         # Si le symbole existe déjà dans le portfolio de l’usager,prix moyen doitêtre mis à jour avec le calcul suivant :𝑝𝑟𝑖𝑥 = ((𝑝𝑟𝑖𝑥𝑎𝑣𝑎𝑛𝑡 ∗ 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑣𝑎𝑛𝑡 ) + (𝑝𝑟𝑖𝑥𝑎𝑗𝑜𝑢𝑡é ∗ 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑗𝑜𝑢𝑡é ) )/(𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑣𝑎𝑛𝑡 + 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑗𝑜𝑢𝑡é)
#         if prix_achat in [action['prix_achat'] for action in donnees["action"] if action['symbole'] == symbol]:#verifier si le prix d'achat existe deja pour un element faire le calcul du prix 𝑝𝑟𝑖𝑥 = ((𝑝𝑟𝑖𝑥𝑎𝑣𝑎𝑛𝑡 ∗ 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑣𝑎𝑛𝑡 ) + (𝑝𝑟𝑖𝑥𝑎𝑗𝑜𝑢𝑡é ∗ 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑗𝑜𝑢𝑡é ) )/(𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑣𝑎𝑛𝑡 + 𝑛𝑏𝐴𝑐𝑡𝑖𝑜𝑛𝑠𝑎𝑗𝑜𝑢𝑡é)
#             for action in donnees["action"]:
#                 if  action['symbole'] == symbol:
#                     ancien_nombre = action['nombre_action']
#                     ancien_prix = action['prix_achat']
#                     nouveau_nombre = ancien_nombre + nombre_action
#                     nouveau_prix = ((ancien_prix * ancien_nombre) + (prix_achat * nombre_action)) #/ nouveau_nombre
#                     action['prix_achat'] = nouveau_prix
#             #print(f"Le prix d'achat pour {symbol} a été mis à jour.")


#         # if prix_achat <= 0 or :
#         #     print("Le prix d'achat doit être un entier positif. Veuillez réessayer.")
#             continue
        
#         df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
        
#         if symbol in df['symbole'].values:
#             print(f"L'action {symbol} a été ajoutée à votre portfolio.")
            
#             # Logique pour ajouter l'action au portfolio
#             df_action = df[df['symbole'] == symbol].iloc[0]  # pour obtenir les details de l'action
            
#             action_ajoutee = {
#                 'symbole': df_action['symbole'],  
#                 #'nom': df_action['nom'],
#                 'nombre_action':nouveau_nombre,
#                 'prix_achat': nouveau_prix
#             }
            
#             # Ici, vous pouvez ajouter la logique pour stocker 'action_ajoutee' dans votre portfolio
#             donnees["action"].append(action_ajoutee)#permet d'ajouter l'action dans le dictionnaire

#             #sauvegarder les donnees ajouter dans le fichier donnees_gestion.txt 

#             with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
#                 donnees_existantes = json.load(f)

            
#             # Sauvegarder dans le fichier de facon definitive et pouvant etre relu n;importe quelle moment
#             # with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
#             #     json.dump(donnees, f, ensure_ascii=False, indent=4)
            

#             #action_ajoutee_df.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False)
            
#             # Lire et afficher le fichier mis à jour
#             with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
#                 portfolio_complet = json.load(f)
#             #portfolio_complet = pd.read_csv(FICHIER_DONNEES)
#                 print("\nPortfolio mis à jour:")
#                 #print(portfolio_complet)
#             #convertir le dictionnaire en dataframe pandas
#                 df_portfolio = pd.DataFrame(donnees["action"])
#                 print(df_portfolio)
#             break
            
#         else:
#             print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
#             #sauvegarder les donnees


def ajout_action():
    while True:
        symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
        if symbol == 'Q':
            break
            
        # Validation du nombre d'actions
        try:
            nombre_action = int(input("Entrez le nombre d'actions à ajouter: "))
            if nombre_action <= 0:
                print("Le nombre d'actions doit être un entier positif. Veuillez réessayer.")
                continue
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
            
        # Validation du prix d'achat
        try:
            prix_achat = float(input("Entrez le prix d'achat par action: "))
            if prix_achat <= 0:
                print("Le prix d'achat doit être positif. Veuillez réessayer.")
                continue
        except ValueError:
            print("Veuillez entrer un prix valide.")
            continue
        
        # Vérifier si le symbole existe dans notre base de données
        try:
            df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
        except FileNotFoundError:
            print("Erreur: Fichier des symboles introuvable.")
            continue
        # Vérifier si le symbole existe dans le dataframe 
            
        if symbol not in df['symbole'].values:
            print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
            continue
        
        print(f"L'action {symbol} a été ajoutée à votre portfolio.")
        
        # Vérifier si l'action existe déjà dans le portfolio
        action_existante = None #initialisation de la variable pour stocker l'action existante 
        for action in donnees["action"]: #parcourir la liste des actions dans le portfolio
            if action['symbole'] == symbol:#verifier si le symbole de l'action correspond au symbole entré par l'utilisateur
                action_existante = action # si oui, stocker l'action existante dans la variable dans action_existante et sortir de la boucle
                break
        
        if action_existante: #si l'action existe deja dans le portfolio
            # Mise à jour d'une action existante
            ancien_nombre = action_existante['nombre_action']
            ancien_prix = action_existante['prix_achat']
            nouveau_nombre = ancien_nombre + nombre_action
            # Calcul du prix moyen pondéré
            nouveau_prix_moyen = ((ancien_prix * ancien_nombre) + (prix_achat * nombre_action)) / nouveau_nombre
            
            # Mise à jour des valeurs
            action_existante['nombre_action'] = nouveau_nombre
            action_existante['prix_achat'] = nouveau_prix_moyen
            
            print(f"Action {symbol} mise à jour: {ancien_nombre} -> {nouveau_nombre} actions, prix moyen: {nouveau_prix_moyen:.2f}$")#affichage du resultat de la mise a jour 2f permet d'afficher 2 chiffre apres la virgule
        else:
            # Ajout d'une nouvelle action
            df_action = df[df['symbole'] == symbol].iloc[0]# pour obtenir les details de l'action
            
            action_ajoutee = {
                'symbole': df_action['symbole'],
                'nombre_action': nombre_action,
                'prix_achat': prix_achat
            }
            
            donnees["action"].append(action_ajoutee)
            print(f"Nouvelle action {symbol} ajoutée: {nombre_action} actions à {prix_achat}$")
        
        # Sauvegarde des données
        try:
            with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
                json.dump(donnees, f, ensure_ascii=False, indent=4)
            print("Portfolio sauvegardé avec succès!")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
        
        # Affichage du portfolio mis à jour
        if donnees["action"]:
            df_portfolio = pd.DataFrame(donnees["action"])
            print("\nPortfolio mis à jour:")
            print(df_portfolio)
        else:
            print("\nPortfolio vide.")
        
        break
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
# creons une fonction pour lire les donnees du fichier json
# def lire_donnees():
#     try:
#         with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
#             donnees_lues = json.load(f)
#             return donnees_lues
#     except FileNotFoundError:
#         print("❌ Aucun portfolio trouvé.")
#         return {'action': [], 'performance': []}

#fonction pour sauvegarder les donnees dans le fichier json

def sauvegarder_donnees():
    """Sauvegarde les données dans le fichier JSON"""
    try:
        with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        print("✅ Données sauvegardées avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")

#-----------------------------------------------------------------------------------------------------------#

#troisieme option: afficher le portfolio-----------------------------------------------------------------------

# nous allons creer une fonction qui affiche tout le portfolio    
def afficher_portfolio():

    df_portfolio = pd.DataFrame(donnees["action"])
    print(df_portfolio)
    # df_portfolio = pd.read_csv(FICHIER_DONNEES)

    # for i in df_portfolio:
    #     print(i)
    #     break
#-----------------------------------------------------------------------------------------------------------#




#fonction pour afficher les performances  qui affichera le symbole, le nombre d'action, le prix d'achat, le prix actuel
def afficher_performance_action():
    df_portfolio = pd.DataFrame(donnees["action"])
    df_prix_actuel = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
    
    performances = []
    
    for index, row in df_portfolio.iterrows():#permet de parcourir chaque ligne du dataframe
        symbole = row['symbole']#obtenir le symbole de l'action
        nombre_action = row['nombre_action']#obtenir le nombre d'action
        #si le nombre d'action existe deja pour un element faire la somme de l'ancien et du nouveau
        
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


#-----------------------------------------------------------------------------------------------------------#

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
            #ici on vas appeler la fonction pour ajouter une action et aussi sauvegarder les donnees
            ajout_action(),
            sauvegarder_donnees()
        

            
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
    