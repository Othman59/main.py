# Exo_1_Créer un algorithme qui incrémente une variable de 1 et continue tant que cette même variable est inférieur à 10.
# count = 0  # initialisation de la variable count à 0

# while count < 10:  # tant que la valeur est inférieur à 10
#     count += 1  # incrémente la variable count de 1
#     print(count)  # affiche la valeur actuelle de count


# #Exo_3_réer un algorithme qui obtient de façon aléatoire un chiffre entre 0 et 100 inclus, puis de vérifier si le résultat est pair ou impair.
# import random

# nombre = random.randint(0, 100)

# if nombre % 2 == 0:
#     print(nombre, "est pair")
# else:
#     print(nombre, "est impair")

# a = 10
# b = 20

# print("Valeurs avant l'échange: a =", a, "b =", b)

# temp = a
# a = b
# b = temp

# print("Valeurs après l'échange: a =", a, "b =", b)

# #Exo_4_Créer un algorithme qui va récupérer en paramètre un chiffre entre 1 et 3. Faire une action selon le résultat attendu : 
# # 1 retournez “un”, 
# # 2 retournez “deux”, 
# # 3 retournez “trois”

# def retourner_chiffre(chiffre):
#     if chiffre == 1:
#         return "un"
#     elif chiffre == 2:
#         return "deux"
#     elif chiffre == 3:
#         return "trois"
#     else:
#         return "Le chiffre doit être entre 1 et 3"

# chiffre = 2
# resultat = retourner_chiffre(chiffre)
# print(resultat) 

# #Exo_5_Créer un algorithme qui génère 10 nombres aléatoires, puis les enregistre dans une liste.
# import random

# nombres_aleatoires = []

# for i in range(10):
#     nombre = random.randint(1, 100)
#     nombres_aleatoires.append(nombre)

# print(nombres_aleatoires)

# # #Exo_6_Créer un algorithme qui, à partir d’une liste de chiffres, nous indique qui est le plus grand et qui est le plus petit.
# def trouver_min_max(liste_chiffres):
#      """
#      Cette fonction prend en entrée une liste de chiffres et retourne le plus petit et le plus grand nombre de la liste.
#      """
#      min_chiffre = float('inf')
#      max_chiffre = float('-inf')

#      for chiffre in liste_chiffres:
#          if chiffre < min_chiffre:
#              min_chiffre = chiffre
#          if chiffre > max_chiffre:
#              max_chiffre = chiffre

#      return min_chiffre, max_chiffre

# liste = [4, 2, 9, 1, 7, 5, 8]
# min_chiffre, max_chiffre = trouver_min_max(liste)
# print(f"Le plus petit chiffre est {min_chiffre} et le plus grand chiffre est {max_chiffre}.")

# #Exo_7_Créer un algorithme , qui va générer un tableau de taille 10. Pour chaque ligne de ce tableau, insérer un tableau de taille 10.
# tableau = []
# for i in range(10):
#     ligne = []
#     for j in range(10):
#         ligne.append(0)
#     tableau.append(ligne)
# print(tableau)


##Exo_8_Créer un algorithme , qui , en récupérant une variable hauteur, est capable de dire combien de boite de conserve seront nécessaire pour constituer une pyramide de rangement(exemple avec une hauteur 4 = 10 boites)
# hauteur = int(input("Entrez la hauteur de la pyramide : "))
# nb_boites = 0

# for i in range(1, hauteur+1):
#   nb_boites += i**2

# print("Pour une pyramide de hauteur", hauteur, "il faudra", nb_boites, "boîtes.")

# #Exo_9_Créer un algorithme, qui demande en paramètre la taille d’un carré. L’algorithme affichera ensuite le carré en fonction de la valeur saisie précédemment.
# #Si mon carré a une taille de 6 alors : 

# def afficher_carre(taille):
#     for i in range(taille):
#         for j in range(taille):
#             print("*", end=" ")
#         print(resultat)

# taille_carre = int(input("Entrez la taille du carré : "))
# afficher_carre(taille_carre)

# #Si mon carré a une taille de 4 alors :

