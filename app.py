import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("IpHunter")

        # Ajouter un tableau
        self.tree = ttk.Treeview(master, columns=("Host", "IP", "Adresse Mac", "Port", "State", "Version", "Vulnerability"))
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Host", anchor="center", width=100)
        self.tree.column("IP", anchor="center", width=100)
        self.tree.column("Adresse Mac", anchor="center", width=100)
        self.tree.column("Port", anchor="center", width=100)
        self.tree.column("State", anchor="center", width=100)
        self.tree.column("Version", anchor="center", width=100)
        self.tree.column("Vulnerability", anchor="center", width=100)

        self.tree.heading("#1", text="", anchor="center")
        self.tree.heading("Host", text="Host", anchor="center")
        self.tree.heading("IP", text="IP", anchor="center")
        self.tree.heading("Adresse Mac", text="Adresse Mac", anchor="center")
        self.tree.heading("Port", text="Port", anchor="center")
        self.tree.heading("State", text="State", anchor="center")
        self.tree.heading("Version", text="Version", anchor="center")
        self.tree.heading("Vulnerability", text="Vulnerability", anchor="center")

        self.tree.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

        # Ajouter un bouton Scan
        self.scan_button = tk.Button(master, text="Scan", command=self.scan)
        self.scan_button.grid(row=1, column=0, padx=10, pady=10)
    
    def scan(self):
        # Ajouter ici la logique de scan du réseau
        # Ajouter une nouvelle ligne dans le tableau pour chaque hôte détecté
        self.tree.insert(parent="", index=tk.END, iid=90, text="", values=("example.com", "192.168.0.1", "00:11:22:33:44:55", "80", "open", "HTTP/1.1", "vulnerable"))

root = tk.Tk()
app = MyApp(root)
root.mainloop()
