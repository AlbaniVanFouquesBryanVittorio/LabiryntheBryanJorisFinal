# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    
    listedejoueurs=[]
    for i in nomsJoueurs:
      joueur=Joueur(i)
      listedejoueurs.append(joueur)
    joueurCourant=0
      

    return [listedejoueurs,joueurCourant]


def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    joueurs[0].append(joueur)
    

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    x=random.randint(0,len(joueurs[0])-1)
    joueurs[1]=x

def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                             qu'un joueur aura après la distribution
                             si ce paramètre vaut 0 on distribue le maximum
                             de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    if nbTresorMax==0:
      nbTresorMax=-1

    i=0
    y=0
    while i<nbTresors and getNbTresorsRestants(joueurs[0][-1]) != nbTresorMax:
      ajouterTresor(joueurs[0][y],i)
      i+=1
      if y==len(joueurs[0])-1:
        y=0
      else:
        y+=1
    


def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """ 
    joueurs[1]=joueurs[1]+1
    if joueurs[1]==len(joueurs[0]):
      joueurs[1]=0

def getNbJoueurs(joueurs):
    """
    retourne le nombre de joueurs participant à la partie
    paramètre: joueurs la liste des joueurs
    résultat: le nombre de joueurs de la partie
    """
    return len(joueurs)

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs[0][joueurs[1]]

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    tresorTrouve(joueurs[0][joueurs[1]])

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs[0][numJoueur])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return joueurs[1]

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    return getNom(joueurs[0][joueurs[1]])

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs[0][numJoueur])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs[0][numJoueur])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """
    return prochainTresor(joueurs[0][joueurs[1]])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    joueurCourantAFini=False

    if getNbTresorsRestants(joueurs[0][joueurs[1]])==0:
      joueurCourantAFini=True
    



if __name__=="__main__" :

  liste=ListeJoueurs(("Michel","Roger"))
  print(liste)  
  print("")

  oui=Joueur("oui")
  ajouterJoueur(liste, oui)
  print(liste)
  print("")
  
  initAleatoireJoueurCourant(liste)
  print(liste)
  print("")

  distribuerTresors(liste,nbTresors=24, nbTresorMax=3)
  print(liste)
  print("")

  changerJoueurCourant(liste)
  print(liste)
  print("")

  print(getNbJoueurs(liste))
  print("")

  print(getJoueurCourant(liste))
  print("")

  joueurCourantTrouveTresor(liste)

  print(nbTresorsRestantsJoueur(liste,0))
  print("oui")

  print(numJoueurCourant(liste))
  print("")

  print(nomJoueurCourant(liste))
  print("")

  print(nomJoueur(liste,1))
  print("")
  
  print(prochainTresorJoueur(liste,1))
  print("")

  print(tresorCourant(liste))
  print("")

  print(prochainTresorJoueur(liste,1))
  print("")

  print(joueurCourantAFini(liste))
