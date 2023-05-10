# Écrivez un programme en Python qui permet de gérer un carnet d'adresses. 
# Le carnet d'adresses doit contenir des noms et des numéros de téléphone. 
# Le programme doit permettre à l'utilisateur d'ajouter des contacts, de supprimer des contacts, de rechercher des contacts par nom ou par numéro, d'afficher tous les contacts et de quitter le programme. 
# Les fonctionnalités du programme doivent inclure l'utilisation de variables, de boucles, de conditions, de tableaux, de fonctions, de tris et de recherches.

contact = [] #initialisation de la liste des contacts

def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    tel = input("Entrez le numéro de téléphone : ")
    contact = (nom, tel) # créer un tuple pour stocker le nom et le numéro de téléphone
    print("Le contact a été ajouté avec succès.")

def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer : ")
    for contact in contact:
        if contact[0] == nom: # si le nom du contact est trouvé
            contact.remove(contact) # supprimer le contact de la liste
            print("Le contact a été supprimé avec succès.")
            return
    print("Le contact n'a pas été trouvé.")

def rechercher_contact_par_nom():
    nom = input("Entrez le nom du contact à rechercher : ")
    found = False
    for contact in contact:
        if contact[0] == nom: # si le nom du contact est trouvé
            print("Nom :", contact[0], " Numéro de téléphone :", contact[1])
            found = True
    if not found:
        print("Le contact n'a pas été trouvé.")

def rechercher_contact_par_tel():
    tel = input("Entrez le numéro de téléphone du contact à rechercher : ")
    found = False
    for contact in contact:
        if contact[1] == tel: # si le numéro de téléphone du contact est trouvé
            print("Nom :", contact[0], " Numéro de téléphone :", contact[1])
            found = True
    if not found:
        print("Le contact n'a pas été trouvé.")

def afficher_contacts():
    if not contact: # si la liste des contacts est vide
        print("Il n'y a aucun contact dans le carnet d'adresses.")
    else:
        print("Voici la liste des contacts :")
        for contact in sorted(contact): # trier les contacts par ordre alphabétique
            print("Nom :", contact[0], " Numéro de téléphone :", contact[1])

def quitter():
    print("Merci d'avoir utilisé le carnet d'adresses.")
    exit()

while True:
    # afficher le menu et demander à l'utilisateur de saisir une option
    
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un contact")
    print("2. Supprimer un contact")
    print("3. Rechercher un contact par nom")
    print("4. Rechercher un contact par numéro de téléphone")
    print("5. Afficher tous les contacts")
    print("6. Quitter le programme")
    choix = input("Entrez le numéro de l'option : ")
    
    # exécuter l'option choisie
    if choix == '1':
        ajouter_contact()
    elif choix == '2':
        supprimer_contact()
    elif choix == '3':
        rechercher_contact_par_nom()
    elif choix == '4':
        rechercher_contact_par_tel()
    elif choix == '5':
        afficher_contacts()
    elif choix == '6':
        quitter()
    else:
        print("Option invalide. Veuillez réessayer.")



