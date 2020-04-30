import random

# je laisse tomber les rotations car il faut les faire ensuite pour le choix


class IA:
    def __init__(self):
        self.previous_state = []
        self.previous_choice = ()
        self.tbl_positions = []
        self.tbl_memory = []

    def indice(self, tableau): # On suppose que le tableau est deja present
        return self.tbl_positions.index(tableau) #retourne index du tableau entre en argument

    def modif_memoire(self, save, partie_perdue): #prend en argument la situation ulterieur a la defaite
        if partie_perdue:
            index = self.indice(save)
            ligne = self.previous_choice[0]
            colonne = self.previous_choice[1]
            self.tbl_memory[index][ligne][colonne] = 0

    def case_occupee(self,tableau):
        i = self.indice(tableau)
        for line in [0,1,2]:
            for case in [0,1,2]:
                # met proba a zero si la case est occupe et sa proba n'est pas deja a 0
                if tableau[line][case] != 0 and self.tbl_memory[i][line][case] == 1:
                    self.tbl_memory[i][line][case] = 0


    def add_inconnu(self, tableau):
        if tableau not in self.tbl_positions: # regarder si la disposition existe ou pas dans la memoire
            self.tbl_positions[:] = self.tbl_positions + [tableau] # modifie totalement la base memoire en incrementant
            self.tbl_memory[:] = self.tbl_memory + [[[1,1,1],[1,1,1],[1,1,1]]] # ajoute proba memoire a la fin
            self.case_occupee(tableau)


    def ia_choix(self, tableau): #retourne une liste avec la ligne et la case choisie
        number = 0
        ligne = 0
        found = False
        arrayindextot = []
        arrayindex = []
        index = self.indice(tableau)
        number = sum(x.count(1) for x in self.tbl_memory[index]) #verifie le nombre de choix non perdants
        if number == 1: #si il y en a 1 seul on le cherche et on assigne sa ligne et sa case comme element d'une liste
            for line in self.tbl_memory[index]:
                colonne = 0
                for case in line:
                    if case == 1:
                        break
                    else:
                        colonne += 1
                else:
                # s'execute si la boucle se termine normalement => https://psung.blogspot.com/2007/12/for-else-in-python.html
                    ligne += 1
                    continue
                break
            choice = [ligne, colonne]
        elif number == 0: #aucun choix non perdant
            self.modif_memoire(self.previous_state,True) # si toutes les probas sont a 0, on met a zero le choix qui emmene a cette situation
            choice = [0,0]
        else:
            # On traverse chaque ligne
            for line in [0,1,2]:
                # on cree une liste avec les indices des choix non perdants
                arrayindex = [i for i,x in enumerate(self.tbl_memory[index][line]) if x == 1]
                # on ajoute cette liste par ligne a une liste general
                # qui contient a la fin les liste des index de choix non perdants par ligne
                if arrayindex: # c'est la meme chose que if arrayindex != [], les sequences vides sont consideres comme False
                    for case in arrayindex:
                        arrayindextot.append([line] + [case])
            print(arrayindextot)
            choice = random.choice(arrayindextot)
        #on met a jour l'etat ou l'on est pour le sauvegarder et le choix fait
        self.previous_state = tableau
        self.previous_choice = choice
        return choice

    def export(self):
        memory = open('data_memory_morpion.txt', 'w')
        memory.write(self.tbl_memory)
        memory.close()
        positions = open('data_positions_morpion.txt', 'w')
        positions.write(self.tbl_positions)
        positions.close()

    def download(self):
        memory = open('data_memory_morpion.txt', 'r')
        self.tbl_memory = memory.read()
        memory.close()
        positions = open('data_positions_morpion.txt', 'r')
        self.tbl_positions = positions.read()
        positions.close()