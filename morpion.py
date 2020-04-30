import IA_Morpion2
import fonctions_jeu

tableau_jeu = [[0,0,0],[0,0,0],[0,0,0]]
ia = IA_Morpion2.IA()

# Permet de charger la memoire enregistree
print("do you want to import data? [Y,N]")
response = input()
if response == 'Y':
    ia.download()

while True:
    # first part is computer pick
    ia.add_inconnu(tableau_jeu)
    ia.ia_choix(tableau_jeu)
    choix = fonctions_jeu.partie_vainqueur(tableau_jeu)
    tableau_jeu[choix[0]][choix[1]] = 'x'
    result = fonctions_jeu.partie_vainqueur(tableau_jeu)
    # Checks if the game is finished after pick
    if result[0]:
        if choix[1] != 'x':
            print("match nul")
        else:
            print(choix[1]+' gagne')
        break
    else:
        # Player pick
        fonctions_jeu.print_board(tableau_jeu)
        print("Entrez la ligne puis la colonne")
        ligne = int(input())
        colonne = int(input())
        tableau_jeu[ligne][colonne] = 'o'
        result = fonctions_jeu.partie_vainqueur(tableau_jeu)
        # Checks if game is finished after pick
        if result[0]:
            # if it is a draw nothing happens
            if choix[1] != 'o':
                print('match nul')
            else:
                # if it is a loss then modify the memory of the ai
                ia.modif_memoire(ia.tbl_positions,True)
                print(choix[1]+' gagne')
            break
        else:
            # continue the game and add board if needed
            ia.add_inconnu(tableau_jeu)

# Permet de sauvegarder la memoire modifiee de ce jeu
print('do you want to save the data? [Y,N]')
response = input()
if response == 'Y':
    ia.export()