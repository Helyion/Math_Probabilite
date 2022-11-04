# -*- coding: utf-8 -*-
"""
Question 2
"""
import numpy as np
import matplotlib.pyplot as plt

Mmax, Mmin, q = 0, 0, 0

#Demande à l'utilisateur de rentrer le paramètre des marches ne nb de lancer et le nb de marches
p = float(input("Entrer le parametre : "))
nb = int(input("Entrer le nombres de lancers : "))
nbM = int(input("Entrer le nombres de marches à faire : "))
plt.ylabel('valeurs')
plt.xlabel('nb lancers')
print("****************")
while q < nbM :
   #Initialise les abscices et les ordonées pour nos marches
   tabx = []
   taby = []
   y = 0
   i = 0
   
   while i < nb:
        #Ajoute au tableau les valeurs
        tabx.append(i)
        taby.append(y)
        rand = np.random.binomial(1, p)
        
        if rand == 0:
            y = y - 1
            if y < Mmin:
                Mmin = y
        
        if rand == 1:
            y = y + 1
            if y > Mmax:
                Mmax = y
                
        tmp = y
        i = i + 1
   tabx.append(i)
   taby.append(y)
   
   q = q + 1
   #Affiche les marches avec sa valeur final 
   print("=================+Marche "+str(q)+"+======================")
   print("la valeur final pour lancer est : ", tmp)
   print("=================================================")
   plt.plot(tabx, taby)
   

#affiche le graphique
plt.show()
print("****************")
print("Pour un paramètre :", p)
print("nombres de lancers :", nb)
print("nombres de marches :", nbM)
print("le max : ", Mmax)
print("le min : ", Mmin)
print("****************")