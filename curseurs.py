# -*- coding: cp1252 -*-

import sys

#v�rification de le version->compatibilit� python2 et python3
if sys.version_info[0]==3:
    from tkinter import *
else:
    from Tkinter import *
    
from math import pi

class ChoixVibra (Frame):
    """Curseurs pour choirsir la fr�quence, la phase et l'amplitude d'une vibration"""

    def __init__(self, boss= None, coul ='red'):
        Frame.__init__(self)     #constructeur de la classe m�re
        #Initialisation de quelques attributs d'instance:
        self.freq, self.phase, self.ampl, self.coul=0, 0, 0, coul
        #Variable d'�tat de la classe � cocher
        self.chk =IntVar()
        Checkbutton(self, text="Affichier", variable=self.chk,
                    fg = self.coul, command =self.setCurve).pack(side=LEFT)
        #D�finition des 3 curseurs
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label="Fr�quence (Hz) :", from_=1, to =9., tickinterval =2,
              resolution =0.25,
              showvalue =0, command =self.setFrequency).pack(side=LEFT)
        Scale(self, length =150, orient=HORIZONTAL, sliderlength =15,
              label= "Phase (degr�s) :", from_ =-180, to =180, tickinterval =90,
              showvalue =0, command = self.setPhase).pack(side=LEFT)
        Scale(self, length =150, orient=HORIZONTAL, sliderlength =25,
              label ="Amplitude :", from_=1, to=9, tickinterval =2,
              showvalue =0, command = self.setAmplitude).pack(side=LEFT)

    def setCurve(self):
        self.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq =float(f)
        self.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp=float(p)
        self.phase = pp*2*pi/360    #conversion degr�s -> radian
        self.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.event_generate('<Control-Z>')

#### Code pour tester la classe : ####

if __name__ == '__main__':
    def afficherTout (event=None):
        lab.configure(text= "{0} - {1} - {2: .3f} - {3}".\
                      format(fra.chk.get(), fra.freq, fra.phase, fra.ampl))

    root=Tk()
    fra = ChoixVibra(root, "navy")
    fra.pack(side=TOP)
    lab = Label(root, text ="test")
    lab.pack()
    root.bind('<Control-Z>', afficherTout)
    root.mainloop()