# def carre(taille):
#     for i in range(taille):
#         for j in range(taille):
#             print("*", end="")
#         print()

#Créer un algorithme pour simuler le déplacement (2D) d’un rubik's cube.

# Définir une liste représentant les couleurs des faces du Rubik's Cube
# colors = ["white", "yellow", "green", "blue", "red", "orange"]

# # Définir une liste représentant l'état initial du Rubik's Cube
# cube = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]]

# # Fonction pour effectuer une rotation de 90 degrés dans le sens des aiguilles d'une montre d'une face donnée
# def rotate(face):
#     temp = [cube[face][0], cube[face][1], cube[face][2]]
#     cube[face][0] = cube[face-2][0]
#     cube[face][1] = cube[face-1][0]
#     cube[face][2] = cube[face][0]
#     cube[face-2][0] = cube[face-2][2]
#     cube[face-1][0] = cube[face-2][1]
#     cube[face][0] = cube[face-2][0]
#     cube[face-2][2] = cube[face][2]
#     cube[face-2][1] = cube[face-1][2]
#     cube[face-2][0] = temp[0]
    
# # Fonction pour dessiner le Rubik's Cube
# def draw_cube():
#     for i in range(6):
#         for j in range(3):
#             for k in range(3):
#                 if i == 0:
#                     ([j, j+1, j+1, j], [2-k, 2-k, 3-k, 3-k], colors[cube[i][j]])
#                 elif i == 1:
#                     ([j, j+1, j+1, j], [k, k, 1-k, 1-k], colors[cube[i][j]])
#                 elif i == 2:
#                     ([k, k+1, k+1, k], [2-j, 2-j, 3-j, 3-j], colors[cube[i][j]])
#                 elif i == 3:
#                     ([k, k+1, k+1, k], [j, j, 1-j, 1-j], colors[cube[i][j]])
#                 elif i == 4:
#                     ([2-k, 2-k+1, 2-k+1, 2-k], [j, j, 1-j, 1-j], colors[cube[i][j]])
#                 elif i == 5:
#                     ([k, k+1, k+1, k], [2-j, 2-j, 1-j, 1-j], colors[cube[i][j]])

# # Rotation de la face avant
# rotate(0)

# # Dessiner le Rubik's Cube
# draw_cube()

# Afficher le Rubik's Cube

#Exercice Final : Jeu de la vie 

# import random

# # Définir la taille de la grille
# grid_size = 10

# # Initialiser la grille avec des cellules aléatoirement vivantes ou mortes
# grid = [[random.choice([0,1]) for _ in range(grid_size)] for _ in range(grid_size)]

# # Définir la fonction pour calculer le nombre de voisins vivants d'une cellule
# def count_neighbors(x, y):
#     count = 0
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == 0 and j == 0:
#                 continue
#             if x + i < 0 or x + i >= grid_size:
#                 continue
#             if y + j < 0 or y + j >= grid_size:
#                 continue
#             if grid[x+i][y+j] == 1:
#                 count += 1
#     return count

# # Définir la fonction pour mettre à jour l'état de la grille à chaque tour
# def update_grid():
#     new_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
#     for i in range(grid_size):
#         for j in range(grid_size):
#             neighbors = count_neighbors(i, j)
#             if grid[i][j] == 1:
#                 if neighbors == 2 or neighbors == 3:
#                     new_grid[i][j] = 1
#             else:
#                 if neighbors == 3:
#                     new_grid[i][j] = 1
#     return new_grid

# # Boucle principale de simulation
# while True:
#     # Afficher la grille
#     for row in grid:
#         print(' '.join(['*' if cell == 1 else '-' for cell in row]))
#     print()

#     # Mettre à jour la grille
#     grid = update_grid()

#     # Attendre avant de passer au jour suivant
#     input("Appuyez sur Entrée pour passer au jour suivant...")

#Tri  à bulles

# tableau = [64,30,32,59,11,25]

# n = len(tableau) #Récupération de la taille du tableau

#Boucle qui va permettre de parcourir le tableau et répéter le processus de comparaison et d'échange
# for i in range(n):
#     for j in range(n-i-1):
#         if tableau[j] > tableau[j+1] :
#             tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
        
