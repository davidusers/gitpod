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