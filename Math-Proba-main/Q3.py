# -*- coding: utf-8 -*-
"""
Question 3
1 dimensions (binaire)
"""

import numpy as np
import matplotlib.pyplot as plt

Mmax, Mmin, q = 0, 0, 0

tabRetourZeroMoy = []    #Stock tout les temps de retour en 0 pour faire la moyenne

#Demande à l'utilisateur de rentrer le paramètre des marches ne nb de lancer et le nb de marches
p = float(input("Entrer le parametre : "))
nb = int(input("Entrer le nombres de lancers : "))
nbM = int(input("Entrer le nombres de marches à faire : "))
plt.ylabel('valeurs')
plt.xlabel('nb lancers')
print("****************")

while q < nbM :
   valeurfinal = 0
   x = 0
   i = 0
   tabLanceZero = []        #Permet d'avoir le retour en 0 
   tabx = []
   taby = []
   
   
   while i < nb:
        #Ajoute au tableau les valeurs
        tabx.append(i)
        taby.append(valeurfinal)
        rand = np.random.binomial(1, p)
        
        if rand == 0:
            valeurfinal = valeurfinal - 1
            if valeurfinal < Mmin:
                Mmin = valeurfinal
        
        if rand == 1:
            valeurfinal = valeurfinal + 1
            if valeurfinal > Mmax:
                Mmax = valeurfinal
                
        #Ajoute les valeurs de retour en 0 
        if valeurfinal == 0 and len(tabLanceZero) == 0:
            tabLanceZero.append(i+1)
            x = x+1
        elif valeurfinal == 0:
            tabLanceZero.append(1+i-tabLanceZero[x-1])
            x = x+1
            
        i = i + 1
        tabx.append(i)
        taby.append(valeurfinal)
        
   q = q + 1
   print("=================+Marche "+str(q)+"+======================")
   print("la valeur final pour lancer est : ", valeurfinal)
   #print("Temps retour a 0 : ",tabLanceZero)
   print("=================================================")
   tabRetourZeroMoy.extend(tabLanceZero)
   plt.plot(tabx, taby)
   


print("************************")
print("pour un paramètre :", p)
print("nombre de lancer :", nb)
print("nombre de marche :", nbM)
print("le max : ", Mmax)
print("le min : ", Mmin)
#print("Zero total : ", tabRetourZeroMoy)
print("il y a eu "+ str(len(tabRetourZeroMoy)) +" retour en zéro dans toutes les marches")
print("soit : "+str(len(tabRetourZeroMoy)/nbM)+ " par marche")
print("************************")
plt.title('en 1 dimension')
plt.show()

#Creation graphique des temps de retour en zero
plt.title('Temps de retour en zéro 1D')
plt.hist(tabRetourZeroMoy, bins=40, color='c', edgecolor='k', alpha=0.65)
plt.show()
