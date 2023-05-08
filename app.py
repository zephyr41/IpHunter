from tkinter import *

gui = Tk()

label = Label(gui, text="Entrez une cible ")

label.pack(side=TOP)

ip = StringVar()  ## sert à définir l'ip

input = Entry(gui, textvariable=ip)  ## sert à donner une zone de texte

input.pack()  ## permet d'organiser les widgets

ip.set("ex : 192.168.1.0/24")

content = ip.get()

gui.mainloop()


## Une fois qu'on à la valeur : rajouter un button scan qui lance une fonction de scan