# print(f"Tri du tableau : {tableau}")

# Tri fusion

# tableau = [64,30,32,59,11]
# def fusion(gauche, droite) :
#     resultat = []

#     i=j=0

#     while i < len(gauche) and j<len(droite) :
#         if gauche[i] < droite[j]:
#             resultat.append(gauche[i])
#             i+=1
#         else : 
#             resultat.append(droite[j])
#             j+=1

#     resultat += gauche[i:]
#     resultat += droite[j:]
#     return resultat

# def tri_fusion(tableau) :

#     if len(tableau) <= 1 :
#         return tableau

#     mediane = len(tableau) // 2
#     partieGauche = tableau[:mediane]
#     partieDroite = tableau[mediane:]

#     partieGauche = tri_fusion(partieGauche)
#     partieDroite = tri_fusion(partieDroite)

#     return fusion(partieGauche,partieDroite)

#Refaire le tri de tableau rapide et trier les chaines de caractère 


#Tri  à bulles

# tableau = [64,30,32,59,11,25]

# n = len(tableau) #Récupération de la taille du tableau

# #Boucle qui va permettre de parcourir le tableau et répéter le processus de comparaison et d'échange
# for i in range(n):
#      for j in range(n-i-1):
#          if tableau[j] > tableau[j+1] :
#              tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
        
# print(f"Tri du tableau : {tableau}")

# # Tri fusion

# tableau = [64,30,32,59,11]
# def fusion(gauche, droite) :
#      resultat = []

#      i=j=0

#      while i < len(gauche) and j<len(droite) :
#          if gauche[i] < droite[j]:
#              resultat.append(gauche[i])
#              i+=1
#          else : 
#              resultat.append(droite[j])
#              j+=1

#      resultat += gauche[i:]
#      resultat += droite[j:]
#      return resultat

# def tri_fusion(tableau) :

#      if len(tableau) <= 1 :
#          return tableau

#      mediane = len(tableau) // 2
#      partieGauche = tableau[:mediane]
#      partieDroite = tableau[mediane:]

#      partieGauche = tri_fusion(partieGauche)
#      partieDroite = tri_fusion(partieDroite)

#      return fusion(partieGauche,partieDroite)



# tri = tri_fusion(tableau)
# print(tri)

# # Tri Rapide

# def partition(tableau, debut, fin) :
#      pivot = tableau[fin]
#      i = debut -1
    
#      for j in range(debut, fin) :
#          if tableau[j] < pivot :
#              i += 1
#              tableau[i],tableau[j] = tableau[j], tableau[i]
    
#      tableau[i+1], tableau[fin] = tableau[fin], tableau[i+1]

#      print(tableau)

#      return i + 1

# def tri_rapide(tableau, debut, fin) :
#      if debut < fin :
#          pivot_index = partition(tableau,debut,fin)
#          tri_rapide(tableau,debut,pivot_index-1)
#          tri_rapide(tableau, pivot_index +1, fin)

# tableau = [64,30,32,87,59,11,16]
# tri_rapide(tableau, 0, len(tableau)-1)
# print(tableau)

# ######

# #Refaire 

# # Tri rapide pour les entiers
# def partition(tableau, debut, fin):
#     pivot = tableau[fin]
#     i = debut - 1

#     for j in range(debut, fin):
#         if tableau[j] < pivot:
#             i += 1
#             tableau[i], tableau[j] = tableau[j], tableau[i]

#     tableau[i+1], tableau[fin] = tableau[fin], tableau[i+1]

#     return i+1

# def tri_rapide_entiers(tableau, debut, fin):
#     if debut < fin:
#         pivot_index = partition(tableau, debut, fin)
#         tri_rapide_entiers(tableau, debut, pivot_index-1)
#         tri_rapide_entiers(tableau, pivot_index+1, fin)

# tableau_entiers = [64, 30, 32, 87, 59, 11, 16]
# tri_rapide_entiers(tableau_entiers, 0, len(tableau_entiers)-1)
# print(tableau_entiers)

