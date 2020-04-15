# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random

#AlbaniVanfouquesThepinier
#Joris


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
  """
  permet de créer une carte:
  paramètres:
  nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
  tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
  pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
  """
  
  C={'nord':nord,'est':est,'sud':sud,'ouest':ouest,'tresor':tresor,'pions':pions}
  return C

def estValide(c):
  """
  retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
  paramètre: c une carte
  """
  res=True
  cpt=0
  if c['nord']==True:
    cpt=cpt+1

  if c['sud']==True:
    cpt=cpt+1

  if c['est']==True:
    cpt=cpt+1

  if c['ouest']==True:
    cpt=cpt+1
  
  if cpt>2:
    res=False

  return res

def murNord(c):
  """
  retourne un booléen indiquant si la carte possède un mur au nord
  paramètre: c une carte
  """
  return  c['nord']

def murSud(c):
  """
  retourne un booléen indiquant si la carte possède un mur au sud
  paramètre: c une carte
  """
  return  c['sud']

def murEst(c):
  """
  retourne un booléen indiquant si la carte possède un mur à l'est
  paramètre: c une carte
  """
  return  c['est']
  
def murOuest(c):
  """
  retourne un booléen indiquant si la carte possède un mur à l'ouest
  paramètre: c une carte
  """
  return  c['ouest'] 

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c['pions']

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    for i in listePions:
        c['pions'].append(i)

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    res=len(c['pions'])

    return res

def possedePion(c,pion):
  """
  retourne un booléen indiquant si la carte possède le pion passé en paramètre
  paramètres: c une carte
              pion un entier compris entre 1 et 4
  """
  res=False
  
  if pion in c['pions']:
    res=True

  return res

def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    res=c['tresor'] 
    return res

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=getTresor(c)
    c['tresor']= None

    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=getTresor(c)
    c['tresor']=tresor
  

    return res

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    
    listeP=c.get('pions')
    for i in range(len(listeP)):
      if listeP[i]==pion:
        listeP.pop(i)
        break

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    listeP=c.get('pions')
    listeP.append(pion)
    
def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
  
    nord=c['nord']
    est=c['est']
    sud=c['sud']
    ouest=c['ouest']

    c['ouest']=sud
    c['sud']=est
    c['est']=nord
    c['nord']=ouest
  
def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """

    nord=c['nord']
    est=c['est']
    sud=c['sud']
    ouest=c['ouest']

    c['nord']=est
    c['ouest']=nord
    c['sud']=ouest
    c['est']=sud
 
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    x=random.randint(0,3)
    i=0
    while i<x:
      tournerHoraire(c)
      i=i+1
    
def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    if c['nord']==True:
      bN=1
    else:
      bN=0
  
    if c['est']==True:
      bE=10
    else:
      bE=0

    if c['sud']==True:
      bS=100
    else:
      bS=0

    if c['ouest']==True:
      bO=1000
    else:
      bO=0
    
    res=bN+bE+bS+bO
    
    res=str(res)
    res=(int(res,2))
    return res
    
def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """   
    if code==0:
      c['nord']=False 
      c['est']=False 
      c['sud']=False 
      c['ouest']=False 

    else:
      i=0
      x1=0
      x2=0
      x3=0
      x4=0
      while i <4:
        quotient=code//2
        reste=code%2
        code=quotient

        if i==0:
          x1=reste
        elif i==1:
          x2=reste
        elif i==2:
          x3=reste
        elif i==3:
          x4=reste
        i=i+1

    if x1==1:
      x1=True
    else:
      x1=False
    if x2==1:
      x2=True
    else:
      x2=False
    if x3==1:
      x3=True
    else:
      x3=False
    if x4==1:
      x4=True
    else:
      x4=False

    c['nord']=x1
    c['est']=x2
    c['sud']=x3
    c['ouest']=x4

def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    i=int(coderMurs(c))
    print('i:',i)
    res=listeCartes[i]
    return res

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte2['sud']==False and carte1['nord']==False:
      res = True

    return res

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte2['nord']==False and carte1['sud']==False:
      res = True

    return res
    

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    res=False
    if carte2['est']==False and carte1['ouest']==False:
      res = True

    return res
    

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    res=False
    if carte2['ouest']==False and carte1['est']==False:
      res = True

    return res
    


if __name__=="__main__":
  carte=Carte(False,False,True,True,2,[3])
  carte1=Carte(True,False,False,False,2,[3])
  print(carte)
  print('Valide:',estValide(carte))
  print('Nord:',murNord(carte))
  print('Sud:',murSud(carte))
  print('Ouest:',murOuest(carte))
  print('Est:',murEst(carte))
  print('get:',getNbPions(carte))
  print('set:',setListePions(carte,[1,2]))
  print('NB:',getNbPions(carte))
  print('possede:',possedePion(carte,1))
  print('getT:',getTresor(carte))
  print('prendreT:',prendreTresor(carte))
  print('mettreT:',mettreTresor(carte,15))
  print('prendre:',prendrePion(carte,1))
  print('poser:',poserPion(carte, 1))
  #print('tournerhor:',tournerHoraire(carte))
  print(carte)
  #print('tourneranti:',tournerAntiHoraire(carte))
  print(carte)
  #print('tourAlea:',tourneAleatoire(carte))
  print(carte)
  print('code:',coderMurs(carte))
  #print('decode:',decoderMurs(carte,2))
  print(carte)
  print('char:',toChar(carte))
  print('passageN:',passageNord((carte),(carte1)))
  print('passageS:',passageSud((carte),(carte1)))
  print('passageO:',passageOuest((carte),(carte1)))
  print('passageE:',passageEst((carte),(carte1)))