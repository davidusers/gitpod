"""Les exigences non-fonctionnelles sont les spécifications qui décrivent les capacités et les
contraintes de fonctionnement du système.
• Interface : Le programme doit avoir une interface console avec un menu clair permettant
à l’usager d’effectuer les différentes actions exigences fonctionnelles ainsi que de
naviguer à travers les différentes options.
• Entrées usager : Le programme doit gérer correctement les entrées incorrectes, par
exemple si un symbole entré n’existe pas
• Stockage : Pour chaque action, le programme doit pouvoir stocker :
o Symbole de l’action (par exemple MSFT pour Microsoft)
o Nombre d’actions achetées
o Prix moyen par action
• Persistance : Le programme doit pouvoir stocker les informations de manière persistante,
c’est-à-dire que les informations sont conservées lors de la fermeture et réouverture du
programme."""
import pandas as pd
import os



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

    
def main():
   
    while True:
        clear_console()
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
#première option: ajouter une action------------------------------------------------------------------------
        if choice == '1':
            while True:
                symbol = input("Entrez le symbole de l'action à ajouter (ou 'q' pour quitter): ").upper()
                if symbol == 'Q':
                    break
                df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
                if symbol in df['symbole'].values:
                    print(f"L'action {symbol} a été ajoutée à votre portfolio.")
                    # Logique pour ajouter l'action au portfolio
                    
                    break
                else:
                    print(f"Le symbole {symbol} n'existe pas. Veuillez réessayer.")
            print("1")
            #deuxième option: supprimer une action-----------------------------------------------------------------------
        elif choice == '2':
            while True:
                symbol = input("Entrez le symbole de l'action à supprimer (ou 'q' pour quitter): ").upper()
                if symbol == 'Q':
                    break
                # Logique pour vérifier si l'action est dans le portfolio
                # Supposons que nous avons une liste fictive pour l'exemple
                portfolio = ['AAPL', 'MSFT', 'GOOGL']
                #troisième option: afficher le portfolio-------------------------------------------------------------------

        elif choice == '3':
            while True:
                symbol = input("Entrez le symbole de l'action à afficher (ou 'q' pour quitter): ").upper()
                if symbol == 'Q':
                    break
                # Logique pour vérifier si l'action est dans le portfolio
                # Supposons que nous avons une liste fictive pour l'exemple
                portfolio = ['AAPL', 'MSFT', 'GOOGL']
                if symbol in portfolio:
                    print(f"Détails de l'action {symbol}:")
                    # Afficher les détails de l'action
                    
                else:
                    print(f"L'action {symbol} n'est pas dans votre portfolio. Veuillez réessayer.")
                    #quatrième option: afficher les performances--------------------------------------------------------------------
        elif choice == '4':
            while True:
                symbol = input("Entrez le symbole de l'action pour afficher les performances (ou 'q' pour quitter): ").upper()
                if symbol == 'Q':
                    break
                # Logique pour vérifier si l'action est dans le portfolio
                # Supposons que nous avons une liste fictive pour l'exemple
                portfolio = ['AAPL', 'MSFT', 'GOOGL']
                if symbol in portfolio:
                    print(f"Performances de l'action {symbol}:")
                    # Afficher les performances de l'action
                    def afficher_performance_action(symbol):
                        df = pd.read_csv("/home/dav/Bureau/la_cite/semestre1/programation python/projet/symboles_prix.csv")
                        if symbol in df['symbole'].values:
                            action_details = df[df['symbole'] == symbol].iloc[0]
                            print(f"Performances de l'action {symbol}:")
                            print(f"Nom: {action_details['nom']}")
                            print(f"Prix: {action_details['prix']}")
                    afficher_performance_action(symbol)




                    break
                else:
                    print(f"L'action {symbol} n'est pas dans votre portfolio. Veuillez réessayer.")
                    #cinquième option: quitter--------------------------------------------------------------------------------------
        elif choice == '5':
            while True:
                confirm = input("Êtes-vous sûr de vouloir quitter? (o/n): ").lower()
                if confirm == 'o':
                    break
                elif confirm == 'n':
                    main()
                else:
                    print("Veuillez entrer 'o' pour oui ou 'n' pour non.")
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
        input("Appuyez sur Entrée pour continuer...")
main()