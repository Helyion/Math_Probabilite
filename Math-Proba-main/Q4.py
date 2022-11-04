# -*- coding: utf-8 -*-
"""
Question 4
2 dimensions
"""

import matplotlib.pyplot as plt
from random import randint

q, x, y = 0, 0, 0

tabRetourZeroMoy = []    #Stock tout les temps de retour en 0 pour faire la moyenne

#Demande à l'utilisateur de rentrer le nb de marches et le nb de lancer
#4 chemin possible 
nb = int(input("Entrer le nombres de lancers : "))
nbM = int(input("Entrer le nombres de marches à faire : "))

plt.scatter(x, y, c = 'green')
while q < nbM :
   zero = 0;
   y = 0
   x = 0 
   tabx = []
   taby = []
   valeurfinal = []
   tabnbLanceZero = []
   i = 0
   tabx.append(x)
   taby.append(y)
   
   #Incrémentation et d'écrémentation des x et y. 
   while i < nb:
       b = randint(0,3)
       if b == 0:
           x += 1
       elif b == 1:
           x -= 1
       elif b == 2:
           y += 1
       else:
           y -= 1
           
     #Renvoi les temps de retour en 0 
       if x == 0 and y == 0 and len(tabnbLanceZero) == 0:
           tabnbLanceZero.append(i+1)
           zero = zero+1
       elif x == 0 and y == 0:
           tabnbLanceZero.append(1+i-tabnbLanceZero[zero-1])
           zero = zero+1
           
       tabx.append(x)
       taby.append(y)
       i = i+1
   valeurfinal.append(x)
   valeurfinal.append(y)
   tabRetourZeroMoy.extend(tabnbLanceZero)
   
   q = q + 1
   #Affichage des marches avec leurs temps de retour en 0 et  la valeur final 
   print("=================+Marche "+str(q)+"+======================")
   print("Les coordonnées finales sont (x,y): ", valeurfinal)
   print("Temps retour a 0 : ",tabnbLanceZero)
   print("=================================================")
       
   
   plt.scatter(x, y)
   plt.plot(tabx, taby)
   
print("************************")
print("pour un paramètre : 0.25")
print("nombre de lancer :", nb)
print("nombre de marche :", nbM)
#print("Zero total : ", tabRetourZeroMoy)
print("il y a eu "+ str(len(tabRetourZeroMoy)) +" retour en zéro dans toutes les marches")
print("soit : "+str(len(tabRetourZeroMoy)/nbM)+ " par marche")
print("************************")
plt.title('en 2 dimensions')
plt.show()

#Creation graphique des temps de retour en zero
plt.title('Temps de retour en zéro 2D')
plt.hist(tabRetourZeroMoy, bins=40, color='c', edgecolor='k', alpha=0.65)
plt.show()
