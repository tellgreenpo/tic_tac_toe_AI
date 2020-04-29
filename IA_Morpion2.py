import random

#je laisse tomber les rotations pour pas a avoir
#def rotation(array): #roatation simple du tableau de jeu
    #line1 = [array[0][2], array[1][2], array[2][2]]
    #line2 = [array[0][1], array[1][1], array[2][1]]
    #line3 = [array[0][0], array[1][0], array[2][0]]
    #return [line1, line2, line3]


class IA:
    def __init__(self):
        self.previous_state = []
        self.previous_choice = ()
        self.tbl_positions = []
        self.tbl_memory = []

    def index(self, tableau): # On suppose que le tableau est deja present
        return self.tbl_positions.index(tableau) #retourne index du tableau entre en argument

    def modif_memoire(self, save, partie_perdue): #prend en argument la situation ulterieur a la defaite
        if partie_perdue:
            index = self.index(self,save)
            ligne = self.previous_choice[0]
            colonne = self.previous_choice[1]
            self.tbl_memory[index][ligne][colonne] = 0


    def add_inconnu(self, tableau):
        if tableau not in self.tbl_positions: #regarder si la disposition existe ou pas dans la memoire
            self.tbl_positions[:] = self.tbl_positions + [tableau] #modifie totalement la base memoire en incrementant(au cas ou mdrr)
            #self.tbl_positions.append(self,tableau) ?

    def case_occupee(self,tableau):
        i = self.index(self,tableau)
        for line in tableau:
            for case in line:
                if case != 0 and self.tbl_memory[i][line][case] == 1:
                    self.tbl_memory[i][line][case] = 0

    def ia_choix(self, tableau): #retourne une liste avec la ligne et la case choisie
        number = 0
        line = 0
        case = 0
        found = False
        index = self.index(self,tableau)
        number = sum(x.count(1) for x in self.tbl_memory[index]) #verifie le nombre de choix non perdants
        if number == 1: #si il y en a 1 seul on le cherche et on assigne sa ligne et sa case comme element d'une liste
            while not found and line < 3:
                while not found and case < 3:
                    if self.tbl_memory[index][line][case] == 1:
                        found = True
                    else:
                        case += 1
                line += 1
            choice = [line,case]
        elif number == 0: #aucun choix non perdant
            self.modif_memoire(self,self.previous_state,True) # si toutes les probas sont a 0, on met a zero le choix qui emmene a cette situation
            choice = [0,0]
        else:
            # On traverse chaque ligne
            arrayindextot = []
            arrayindex = []
            for line in tableau:
                arrayindex[:] = [i for i,x in enumerate(self.tbl_memory[index][line]) if x == 1]    #on cree une liste avec les indexs des choix non perdants
                     # on ajoute cette liste par ligne a une liste general qui contient a la fin les liste des index de choix non perdants par ligne
                arrayindextot.append(arrayindex)
            choice_line = random.choice(arrayindextot) # on choisit au hazard une ligne avec au moins un choix non perdant
            choice_case = random.choice(choice_line) #on choisit au hazard une case de la ligne
            choice = [choice_line,choice_case]
        #on met a jour l'etat ou l'on est pour le sauvegarder et le choix fait
        self.previous_state = tableau
        self.previous_choice = choice
        return choice
