# Écrivez un programme en Python qui implémente une calculatrice utilisant la notation polonaise inversée (RPN). 
# Le programme doit permettre à l'utilisateur d'entrer une expression RPN et de calculer le résultat. 
# Les fonctionnalités du programme doivent inclure l'utilisation de variables, de boucles, de conditions, de tableaux, de fonctions, de tris et de recherches.

# Définir une fonction pour évaluer une expression RPN
def eval_rpn(expr):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for token in expr.split():
        if token not in operators:
            try:
                token = int(token)
            except ValueError:
                token = float(token)
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                 result = a ** b
            stack.append(result)
    return stack[0]

# Demander à l'utilisateur d'entrer une expression RPN
expr = input("Entrez une expression RPN : ")

# Évaluer l'expression RPN
result = eval_rpn(expr)

# Afficher le résultat
print("Le résultat est :", result)

#Le programme peut également prendre en charge l'utilisation de variables, de boucles, de conditions, de tableaux, de fonctions, de tris et de recherches, selon les besoins spécifiques. 

# Définir une classe pour gérer les variables
class Variables:
    def __init__(self):
        self.vars = {}

    def get(self, var):
        return self.vars.get(var, 0)

    def set(self, var, val):
        self.vars[var] = val

# Définir une fonction pour évaluer une expression RPN avec des variables
def eval_rpn(expr, vars):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for token in expr.split():
        if token not in operators:
            try:
                token = int(token)
            except ValueError:
                token = float(token)
            stack.append(vars.get(token, token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                result = a ** b
            stack.append(result)
    return stack[0]

# Demander à l'utilisateur d'entrer des variables et une expression RPN
vars = Variables()
while True:
    var = input("Entrez une variable (ou appuyez sur Entrée pour continuer) : ")
    if not var:
        break


    # Définition de la classe Contact
class Contact:
    def __init__(self, nom, prenom, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.telephone}, {self.email}"

# Liste de contacts
contacts = []

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Entrez le nom : ")
    prenom = input("Entrez le prénom : ")
    telephone = input("Entrez le numéro de téléphone : ")
    email = input("Entrez l'adresse e-mail : ")
    contact = Contact(nom, prenom, telephone, email)
    contacts.append(contact)
    print("Le contact a été ajouté avec succès.")

# Fonction pour afficher la liste des contacts
def afficher_contacts():
    if len(contacts) == 0:
        print("Il n'y a aucun contact.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i+1}. {contact}")

# Fonction pour supprimer un contact
def supprimer_contact():
    index = int(input("Entrez l'index du contact à supprimer : ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Le contact a été supprimé avec succès.")
    else:
        print("Index invalide.")

#Ajouter une fonctionnalité qui permet de modifier un contact existant

# Fonction pour modifier un contact
def modifier_contact():
    index = int(input("Entrez l'index du contact à modifier : ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        nom = input(f"Entrez le nouveau nom ({contact.nom}) : ")
        prenom = input(f"Entrez le nouveau prénom ({contact.prenom}) : ")
        telephone = input(f"Entrez le nouveau numéro de téléphone ({contact.telephone}) : ")
        email = input(f"Entrez la nouvelle adresse e-mail ({contact.email}) : ")
        if nom:
            contact.nom = nom
        if prenom:
            contact.prenom = prenom
        if telephone:
            contact.telephone = telephone
        if email:
            contact.email = email
        print("Le contact a été modifié avec succès.")
    else:
        print("Index invalide.")

# Boucle principale pour afficher le menu
while True:
    print("\n1. Ajouter un contact")
    print("2. Afficher la liste des contacts")
    print("3. Supprimer un contact")
    print("4. Modifier un contact")
    print("5. Quitter")
    choix = input("Entrez votre choix : ")
    if choix == '1':
        ajouter_contact()
    elif choix == '2':
        afficher_contacts()
    elif choix == '3':
        supprimer_contact()
    elif choix == '4':
        modifier_contact()
    elif choix == '5':
        break
    else:
        print("Choix invalide.")

