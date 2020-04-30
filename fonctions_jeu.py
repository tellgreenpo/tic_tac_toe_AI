import os
# J'ai pique les fonctions que tu as fais
def Rotation (T) :
    L0 = [T[2][0], T[1][0], T[0][0]]
    L1 = [T[2][1], T[1][1], T[0][1]]
    L2 = [T[2][2], T[1][2], T[0][2]]
    return [L0, L1, L2]

def partie_vainqueur(tableau):
    for ligne in range(2):  #check 3 en ligne ou colonne ou diag grace a rotation
        tableau_aux = tableau
        for ligne in tableau_aux:
            if ligne == ['o', 'o', 'o']:
                return [True, 'o']
            elif ligne == ['x', 'x', 'x']:
                return [True, 'x']
        if [tableau[0][0], tableau[1][1], tableau[2][2]] == ['o', 'o', 'o']:
            return [True, 'o']
        elif [tableau[0][0], tableau[1][1], tableau[2][2]] == ['x', 'x', 'x']:
            return [True, 'x']
        tableau_aux[:] = Rotation(tableau)
    match_nul = [True,'nul']
    for line in tableau:     #check si il y encore de la place pour jouer
        if 0 in line:
            return [False,'nul']
    return match_nul    #si rien n'a ete retourné, considere la partie alors come un match nul


def print_board(tableau):
    print("   |   |   ")
    print(" " + tableau[0][0] + " | " + tableau[0][1] + " | " + tableau[0][2] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + tableau[1][0] + " | " + tableau[1][1] + " | " + tableau[1][2] + "  ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + tableau[2][0] + " | " + tableau[2][1] + " | " + tableau[2][2] + "  ")
    print("   |   |   ")