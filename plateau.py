# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """
    
    nouveauPlateau=Matrice(7,7)
    setVal(nouveauPlateau,0,0,Carte(True,False,False,True))
    setVal(nouveauPlateau,0,2,Carte(True,False,False,False))
    setVal(nouveauPlateau,0,4,Carte(True,False,False,False))
    setVal(nouveauPlateau,0,6,Carte(True,True,False,False))
    setVal(nouveauPlateau,2,0,Carte(False,False,False,True))
    setVal(nouveauPlateau,2,2,Carte(False,False,False,True))
    setVal(nouveauPlateau,2,4,Carte(True,False,False,False))
    setVal(nouveauPlateau,2,6,Carte(False,True,False,False))
    setVal(nouveauPlateau,4,0,Carte(False,False,False,True))
    setVal(nouveauPlateau,4,2,Carte(False,False,True,False))
    setVal(nouveauPlateau,4,4,Carte(False,True,False,False))
    setVal(nouveauPlateau,4,6,Carte(False,True,False,False))
    setVal(nouveauPlateau,6,0,Carte(False,False,True,True))
    setVal(nouveauPlateau,6,2,Carte(False,False,True,False))
    setVal(nouveauPlateau,6,4,Carte(False,False,True,False))
    setVal(nouveauPlateau,6,6,Carte(False,True,True,False))

    # Réparti les pions en fonction du nombre de joueurs
    if nbJoueurs == 4:
      setVal(nouveauPlateau,0,0,Carte(True,False,False,True,0,[1]))
      setVal(nouveauPlateau,6,6,Carte(False,True,True,False,0,[2]))
      setVal(nouveauPlateau,0,6,Carte(True,True,False,False,0,[3]))
      setVal(nouveauPlateau,6,0,Carte(False,False,True,True,0,[4]))
    elif nbJoueurs==3:
      setVal(nouveauPlateau,0,0,Carte(True,False,False,True,0,[1]))
      setVal(nouveauPlateau,6,6,Carte(False,True,True,False,0,[2]))
      setVal(nouveauPlateau,0,6,Carte(True,True,False,False,0,[3]))
    elif nbJoueurs ==2 :
      setVal(nouveauPlateau,0,0,Carte(True,False,False,True,1,[1]))
      setVal(nouveauPlateau,6,6,Carte(False,True,True,False,0,[2]))
    else:
      setVal(nouveauPlateau,0,0,Carte(True,False,False,True,0,[1]))
      
    L=creerCartesAmovibles(1,nbTresors) 
   
    #Ajoute chaque carte une à une dans le plateau où il y a un zero
    for x in range(getNbLignes(nouveauPlateau)):
      for y in range(getNbColonnes(nouveauPlateau)):
         if nouveauPlateau[x][y]==0:
           setVal(nouveauPlateau,x,y,L[0])
           L.pop(0)

    

    #Réparti les trésors aléatoirement sur les cartes 
    ListeTrésor=[]
    Coord={1:[0,0],2:[0,1],3:[0,2],4:[0,3],5:[0,4],6:[0,5],7:[0,6],8:[1,0],9:[1,1],10:[1,2],11:[1,3],12:[1,4],13:[1,5],14:[1,6],15:[2,0],16:[2,1],17:[2,2],18:[2,3],19:[2,4],20:[2,5],21:[2,6],22:[3,0],23:[3,1],24:[3,2],25:[3,3],26:[3,4],27:[3,5],28:[3,6],29:[4,0],30:[4,1],31:[4,2],32:[4,3],33:[4,4],34:[4,5],35:[4,6],36:[5,0],37:[5,1],38:[5,2],39:[5,3],40:[5,4],41:[5,5],42:[5,6],43:[6,0],44:[6,1],45:[6,2],46:[6,3],47:[6,4],48:[6,5],49:[6,6]}

    print(nbTresors)
    for i in range(1,nbTresors+1):
      ListeTrésor.append(i)

    while len(ListeTrésor)!=0:
      Co=random.choice(list(Coord.keys()))
      a=Coord[Co][0]
      b=Coord[Co][1]
      mettreTresor(nouveauPlateau[a][b],ListeTrésor[0])
      del Coord[Co]
      ListeTrésor.pop(0)
    
    couplePlateau={"plateau" : nouveauPlateau, "carte" : L}

    return couplePlateau


