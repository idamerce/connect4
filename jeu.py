import grille
import IA
import IA_Advanced
import time
import math
import random
def winner(gagnant):
	print("Joueur ",gagnant,"a gagné !") if gagnant!=0 else print("Equivalence !")

def Play(colonnes,lignes,Joueurs,affichage=True):
	G=grille.grille(colonnes,lignes)
	#G=grille.grille(6,5)
	#G=grille.grille(7,6)
	
	gagnant=0 # 1 si j1 gagne, 2 sinon
	dep=''
	if (Joueurs[0] and Joueurs[1])==0:
		dep=input("Position de départ (vide pour début de partie) : ")
	G.joue_seq(dep)
	humanvsbot = Joueurs[0]!=Joueurs[1] 
	while (not G.grille_pleine() and gagnant==0):
		if affichage==True:
			print(G) # à remplacer par print(G) une fois la procédure __str__ écrite
			print("Joueur",G.joueur_courant())
		type_j=Joueurs[G.joueur_courant()-1] # on détermine le type de joueur qui va jouer
		if type_j==0: # choix du joueur humain
			c=int(input("Colonne ? "))-1
			while not G.coup_humain_valide(c):
				c=int(input("Colonne ? "))-1 # les colonnes sont numérotées de 0 à 6
		else: # choix de l'IA
			if affichage:
				print("Role de l'AI")
			if humanvsbot:
				time.sleep(.4)
			#c=IA.IA_alea(G)
			c=IA.IA_gagne(G)
		if G.est_coup_gagnant(c):
			gagnant=G.joueur_courant()
		G.joue(c)
	if affichage==True:
		print(G)
	return gagnant

#winner(Play(6,5,[0,1]))

def playBetweenTwoAIOneRound():
	Joueurs=[1, 1] # 0=humain, >0=IA  
	gagnant = Play(6,5,Joueurs )# 0=humain, >0=IA  :
	print("Joueur ",gagnant,"a gagné !") if gagnant!=0 else print("Equivalence !")

#playBetweenTwoAIOneRound()

def PlayXRound(x):
	grillMaxWidth=20
	Joueurs=[1, 1]
	winner_statistics=[0,0]
	for i in range(x):
		width=random.randrange(5,grillMaxWidth)
		height=width-1
		gagnant=Play(width,height,Joueurs,False)
		print("Joueur ",gagnant,"a gagné !") if gagnant!=0 else print("Equivalence !")
		if gagnant==1:
			winner_statistics[0]+=1
		if gagnant==2:
			winner_statistics[1]+=1
	print(f"le joueur 1 a gagner {winner_statistics[0]} fois or le joueur 2 a gagné {winner_statistics[1]} fois, Nombre de balance {x-winner_statistics[0]-winner_statistics[1]}")

#PlayXRound(100)


#advancedIA Minimax
def PlayIA_AdvancedMinimax(colonnes,lignes,Joueurs,affichage=True,humanvsbot=False):
	G=grille.grille(colonnes,lignes)

	gagnant=0 # 1 si j1 gagne, 2 sinon
	dep=''
	if (Joueurs[0] and Joueurs[1])==0:
		dep=input("Position de départ (vide pour début de partie) : ")
	G.joue_seq(dep)
	#humanvsbot = Joueurs[0]!= Joueurs[1] 
	while (not G.grille_pleine() and gagnant==0):
		if affichage==True:
			print(G) # à remplacer par print(G) une fois la procédure __str__ écrite
			print("Joueur",G.joueur_courant())
		type_j=Joueurs[G.joueur_courant()-1]
		 # on détermine le type de joueur qui va jouer
		if type_j==0: # choix du joueur humain
			c=int(input("Colonne ? "))-1
			while not G.coup_humain_valide(c):
				c=int(input("Colonne ? "))-1 # les colonnes sont numérotées de 0 à 6
		else: # choix de l'IA
			if affichage==True:
				print("Role de l'AI")
			if humanvsbot:
				time.sleep(1)
			c=IA_Advanced.miniMax(G,3,True)[0]
			print("column",c)
		if G.coup_humain_valide(c):
			if G.est_coup_gagnant(c):
				gagnant=G.joueur_courant()
			G.joue(c)
	if affichage==True:
		print(G)
	return gagnant

# dd=PlayIA_AdvancedMinimax(6,5,Joueurs=[0,1],affichage=True)
# winner(dd)

#advancedIA Alpha Beta
def PlayIA_AdvancedAmeleoratioAlphaBeta(colonnes,lignes,Joueurs,affichage=True,humanvsbot=False):
	G=grille.grille(colonnes,lignes)

	gagnant=0 # 1 si j1 gagne, 2 sinon
	dep=''
	if (Joueurs[0] and Joueurs[1])==0:
		dep=input("Position de départ (vide pour début de partie) : ")
	G.joue_seq(dep)
	#humanvsbot = Joueurs[0]!= Joueurs[1] 
	while (not G.grille_pleine() and gagnant==0):
		if affichage==True:
			print(G) # à remplacer par print(G) une fois la procédure __str__ écrite
			print("Joueur",G.joueur_courant())
		type_j=Joueurs[G.joueur_courant()-1]
		 # on détermine le type de joueur qui va jouer
		if type_j==0: # choix du joueur humain
			c=int(input("Colonne ? "))-1
			while not G.coup_humain_valide(c):
				c=int(input("Colonne ? "))-1 # les colonnes sont numérotées de 0 à 6
		else: # choix de l'IA
			if affichage==True:
				print("Role de l'AI")
			if humanvsbot:
				time.sleep(1)
			c=IA_Advanced.miniMaxAlphaBeta(G,4,-math.inf, math.inf,True)[0]
		if G.coup_humain_valide(c):
			if G.est_coup_gagnant(c):
				gagnant=G.joueur_courant()
			G.joue(c)
	if affichage==True:
		print(G)
	return gagnant

dd=PlayIA_AdvancedAmeleoratioAlphaBeta(6,5,Joueurs=[0,1],affichage=True)
winner(dd)


