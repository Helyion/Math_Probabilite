# -*- coding: utf-8 -*-
"""
Question 5
3 dimensions
"""

import matplotlib.pyplot as plt
from random import randint


q, x, y, z = 0, 0, 0, 0

tabRetourZeroMoy = []    #Stock tout les temps de retour en 0 pour faire la moyenne

#Demande à l'utilisateur de rentrer le nb de marches et le nb de lancer
nb = int(input("Entrer le nombres de lancers : "))
nbM = int(input("Entrer le nombres de marches à faire :"))
ax = plt.axes(projection='3d')
ax.scatter3D(x, y, z);

while q < nbM :
   x = 0 
   y = 0
   z = 0
   tabx = []
   taby = []
   tabz = []
   tmpZero = 0
   tabZero = []
   i = 0
   tabx.append(x)
   taby.append(y)
   tabz.append(z)
   #On rempli les tabs
   while i < nb:
       b = randint(0,5)
       if b == 0: 
           x += 1
       elif b == 1:
           x -= 1
       elif b == 2:
           y += 1
       elif b == 3:
           y -= 1
       elif b == 4:
           z += 1
       else:
           z -= 1
           
       i = i+1
       tmpZero = tmpZero + 1
       if y == 0 and x == 0 and z == 0:
           tabZero.append(tmpZero)
           tmpZero = 0;
       tabx.append(x)
       taby.append(y)
       tabz.append(z)


   q = q + 1
   #Affichage en 3D
   ax.scatter3D(x, y, z);
   ax.plot3D(tabx, taby, tabz)
   tabRetourZeroMoy.extend(tabZero)
   
   #Affichage par Marche des differantes coordonnées
   print("=================+Marche "+str(q)+"+======================")
   print("Les coordonnées finales : x:"+str(x)+" y:"+str(y)+" z:"+str(z))
   """
   print("Les coordonnées x : " + str(tabx))
   print("Les coordonnées y : " + str(taby))
   print("Les coordonnées z : " + str(tabz))
   """
   print("Temps de retour a zéro : "+ str(tabZero))
   print("=================================================")

print("************************")
print("pour un paramètre : 0.16")
print("nombre de lancer :", nb)
print("nombre de marche :", nbM)
#print("Zero total : ", tabRetourZeroMoy)
print("il y a eu "+ str(len(tabRetourZeroMoy)) +" retour en zéro dans toutes les marches")
print("soit : "+str(len(tabRetourZeroMoy)/nbM)+ " par marche")
print("************************")
plt.title('en 3 dimensions')
plt.show()

#Creation graphique des temps de retour en zero
plt.title('Temps de retour en zéro 3D')
plt.hist(tabRetourZeroMoy, bins=40, color='c', edgecolor='k', alpha=0.65)
plt.show()

