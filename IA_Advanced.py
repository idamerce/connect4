import grille
import random
import IA
import math
import numpy as np
from copy import deepcopy

def IA_alea(G): # IA jouant aléatoirement
	return random.choice(coups_possibles(G)) # à modifier

def IA_gagne(G):
	return bon_coup_score(G)

def coups_possibles(G):
	coups_possibles=[]
	for index,hauteur in enumerate(G.hauteurs):
		if hauteur!=G.lignes:
			coups_possibles.append(index)
	return coups_possibles

def exist_il_un_coup_gagnant(G,joueur):
	coups_possible= coups_possibles(G)
	for coup in coups_possible:
		#print(coup)
		G_temp=deepcopy(G)
		if G_temp.est_coup_gagnant(coup,joueur):
			return True
	return False

def est_noeud_terminal(G):
	jc_jadv=joueur_courant_adversaire(G) # jc_jadv[0] est le joueur courant or jc_jadv[1] est l'adversaire
	coup_jc_g=exist_il_un_coup_gagnant(G,jc_jadv[0])
	coup_jadv_g=exist_il_un_coup_gagnant(G,jc_jadv[1])
	est_coup_exist=len(coups_possibles(G)) == 0
	#print("coup_jc_g ",coup_jc_g," coup_jadv_g ",coup_jadv_g ," est_coup_exist ",est_coup_exist)
	return coup_jc_g or coup_jadv_g or est_coup_exist 

def bon_coup_score(G):
	coup_possible=coups_possibles(G)
	meilleur_score=-1000
	meilleur_coup=IA_alea(G)
	for coup in coup_possible:
		temp_G=deepcopy(G)
		temp_G.jeu[coup][temp_G.hauteurs[coup]]=temp_G.joueur_courant()
		score=score_coup(temp_G)
		if score>meilleur_score:
			meilleur_score=score
			meilleur_coup=coup
		print("coup", meilleur_coup, "meilleur score", meilleur_score)
	return meilleur_coup

def joueur_courant_adversaire(G):
	j_crnt=G.joueur_courant()
	G.coups+=1
	j_adv= G.joueur_courant()
	G.coups-=1
	return [j_crnt, j_adv]  

def evaluer_zone(zone,jc_jadv):
	score = 0
	#print("zone",zone)
	if zone.count(jc_jadv[0]) == 4:
		score += 100
	elif zone.count(jc_jadv[0]) == 3 and zone.count(0) == 1:
		score += 5
	elif zone.count(jc_jadv[0]) == 2 and zone.count(0) == 2:
		score += 2
	# if zone.count(jc_jadv[1]) == 3 and zone.count(0) == 1:
	# 	score -= 4

	return score

def ligne_grille(G,row):
	ligne=[]
	for i in range(G.colonnes):
		#print("i",i,"r",row)
		ligne.append(G.jeu[i][row])
	return ligne

def score_coup(G):
	jc_jadv=joueur_courant_adversaire(G) # jc_jadv[0] est le joueur courant or jc_jadv[1] est l'adversaire

	score=0
	score+=score_vertical(G,score,jc_jadv) + score_horizontal(G,score,jc_jadv)+ score_vertical(G,score,jc_jadv)
	#print("score", score)
	return score

def score_vertical(G,score,jc_jadv):
	for c in range(G.colonnes):
		colonne = G.jeu[c]
		for r in range(G.lignes-3):
			zone = colonne[r:r+4]
			score += evaluer_zone(zone, jc_jadv)
	return score

def score_horizontal(G,score,jc_jadv):
	for r in range(G.lignes):
		ligne = ligne_grille(G,r)
		#print(r,"--",ligne)
		for c in range(G.colonnes - 3):
			zone = ligne[c:c + 4]
			score += evaluer_zone(zone, jc_jadv)

	return score

def score_vertical(G,score,jc_jadv):

	for r in range(G.lignes-3):
		for c in range(G.colonnes-3):
			zone = [G.jeu[c+i][r+i] for i in range(4)]
			score += evaluer_zone(zone, jc_jadv)

	for r in range(G.lignes-3):
		for c in range(G.colonnes-3):
			zone = [G.jeu[c+i][r+3-i]  for i in range(4)]
			score += evaluer_zone(zone, jc_jadv)

	return score

def miniMax(G, depth, maximizingPlayer):
	coups_possible = coups_possibles(G)
	est_terminal = est_noeud_terminal(G)
	jc_jadv=joueur_courant_adversaire(G) # jc_jadv[0] est le joueur courant or jc_jadv[1] est l'adversaire
	column = random.choice(coups_possible)
	if depth == 0 or est_terminal:
		#print("terminale",est_terminal,"----",depth)
		if est_terminal:
			bon_coup_jc=IA.bon_coup(G,jc_jadv[0])
			bon_coup_jadv=IA.bon_coup(G,jc_jadv[1])
			if bon_coup_jc!=-1:
				return (bon_coup_jc, 100000000000000)
			elif bon_coup_jadv!=-1:
				return (bon_coup_jadv, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_coup(G))
	if maximizingPlayer:
		value = -math.inf
		for col in coups_possible:
			G_temp = deepcopy(G)
			G_temp.jeu[col][G_temp.hauteurs[col]]=jc_jadv[0]
			new_score = miniMax(G_temp, depth-1, False)[1]
			if new_score > value:
				value = new_score
				column = col
		return column,new_score
	else:
		value = math.inf
		for col in coups_possible:
			G_temp = deepcopy(G)
			G_temp.jeu[col][G_temp.hauteurs[col]]=jc_jadv[1]
			new_score = miniMax(G_temp, depth-1, True)[1]
			if new_score < value:
				value = new_score
				column = col
		return column,new_score

def miniMaxAlphaBeta(G, depth, alpha, beta, maximizingPlayer):
	coups_possible = coups_possibles(G)
	est_terminal = est_noeud_terminal(G)
	jc_jadv=joueur_courant_adversaire(G) # jc_jadv[0] est le joueur courant or jc_jadv[1] est l'adversaire
	column = random.choice(coups_possible)
	if depth == 0 or est_terminal:
		#print("terminale",est_terminal,"----",depth)
		if est_terminal:
			bon_coup_jc=IA.bon_coup(G,jc_jadv[0])
			bon_coup_jadv=IA.bon_coup(G,jc_jadv[1])
			if bon_coup_jc!=-1:
				return (bon_coup_jc, 100000000000000)
			elif bon_coup_jadv!=-1:
				return (bon_coup_jadv, -10000000000000)
			else: # Game is over, no more valid moves
				return (None, 0)
		else: # Depth is zero
			return (None, score_coup(G))
	if maximizingPlayer:
		value = -math.inf
		for col in coups_possible:
			G_temp = deepcopy(G)
			G_temp.jeu[col][G_temp.hauteurs[col]]=jc_jadv[0]
			new_score = miniMax(G_temp, depth-1, False)[1]
			if new_score > value:
				value = new_score
				column = col
			alpha = max(alpha, value)
			if alpha >= beta:
				break
		return column,new_score
	else:
		value = math.inf
		for col in coups_possible:
			G_temp = deepcopy(G)
			G_temp.jeu[col][G_temp.hauteurs[col]]=jc_jadv[1]
			new_score = miniMax(G_temp, depth-1, True)[1]
			if new_score < value:
				value = new_score
				column = col
			beta = min(beta, value)
			if alpha >= beta:
				break
		return column,new_score
