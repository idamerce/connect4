class grille:

	# initialise le jeu
	def __init__(self,c,l):
		self.colonnes = c # inférieur à 10
		self.lignes = l
		# les hauteurs sont toutes initialisées à 0
		self.hauteurs = [0 for _ in range(self.colonnes)]
		# on rempli une grille de 0 (cases vides)
		self.jeu = [[0 for _ in range(self.lignes)] for _ in range(self.colonnes)]	
		self.coups = 0 # nombre de coups joués
	
	def __str__(self):
		s = ''
		i=self.lignes-1
		j=0
		while i>=0:
			s+="| "
			while j<self.colonnes:
				s+=str(self.jeu[j][i])+" | "
				j+=1
			s+="\n"
			j=0
			i-=1

		# i=0
		# j=0
		# s+="\n\n"
		# while i<self.lignes:
		# 	s+="| "
		# 	while j<self.colonnes:
		# 		s+=str(self.jeu[j][i])+" | "
		# 		j+=1
		# 	s+="\n"
		# 	j=0
		# 	i+=1

		# mettre dans s l'affichage voulu
		return s

	def joueur_courant(self):
		return 1+self.coups%2 # 1 pour coup pair, 2 sinon
	

	def est_jouable(self,col):
		return self.hauteurs[col] < self.lignes
		
	# vérifie si un joueur a saisi un coup jouable
	def coup_humain_valide(self,col):
		return col!=None and col>=0 and col<=self.lignes and not self.colonne_pleine(col)# à modifier

	# joue un coup au bon endroit (sans vérification)
	def joue(self,col):
		self.jeu[col][self.hauteurs[col]]=self.joueur_courant()
		self.coups+=1
		self.hauteurs[col]+=1

	# joue une séquence de coups stockée dans une chaine de caractères, en vérifiant la validité :
	# coups jouables, pas de partie terminée. Retourne le nombre de coups joués.
	def joue_seq(self,seq):
		for i in range(len(seq)):
			col=int(seq[i])-1
			if(col<0 or col>=self.colonnes or not self.est_jouable(col) or self.est_coup_gagnant(col)):
				return i
			self.joue(col)
		return len(seq)

	# retourne le nombre de coups joués 
	def nb_coups(self):
		return self.coups

	def nb_lignes(self):
		return self.lignes
		
	def nb_colonnes(self):
		return self.colonnes
		
	# retourne vrai si la colonne est pleine 
	def colonne_pleine(self,c):
		return self.hauteurs[c]==self.colonnes-1

	# retourne vrai si la grille est pleine 
	def grille_pleine(self):
		return self.lignes*self.colonnes<=self.coups
		# for i in range(self.lignes):
		# 	for j in range(self.colonnes):
		# 		if self.jeu[j][i]==0:
		# 			return False
		# return True

	# retourne vrai si col permet au joueur courant de gagner
	def est_coup_gagnant(self,col,joueur_courant=None):
		idx=self.hauteurs[col]-1
		isVerticalWinning=False
		if joueur_courant==None:
			joueur_courant=self.joueur_courant()
		if idx>=2:
			isVerticalWinning= self.isVertical_Wining(col,idx,joueur_courant)
		return isVerticalWinning or self.isHorizontal_Wining(col,idx+1,joueur_courant) or self.isDiagonal_Wining(col,idx+1,joueur_courant)

	def isVertical_Wining(self,col,idx,joueur_courant):
		coups=1
		while self.jeu[col][idx]==joueur_courant:
			coups+=1
			idx-=1
			if coups==4:
				return True
		return False

	def isHorizontal_Wining(self,col,idx,joueur_courant):
		self.jeu[col][self.hauteurs[col]]=joueur_courant
		for j in range(self.colonnes-1):
			pion=0
			coups=0
			if self.jeu[j][idx] !=0:
				pion=self.jeu[j][idx]
				while j<self.colonnes and self.jeu[j][idx] ==pion :
					coups+=1
					j+=1
					if coups==4:
						return True
		return False

	def isDiagonal_Wining(self,col,idx,joueur_courant):
		#if self.colonnes-self.hauteurs[col] >4:
		#print(self.jeu)
		if idx >=3:
			leftDiagonal=rightDiagonal=0
			i=1
			while idx-i>=0:
				if col>=2:
					if self.jeu[col-i][idx-i]==joueur_courant:
						leftDiagonal+=1
				if self.colonnes-col>3 and i+col<self.colonnes:
					if self.jeu[col+i][idx-i]==joueur_courant:
						rightDiagonal+=1
				i+=1
			if leftDiagonal==3 or rightDiagonal==3:
				return True

		if self.colonnes-idx>=3 :
			leftDiagonal=rightDiagonal=0
			i=1
			while i+idx<self.lignes and i+col<self.colonnes:
				if col<=3:
					if self.jeu[col-i][idx+i]==joueur_courant:
						leftDiagonal+=1
				if self.colonnes-col>3:
					if self.jeu[col+i][idx+i]==joueur_courant:
						rightDiagonal+=1
				i+=1
			if leftDiagonal==3 or rightDiagonal==3:
				return True
		return False

 