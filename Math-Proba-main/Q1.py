# -*- coding: utf-8 -*-
"""
Question 1
Simulation des n premiers élements d'une marche aléatoire de paramètre 0.5
"""
import numpy as np

p = .6 #Modifiable pour changer le paramétre

total, Mmax, Mmin, i = 0, 0, 0, 0


#Demande à l'utilisateur de rentrer un nb de lancer
nb = int(input("Entrer le nombres de lancers :"))
while i < nb:
    rand = np.random.binomial(1, p)
    
    if rand == 0:
        total = total - 1
        if total < Mmin:
            Mmin = total        #Valeur max de la marche 
    
    if rand == 1:
        total = total + 1
        if total > Mmax:
            Mmax = total        #Valeur min de la marche 
    i = i + 1

#Affichage Console
print("le resultat final avec comme paramètre : ")
print(p)
print("est : ")
print(total)
print("le maximum est : ")
print(Mmax)
print("le minimum est : ")
print(Mmin)
