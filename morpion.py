#create game grid
def initier_grille(monTab):
    return(monTab)

#display game grid
def afficher_grille(monTab):
    print(monTab[0])
    print(monTab[1])
    print(monTab[2])

monTab=[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']

#ask X stroke
def demander_coup_croix(monTab):
     y=int(input("Entrez une colone: "))
     x=int(input("Entrez une ligne: "))
     x=x-1
     y=y-1
     if monTab[x][y] != " ":
         print("Coup impossible.")
         demander_coup_croix(monTab)
     else:
         monTab[x][y]="x"
         print(monTab[0])
         print(monTab[1])
         print(monTab[2])
     return monTab

#ask O stroke
def demander_coup_rond(monTab):
     y=int(input("Entrez une colone: "))
     x=int(input("Entrez une ligne: "))
     x=x-1
     y=y-1
     if monTab[x][y] != " ":
         print("Coup impossible.")
         demander_coup_rond(monTab)
     else:
         monTab[x][y]="o"
         print(monTab[0])
         print(monTab[1])
         print(monTab[2])
     return monTab

#X win
def gagner_croix(tab):
    continu = False
    if tab[0][0]==tab[0][1] and tab[0][0]==tab[0][2] and tab[0][0]!=" " and tab[0][0]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[1][0]==tab[1][1] and tab[1][0]==tab[1][2] and tab[1][0]!=" " and tab[1][0]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[2][0]==tab[2][1] and tab[2][0]==tab[2][2] and tab[2][0]!=" " and tab[2][0]=="x":
        print("Le joueur avec les  croix a gagné !")
    elif tab[0][0]==tab[1][0] and tab[0][0]==tab[2][0] and tab[0][0]!=" " and tab[0][0]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[0][1]==tab[1][1] and tab[0][1]==tab[2][1] and tab[0][1]!=" " and tab[0][1]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[0][2]==tab[1][2] and tab[0][2]==tab[2][2] and tab[0][2]!=" " and tab[0][2]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[0][0]==tab[1][1] and tab[0][0]==tab[2][2] and tab[0][0]!=" " and tab[0][0]=="x":
        print("Le joueur avec les croix a gagné !")
    elif tab[0][2]==tab[1][1] and tab[0][2]==tab[2][0] and tab[0][2]!=" " and tab[0][2]=="x":
        print("Le joueur avec les croix a gagné !")
    else :
        continu = True
    return continu

#O win
def gagner_rond(tab):
    continu = False
    if tab[0][0]==tab[0][1] and tab[0][0]==tab[0][2] and tab[0][0]!=" " and tab[0][0]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[1][0]==tab[1][1] and tab[1][0]==tab[1][2] and tab[1][0]!=" " and tab[1][0]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[2][0]==tab[2][1] and tab[2][0]==tab[2][2] and tab[2][0]!=" " and tab[2][0]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[0][0]==tab[1][0] and tab[0][0]==tab[2][0] and tab[0][0]!=" " and tab[0][0]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[0][1]==tab[1][1] and tab[0][1]==tab[2][1] and tab[0][1]!=" " and tab[0][1]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[0][2]==tab[1][2] and tab[0][2]==tab[2][2] and tab[0][2]!=" " and tab[0][2]=="o":
        print("Le joueur avec les ronds a gagné !")
    elif tab[0][0]==tab[1][1] and tab[0][0]==tab[2][2] and tab[0][0]!=" " and tab[0][0]=="o":
        print("Le joueur avec les ronds a gagné !")
        
    elif tab[0][2]==tab[1][1] and tab[0][2]==tab[2][0] and tab[0][2]!=" " and tab[0][2]=="o":
        print("Le joueur avec les ronds a gagné !")
    else :
        continu = True
    return continu

#change player
def changer_joueur(coup_jouer, monTab):
    variable_utile=True
    while variable_utile==True:
        if coup_jouer%2==0:
             print("Au croix de jouer:")
             montab = demander_coup_croix(monTab)
             coup_jouer+=1
        elif coup_jouer%2!=0:
             print("Au rond de jouer:")
             demander_coup_rond(monTab)
             coup_jouer+=1
        if gagner_croix(monTab) == False:
            variable_utile = gagner_croix(monTab)
        elif gagner_rond(monTab) == False:
           variable_utile = gagner_rond(monTab)
    return(coup_jouer)

#recursive function to play
def jouer(monTab):
    initier_grille(([' ',' ',' '],[' ',' ',' '],[' ',' ',' ']))
    afficher_grille(monTab)
    changer_joueur(0, monTab)
    #ask to retry
    recomencer =input(f"\nVoulez vous recommencer ?: ")
    if recomencer in ('oui'):
        jouer(([' ',' ',' '],[' ',' ',' '],[' ',' ',' ']))
jouer(monTab)