# # Tri rapide pour les chaînes de caractères
# def partition_chaines(tableau, debut, fin):
#     pivot = tableau[fin]
#     i = debut - 1

#     for j in range(debut, fin):
#         if tableau[j].compareto(pivot) < 0:
#             i += 1
#             tableau[i], tableau[j] = tableau[j], tableau[i]

#     tableau[i+1], tableau[fin] = tableau[fin], tableau[i+1]

#     return i+1

# def tri_rapide_chaines(tableau, debut, fin):
#     if debut < fin:
#         pivot_index = partition_chaines(tableau, debut, fin)
#         tri_rapide_chaines(tableau, debut, pivot_index-1)
#         tri_rapide_chaines(tableau, pivot_index+1, fin)

# tableau_chaines = ["orange", "pomme", "banane", "kiwi", "fraise", "abricot"]
# tri_rapide_chaines(tableau_chaines, 0, len(tableau_chaines)-1)
# print(tableau_chaines)


# # Recherche Séquentielle

# tableau = ["Toto", "Tata", "Toutou"]
# valeur = "Tata"
# trouve = False

# for i in tableau :
#     if i == valeur :
#         trouve = True
#         print(i)
#         print("valeur trouvée")
#         break

# if not trouve:
#     print("valeur non trouvée")

# # Recherche binaire 

# def binary_search(arr, x):
#     """
#     Recherche binaire pour trouver l'index de l'élément x dans la liste triée arr.
#     Retourne -1 si l'élément n'est pas présent dans la liste.
#     """
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] < x:
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             return mid
#     return -1


# film = [
#     {
#         "titre" : "Film1", 
#         "genre" : "Genre",

#     }
# ] 
# print(film)
# film.append({"titre": "Film2,", "genre": "Genre2"})
# print(film)


# # Initialisation de la bibliothèque
# bibliotheque = []

# # Fonction pour ajouter un livre à la bibliothèque
# def ajouter_livre():
#     titre = input("Entrez le titre du livre : ")
#     auteur = input("Entrez le nom de l'auteur : ")
#     bibliotheque[titre] = auteur
#     print("Le livre a été ajouté avec succès.")

# # Supprimer un livre 
# def supprimer_livre():
#     titre = input("Titre du livre : ")
#     for livre in bibliotheque:
#         if livre["titre"] == titre:
#             bibliotheque.remove(livre)
#             print("Le livre a été supprimé avec succès.")
#             return
#     print("Le livre n'a pas été trouvé.")

# # Rechercher un livre par titre
# def rechercher_livre():
#     titre = input("Titre du livre : ")
#     for livre in bibliotheque:
#         if livre["titre"] == titre:
#             print(f'Titre: {livre["titre"]}, Auteur: {livre["auteur"]}, Année de publication: {livre["Année"]}')
#             return
#     print("Le livre n'a pas été trouvé.")

# # Afficher tous les livres
# def afficher_livres():
#     if len(bibliotheque) == 0:
#         print("La bibliothèque est vide.")
#     else:
#         for livre in bibliotheque:
#             print(f'Titre: {livre["titre"]}, Auteur: {livre["auteur"]}, Année de publication: {livre["annee"]}')

# # Trier les livres par titre
# def trier_livres():
#     bibliotheque.sort(key=lambda x: x["titre"])
#     print("La bibliothèque a été triée avec succès par titre.")

# # Menu principal
# while True:
#     print("""
#     1. Ajouter un livre à la bibliothèque
#     2. Supprimer un livre de la bibliothèque
#     3. Rechercher un livre par titre
#     4. Afficher tous les livres
#     5. Trier les livres par titre
#     6. Quitter
#     """)
#     choix = input("Entrez votre choix : ")
#     if choix == "1":
#         ajouter_livre()
#     elif choix == "2":
#         supprimer_livre()
#     elif choix == "3":
#         rechercher_livre()
#     elif choix == "4":
#         afficher_livres()
#     elif choix == "5":
#         trier_livres()
#     elif choix == "6":
#         print("Au revoir !")
#         break
#     else:
#         print("Choix invalide. Veuillez réessayer.")        



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


