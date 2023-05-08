from tkinter import *
import tkinter
from verif import isGoodIp

gui = Tk()
gui.geometry("330x330")
label = Label(gui, text="Entrez une cible ")

label.pack(side=TOP)

ipInLabel = StringVar()  ## sert à définir l'ip dans le label

input = Entry(gui, textvariable=ipInLabel)  ## sert à donner une zone de texte qui contient notre ip

input.pack()  ## permet d'organiser les widgets
ipInLabel.set("ex : 192.168.1.0/24") ## définit une variable par default

def Scan() :

    IptoScan = ipInLabel.get() ## sert à récupéré la variable a scanner
    if len(IptoScan) > 3 and isGoodIp(IptoScan):
        print('The host to attack is : ', IptoScan) ## L'affiche
    else : print("Enter an valid ip")
 



scanButton = tkinter.Button(gui, text ="Scan", command=Scan) ## permet de lancer la commande scan quand on lance le label
scanButton.config(width=20, height=2)
 
scanButton.pack()

gui.mainloop()


## Une fois qu'on à la valeur : rajouter un button scan qui lance une fonction de scan