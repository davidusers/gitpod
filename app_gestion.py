import os
import json
from datetime import datetime

# Fichier pour sauvegarder les données
FICHIER_DONNEES = "donnees_gestion.json"

# Structure des données
donnees = {
    "clients": [],
    "produits": [],
    "commandes": []
}

def charger_donnees():
    """Charge les données depuis le fichier JSON"""
    global donnees
    try:
        if os.path.exists(FICHIER_DONNEES):
            with open(FICHIER_DONNEES, 'r', encoding='utf-8') as f:
                donnees = json.load(f)
            print("✅ Données chargées avec succès!")
        else:
            print("ℹ️  Aucun fichier de données trouvé. Démarrage avec des données vides.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement des données: {e}")

def sauvegarder_donnees():
    """Sauvegarde les données dans le fichier JSON"""
    try:
        with open(FICHIER_DONNEES, 'w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        print("✅ Données sauvegardées avec succès!")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde: {e}")

def afficher_menu_principal():
    """Affiche le menu principal"""
    print("\n" + "="*50)
    print("🏢 APPLICATION DE GESTION")
    print("="*50)
    print("1. 👥 Gestion des clients")
    print("2. 📦 Gestion des produits")
    print("3. 🛒 Gestion des commandes")
    print("4. 📊 Statistiques")
    print("5. 💾 Sauvegarder les données")
    print("0. 🚪 Quitter")
    print("="*50)

def afficher_sous_menu(titre):
    """Affiche un sous-menu"""
    print(f"\n--- {titre} ---")
    print("1. Ajouter")
    print("2. Lister")
    print("3. Modifier")
    print("4. Supprimer")
    print("5. Rechercher")
    print("0. Retour au menu principal")

# ==================== GESTION DES CLIENTS ====================

def gerer_clients():
    """Menu de gestion des clients"""
    while True:
        afficher_sous_menu("GESTION DES CLIENTS")
        choix = input("Choisissez une option (0-5): ")
        
        if choix == "1":
            ajouter_client()
        elif choix == "2":
            lister_clients()
        elif choix == "3":
            modifier_client()
        elif choix == "4":
            supprimer_client()
        elif choix == "5":
            rechercher_client()
        elif choix == "0":
            break
        else:
            print("❌ Option invalide!")

def ajouter_client():
    """Ajoute un nouveau client"""
    print("\n--- Ajouter un client ---")
    try:
        id_client = len(donnees["clients"]) + 1
        nom = input("Nom: ").strip()
        prenom = input("Prénom: ").strip()
        email = input("Email: ").strip()
        telephone = input("Téléphone: ").strip()
        
        if not nom or not prenom:
            print("❌ Le nom et prénom sont obligatoires!")
            return
        
        client = {
            "id": id_client,
            "nom": nom,
            "prenom": prenom,
            "email": email,
            "telephone": telephone,
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        donnees["clients"].append(client)
        print(f"✅ Client {prenom} {nom} ajouté avec succès (ID: {id_client})")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'ajout: {e}")

def lister_clients():
    """Liste tous les clients"""
    print("\n--- Liste des clients ---")
    if not donnees["clients"]:
        print("ℹ️  Aucun client enregistré.")
        return
    
    for client in donnees["clients"]:
        print(f"ID: {client['id']} | {client['prenom']} {client['nom']} | "
              f"Email: {client['email']} | Tél: {client['telephone']}")

def modifier_client():
    """Modifie un client existant"""
    print("\n--- Modifier un client ---")
    lister_clients()
    
    try:
        id_client = int(input("\nID du client à modifier: "))
        client = next((c for c in donnees["clients"] if c["id"] == id_client), None)
        
        if not client:
            print("❌ Client non trouvé!")
            return
        
        print(f"Modification du client: {client['prenom']} {client['nom']}")
        client["nom"] = input(f"Nouveau nom [{client['nom']}]: ") or client["nom"]
        client["prenom"] = input(f"Nouveau prénom [{client['prenom']}]: ") or client["prenom"]
        client["email"] = input(f"Nouvel email [{client['email']}]: ") or client["email"]
        client["telephone"] = input(f"Nouveau téléphone [{client['telephone']}]: ") or client["telephone"]
        
        print("✅ Client modifié avec succès!")
        
    except ValueError:
        print("❌ ID invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la modification: {e}")

def supprimer_client():
    """Supprime un client"""
    print("\n--- Supprimer un client ---")
    lister_clients()
    
    try:
        id_client = int(input("\nID du client à supprimer: "))
        client = next((c for c in donnees["clients"] if c["id"] == id_client), None)
        
        if not client:
            print("❌ Client non trouvé!")
            return
        
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer {client['prenom']} {client['nom']}? (o/n): ")
        if confirmation.lower() == 'o':
            donnees["clients"] = [c for c in donnees["clients"] if c["id"] != id_client]
            print("✅ Client supprimé avec succès!")
        else:
            print("❌ Suppression annulée.")
            
    except ValueError:
        print("❌ ID invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la suppression: {e}")

def rechercher_client():
    """Recherche un client"""
    print("\n--- Rechercher un client ---")
    terme = input("Entrez un nom ou prénom à rechercher: ").lower().strip()
    
    if not terme:
        print("❌ Veuillez entrer un terme de recherche!")
        return
    
    resultats = [c for c in donnees["clients"] 
                if terme in c["nom"].lower() or terme in c["prenom"].lower()]
    
    if not resultats:
        print("ℹ️  Aucun client trouvé.")
        return
    
    print(f"\n🔍 {len(resultats)} client(s) trouvé(s):")
    for client in resultats:
        print(f"ID: {client['id']} | {client['prenom']} {client['nom']} | "
              f"Email: {client['email']}")

# ==================== GESTION DES PRODUITS ====================

def gerer_produits():
    """Menu de gestion des produits"""
    while True:
        afficher_sous_menu("GESTION DES PRODUITS")
        choix = input("Choisissez une option (0-5): ")
        
        if choix == "1":
            ajouter_produit()
        elif choix == "2":
            lister_produits()
        elif choix == "3":
            modifier_produit()
        elif choix == "4":
            supprimer_produit()
        elif choix == "5":
            rechercher_produit()
        elif choix == "0":
            break
        else:
            print("❌ Option invalide!")

def ajouter_produit():
    """Ajoute un nouveau produit"""
    print("\n--- Ajouter un produit ---")
    try:
        id_produit = len(donnees["produits"]) + 1
        nom = input("Nom du produit: ").strip()
        description = input("Description: ").strip()
        prix = float(input("Prix: "))
        quantite = int(input("Quantité en stock: "))
        
        if not nom:
            print("❌ Le nom du produit est obligatoire!")
            return
        
        produit = {
            "id": id_produit,
            "nom": nom,
            "description": description,
            "prix": prix,
            "quantite": quantite,
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        donnees["produits"].append(produit)
        print(f"✅ Produit '{nom}' ajouté avec succès (ID: {id_produit})")
        
    except ValueError:
        print("❌ Prix ou quantité invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de l'ajout: {e}")

def lister_produits():
    """Liste tous les produits"""
    print("\n--- Liste des produits ---")
    if not donnees["produits"]:
        print("ℹ️  Aucun produit enregistré.")
        return
    
    for produit in donnees["produits"]:
        print(f"ID: {produit['id']} | {produit['nom']} | "
              f"Prix: {produit['prix']}€ | Stock: {produit['quantite']} | "
              f"Desc: {produit['description'][:30]}...")

def modifier_produit():
    """Modifie un produit existant"""
    print("\n--- Modifier un produit ---")
    lister_produits()
    
    try:
        id_produit = int(input("\nID du produit à modifier: "))
        produit = next((p for p in donnees["produits"] if p["id"] == id_produit), None)
        
        if not produit:
            print("❌ Produit non trouvé!")
            return
        
        print(f"Modification du produit: {produit['nom']}")
        produit["nom"] = input(f"Nouveau nom [{produit['nom']}]: ") or produit["nom"]
        produit["description"] = input(f"Nouvelle description [{produit['description']}]: ") or produit["description"]
        
        nouveau_prix = input(f"Nouveau prix [{produit['prix']}]: ")
        if nouveau_prix:
            produit["prix"] = float(nouveau_prix)
            
        nouvelle_quantite = input(f"Nouvelle quantité [{produit['quantite']}]: ")
        if nouvelle_quantite:
            produit["quantite"] = int(nouvelle_quantite)
        
        print("✅ Produit modifié avec succès!")
        
    except ValueError:
        print("❌ ID, prix ou quantité invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la modification: {e}")

def supprimer_produit():
    """Supprime un produit"""
    print("\n--- Supprimer un produit ---")
    lister_produits()
    
    try:
        id_produit = int(input("\nID du produit à supprimer: "))
        produit = next((p for p in donnees["produits"] if p["id"] == id_produit), None)
        
        if not produit:
            print("❌ Produit non trouvé!")
            return
        
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer '{produit['nom']}'? (o/n): ")
        if confirmation.lower() == 'o':
            donnees["produits"] = [p for p in donnees["produits"] if p["id"] != id_produit]
            print("✅ Produit supprimé avec succès!")
        else:
            print("❌ Suppression annulée.")
            
    except ValueError:
        print("❌ ID invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la suppression: {e}")

def rechercher_produit():
    """Recherche un produit"""
    print("\n--- Rechercher un produit ---")
    terme = input("Entrez un nom ou description à rechercher: ").lower().strip()
    
    if not terme:
        print("❌ Veuillez entrer un terme de recherche!")
        return
    
    resultats = [p for p in donnees["produits"] 
                if terme in p["nom"].lower() or terme in p["description"].lower()]
    
    if not resultats:
        print("ℹ️  Aucun produit trouvé.")
        return
    
    print(f"\n🔍 {len(resultats)} produit(s) trouvé(s):")
    for produit in resultats:
        print(f"ID: {produit['id']} | {produit['nom']} | "
              f"Prix: {produit['prix']}€ | Stock: {produit['quantite']}")

# ==================== GESTION DES COMMANDES ====================

def gerer_commandes():
    """Menu de gestion des commandes"""
    while True:
        print("\n--- GESTION DES COMMANDES ---")
        print("1. Créer une commande")
        print("2. Lister les commandes")
        print("3. Voir les détails d'une commande")
        print("4. Supprimer une commande")
        print("0. Retour au menu principal")
        
        choix = input("Choisissez une option (0-4): ")
        
        if choix == "1":
            creer_commande()
        elif choix == "2":
            lister_commandes()
        elif choix == "3":
            details_commande()
        elif choix == "4":
            supprimer_commande()
        elif choix == "0":
            break
        else:
            print("❌ Option invalide!")

def creer_commande():
    """Crée une nouvelle commande"""
    print("\n--- Créer une commande ---")
    
    # Vérifier s'il y a des clients et produits
    if not donnees["clients"]:
        print("❌ Aucun client disponible. Veuillez d'abord ajouter un client.")
        return
    
    if not donnees["produits"]:
        print("❌ Aucun produit disponible. Veuillez d'abord ajouter des produits.")
        return
    
    try:
        # Sélection du client
        lister_clients()
        id_client = int(input("\nID du client: "))
        client = next((c for c in donnees["clients"] if c["id"] == id_client), None)
        
        if not client:
            print("❌ Client non trouvé!")
            return
        
        # Création de la commande
        id_commande = len(donnees["commandes"]) + 1
        commande = {
            "id": id_commande,
            "client_id": id_client,
            "client_nom": f"{client['prenom']} {client['nom']}",
            "date_creation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "articles": [],
            "statut": "En cours"
        }
        
        # Ajout des articles
        while True:
            print("\n--- Ajouter un article ---")
            lister_produits()
            
            id_produit = int(input("\nID du produit à ajouter (0 pour terminer): "))
            if id_produit == 0:
                break
                
            produit = next((p for p in donnees["produits"] if p["id"] == id_produit), None)
            if not produit:
                print("❌ Produit non trouvé!")
                continue
            
            quantite = int(input(f"Quantité de '{produit['nom']}' (stock disponible: {produit['quantite']}): "))
            
            if quantite > produit["quantite"]:
                print("❌ Quantité insuffisante en stock!")
                continue
            
            # Ajouter l'article à la commande
            commande["articles"].append({
                "produit_id": id_produit,
                "produit_nom": produit["nom"],
                "prix_unitaire": produit["prix"],
                "quantite": quantite,
                "sous_total": produit["prix"] * quantite
            })
            
            # Mettre à jour le stock
            produit["quantite"] -= quantite
            
            print(f"✅ {quantite} x '{produit['nom']}' ajouté à la commande")
            
            continuer = input("Ajouter un autre article? (o/n): ")
            if continuer.lower() != 'o':
                break
        
        if not commande["articles"]:
            print("❌ Commande annulée - aucun article ajouté")
            return
        
        # Calcul du total
        commande["total"] = sum(article["sous_total"] for article in commande["articles"])
        
        # Ajouter la commande
        donnees["commandes"].append(commande)
        print(f"✅ Commande #{id_commande} créée avec succès!")
        print(f"💰 Total: {commande['total']}€")
        
    except ValueError:
        print("❌ Valeur invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la création: {e}")

def lister_commandes():
    """Liste toutes les commandes"""
    print("\n--- Liste des commandes ---")
    if not donnees["commandes"]:
        print("ℹ️  Aucune commande enregistrée.")
        return
    
    for commande in donnees["commandes"]:
        print(f"Commande #{commande['id']} | Client: {commande['client_nom']} | "
              f"Date: {commande['date_creation']} | Total: {commande['total']}€ | "
              f"Statut: {commande['statut']}")

def details_commande():
    """Affiche les détails d'une commande"""
    print("\n--- Détails d'une commande ---")
    lister_commandes()
    
    try:
        id_commande = int(input("\nID de la commande à afficher: "))
        commande = next((c for c in donnees["commandes"] if c["id"] == id_commande), None)
        
        if not commande:
            print("❌ Commande non trouvée!")
            return
        
        print(f"\n📋 Commande #{commande['id']}")
        print(f"👤 Client: {commande['client_nom']}")
        print(f"📅 Date: {commande['date_creation']}")
        print(f"📊 Statut: {commande['statut']}")
        print("\n🛒 Articles:")
        for article in commande["articles"]:
            print(f"  - {article['quantite']} x {article['produit_nom']} "
                  f"({article['prix_unitaire']}€) = {article['sous_total']}€")
        print(f"\n💰 TOTAL: {commande['total']}€")
        
    except ValueError:
        print("❌ ID invalide!")
    except Exception as e:
        print(f"❌ Erreur: {e}")

def supprimer_commande():
    """Supprime une commande"""
    print("\n--- Supprimer une commande ---")
    lister_commandes()
    
    try:
        id_commande = int(input("\nID de la commande à supprimer: "))
        commande = next((c for c in donnees["commandes"] if c["id"] == id_commande), None)
        
        if not commande:
            print("❌ Commande non trouvée!")
            return
        
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer la commande #{id_commande}? (o/n): ")
        if confirmation.lower() == 'o':
            # Restaurer le stock des produits
            for article in commande["articles"]:
                produit = next((p for p in donnees["produits"] if p["id"] == article["produit_id"]), None)
                if produit:
                    produit["quantite"] += article["quantite"]
            
            donnees["commandes"] = [c for c in donnees["commandes"] if c["id"] != id_commande]
            print("✅ Commande supprimée avec succès!")
        else:
            print("❌ Suppression annulée.")
            
    except ValueError:
        print("❌ ID invalide!")
    except Exception as e:
        print(f"❌ Erreur lors de la suppression: {e}")

# ==================== STATISTIQUES ====================

def afficher_statistiques():
    """Affiche les statistiques de l'application"""
    print("\n--- STATISTIQUES ---")
    
    nb_clients = len(donnees["clients"])
    nb_produits = len(donnees["produits"])
    nb_commandes = len(donnees["commandes"])
    
    print(f"👥 Nombre de clients: {nb_clients}")
    print(f"📦 Nombre de produits: {nb_produits}")
    print(f"🛒 Nombre de commandes: {nb_commandes}")
    
    if nb_commandes > 0:
        total_ventes = sum(commande["total"] for commande in donnees["commandes"])
        commande_moyenne = total_ventes / nb_commandes
        print(f"💰 Chiffre d'affaires total: {total_ventes:.2f}€")
        print(f"📊 Panier moyen: {commande_moyenne:.2f}€")
    
    # Produits les plus vendus
    if nb_commandes > 0:
        print("\n🏆 Top produits:")
        ventes_par_produit = {}
        for commande in donnees["commandes"]:
            for article in commande["articles"]:
                produit_id = article["produit_id"]
                if produit_id not in ventes_par_produit:
                    ventes_par_produit[produit_id] = {
                        "nom": article["produit_nom"],
                        "quantite": 0,
                        "chiffre_affaires": 0
                    }
                ventes_par_produit[produit_id]["quantite"] += article["quantite"]
                ventes_par_produit[produit_id]["chiffre_affaires"] += article["sous_total"]
        
        top_produits = sorted(ventes_par_produit.items(), 
                            key=lambda x: x[1]["quantite"], 
                            reverse=True)[:5]
        
        for i, (produit_id, stats) in enumerate(top_produits, 1):
            print(f"  {i}. {stats['nom']} - {stats['quantite']} unités "
                  f"({stats['chiffre_affaires']:.2f}€)")

# ==================== MENU PRINCIPAL ====================

def menu_principal():
    """Fonction principale du menu"""
    charger_donnees()
    
    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option (0-5): ")
        
        if choix == "1":
            gerer_clients()
        elif choix == "2":
            gerer_produits()
        elif choix == "3":
            gerer_commandes()
        elif choix == "4":
            afficher_statistiques()
        elif choix == "5":
            sauvegarder_donnees()
        elif choix == "0":
            sauvegarder_avant_quitter = input("Voulez-vous sauvegarder avant de quitter? (o/n): ")
            if sauvegarder_avant_quitter.lower() == 'o':
                sauvegarder_donnees()
            print("👋 Au revoir!")
            break
        else:
            print("❌ Option invalide!")

# Point d'entrée de l'application
if __name__ == "__main__":
    menu_principal()