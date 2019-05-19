
# -*- coding: cp1252 -*-
import sys

#vérification de le version->compatibilité python2 et python3
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *
    
from math import sin, pi

class OscilloGraphe(Canvas):
    "Canevas spécialiser pour dessiner des courbes élongation/temps"
    def __init__(self, boss=None, larg=200, haut=150):
        "constructeur graphique: axe et echelle horizontale"
        #construction du widget parent :
        Canvas.__init__(self)                   #appel au constructeur
        self.configure(width=larg, height =haut)#de la classe parente
        self.larg, self.haut=larg, haut
        #tracé des axes de référence:
        self.create_line(10, haut/2, larg, haut/2, arrow=LAST)  #axe X
        #self.create_line(10, haut-5, 10, 5, arrow =LAST)        #axe Y
        self.create_line(larg/2-3, haut-5, larg/2-3, 5, arrow =LAST)
        #tracé des échelles avec des graduations:
        pas=(larg-25)/8
        for t in range(1, 9):
            stx=10+t*pas
            self.create_line(stx, haut/2-4, stx, haut/2+4)

        pasx=(larg-25)/8
        pasy=(haut-20)/10
        
        x, y=10, 10

        while y<haut-25:
    
    
            while x<larg-20:
                self.create_rectangle(x, y, x+pasx, y+pasy, outline="grey")
                x+=pasx
            x=10   
            y+=pasy

    def traceCourbe(self, freq=1, phase=0, ampl=10, coul='red'):
        "tracé graphique élogation/temps sur 1 seconde"
        curve=[]
        pas = (self.larg-25)/1000.
        for t in range (0, 1001, 5):
            e=ampl*sin(2*pi*freq*t/1000 - phase)
            x=10+t*pas
            y=self.haut/2 - e*self.haut/25
            curve.append((x, y))
        n = self.create_line(curve, fill=coul, smooth=1)
        return n

if __name__=='__main__':
    root=Tk()
    gra=OscilloGraphe(root, 250, 180)
    gra.pack()
    gra.configure(bg='white', bd =2, relief=SUNKEN)
    gra.traceCourbe(2, 1.2, 10, 'purple')
    root.mainloop()
