#logique pour supprimer l'action du portfolio
def supprimer_action_du_portfolio(portfolio):
    while True:
        symbol = input("Entrez le symbole de l'action à supprimer (ou 'q' pour quitter): ").upper()
        if symbol == 'Q':
            break
        if symbol in portfolio:
            portfolio.remove(symbol)
            print(f"L'action {symbol} a été supprimée de votre portfolio.")
            break
        else:
            print(f"L'action {symbol} n'est pas dans votre portfolio. Veuillez réessayer.")
    return portfolio



# def supprimer_action():
#     """Fonction pour supprimer une action du portfolio"""
    
#     # Vérifier d'abord si le portfolio n'est pas vide
#     if not donnees["action"]:
#         print("Votre portfolio est vide. Aucune action à supprimer.")
#         return
    
#     # Afficher le portfolio actuel
#     print("\n📊 VOTRE PORTFOLIO ACTUEL:")
#     df_portfolio = pd.DataFrame(donnees["action"])
#     print(df_portfolio)
    
#     while True:
#         symbol = input("\nEntrez le symbole de l'action à supprimer (ou 'q' pour annuler): ").upper()
        
#         if symbol == 'Q':
#             print("Suppression annulée.")
#             return
        
#         # Vérifier si le symbole existe dans le portfolio
#         action_trouvee = None
#         for action in donnees["action"]:
#             if action['symbole'] == symbol:
#                 action_trouvee = action
#                 break
        
#         if not action_trouvee:
#             print(f"❌ Le symbole {symbol} n'existe pas dans votre portfolio. Veuillez réessayer.")
#             continue
        
#         # Afficher les détails de l'action trouvée
#         print(f"\nAction trouvée:")
#         print(f"Symbole: {action_trouvee['symbole']}")
#         print(f"Nombre d'actions: {action_trouvee['nombre_action']}")
#         print(f"Prix d'achat moyen: {action_trouvee['prix_achat']:.2f}$")
        
#         # Demander confirmation
#         confirmation = input(f"\nÊtes-vous sûr de vouloir supprimer {symbol} de votre portfolio? (o/n): ").lower()
        
#         if confirmation in ['o', 'oui', 'y', 'yes']:
#             # Supprimer l'action
#             donnees["action"] = [action for action in donnees["action"] if action['symbole'] != symbol]
            
#             # Sauvegarder les modifications
#             try:
#                 with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
#                     json.dump(donnees, f, ensure_ascii=False, indent=4)
#                 print(f"✅ Action {symbol} supprimée avec succès!")
                
#                 # Afficher le portfolio mis à jour
#                 if donnees["action"]:
#                     print("\n📊 PORTFOLIO MIS À JOUR:")
#                     df_nouveau = pd.DataFrame(donnees["action"])
#                     print(df_nouveau)
#                 else:
#                     print("\n📊 Votre portfolio est maintenant vide.")
                    
#             except Exception as e:
#                 print(f"❌ Erreur lors de la sauvegarde: {e}")
        
#         else:
#             print("Suppression annulée.")
        
#         break