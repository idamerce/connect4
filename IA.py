import grille
import random
from copy import deepcopy
def IA_alea(G): # IA jouant aléatoirement
	return random.choice(coups_possibles(G)) # à modifier

def IA_gagne(G):
	
	bonCoup=bon_coup(G,G.joueur_courant())
	G.coups+=1
	coup_attaque=bon_coup(G,G.joueur_courant())
	G.coups-=1
	if bonCoup!=-1:
		return bonCoup
	elif coup_attaque!=-1:
		return coup_attaque
	else:
		return IA_alea(G)

def bon_coup(G,joueur_courant):
	coup_possible=coups_possibles(G)
	for coup in coup_possible:
		if deepcopy(G).est_coup_gagnant(coup,joueur_courant)==True:
			return coup
	return -1

def coups_possibles(G):
	coups_possibles=[]
	for index,hauteur in enumerate(G.hauteurs):
		if hauteur!=G.lignes:
			coups_possibles.append(index)
	return coups_possibles