def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    Dcarte={'Angle':16,'Jonction':6,'Droit':12}
    ListeCarteA=[]
    i=0
    x=random.randint(0,2)

    while i<34:
      if x==0:
        c=Carte(True,False,False,True)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Angle']
        Dcarte['Angle']=y-1
        if Dcarte['Angle']==0:
          if Dcarte['Jonction']==0:
            x=2
          elif Dcarte['Droit']==0:
            x=1
          else:
            x=random.randint(1,2)
        i=i+1

      elif x==1:
        c=Carte(True,False,False,False)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Jonction']
        Dcarte['Jonction']=y-1
        if Dcarte['Jonction']==0:
          if Dcarte['Angle']==0:
            x=2
          elif Dcarte['Droit']==0:
            x=0
          else:
            x=random.randrange(0,2,2)
        i=i+1

      elif x==2:
        c=Carte(True,False,True,False)
        tourneAleatoire(c)
        ListeCarteA.append(c)
        y=Dcarte['Droit']
        Dcarte['Droit']=y-1
        if Dcarte['Droit']==0:
          if Dcarte['Angle']==0:
            x=1
          elif Dcarte['Jonction']==0:
            x=0
          else:
            x=random.randint(0,1)
        i=i+1
      
    return ListeCarteA


def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    res=False
    carte=getVal(plateau["plateau"],lig,col)
    if numTresor==getTresor(carte):
        prendreTresor(carte)
        res=True
    return res


def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for lig in range(getNbLignes(plateau["plateau"])):
      for col in range(getNbColonnes(plateau["plateau"])):
        if getTresor(plateau["plateau"][lig][col])==numTresor:
          return (lig,col)
    return None

def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for lig in range(getNbLignes(plateau["plateau"])):
      for col in range(getNbColonnes(plateau["plateau"])):
        if possedePion(plateau["plateau"][lig][col],numJoueur):
          return (lig,col)
    return None

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    carte=getVal(plateau["plateau"],lin,col)
    if possedePion(carte,numJoueur):
      prendrePion(carte,numJoueur)
      

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    carte=getVal(plateau["plateau"],lin,col)
    poserPion(carte,numJoueur)


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    carte1=(plateau["plateau"][ligD][colD])
    carte2=(plateau["plateau"][ligA][colA])

    listeAccessible=[]

    for i in range(4):
      listeAccessible.append(plateau["plateau"][ligD][colD])

    listeAccessible=[plateau["plateau"][ligD][colD+1], plateau["plateau"][ligD][colD],plateau["plateau"][ligD][colD],plateau["plateau"][ligD][colD]]

    while carte1!=carte2:
      
      carte3=(plateau[ligD][colD+1])
      if passageNord(carte1,carte3):        
        carte1=(plateau[ligD][colD+1])
      else:
        carte3=(plateau[ligD][colD-1])

        carte3=(plateau[ligD][colD-1])
        if passageSud(carte1,carte3):        
          carte1=(plateau[ligD][colD-1])
        else:
          carte3=(plateau[ligD][colD+1])
      
          carte3=(plateau[ligD+1][colD])
          if passageOuest(carte1,carte3):        
            carte1=(plateau[ligD+1][colD])
          else:
            carte3=(plateau[ligD-1][colD])
      
            carte3=(plateau[ligD-1][colD])
            if passageEst(carte1,carte3):        
              carte1=(plateau[ligD-1][colD])
            else:
              carte3=(plateau[ligD+1][colD])
      
      
def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass

if __name__=="__main__" :
  p=Plateau(2,10)
  creerCartesAmovibles(1,5)
 
  #print(p["plateau"][0][0])

  prendreTresorPlateau(p,0,0,1)

  #print(p["plateau"][0][0])

  print(getCoordonneesTresor(p,2))
  
  print(getCoordonneesJoueur(p,1))

  prendrePionPlateau(p,0,2,5)

  poserPionPlateau(p,0,2,3)
