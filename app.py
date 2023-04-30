import tkinter as tk
from tkinter import ttk


class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("IpHunter")
        self.target = ""

        # Ajouter un label pour la zone de saisie de la cible
        self.target_label = tk.Label(master, text="Target:")
        self.target_label.grid(row=0, column=0, padx=10, pady=10)

        # Ajouter une zone de saisie pour la cible
        self.target_entry = tk.Entry(master)
        self.target_entry.grid(row=0, column=1, padx=10, pady=10)

        # Ajouter un tableau
        self.tree = ttk.Treeview(
            master,
            columns=(
                "Host",
                "IP",
                "Adresse Mac",
                "Port",
                "State",
                "Version",
                "Vulnerability",
            ),
        )
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Host", anchor="center", width=100)
        self.tree.column("IP", anchor="center", width=100)
        self.tree.column("Adresse Mac", anchor="center", width=100)
        self.tree.column("Port", anchor="center", width=100)
        self.tree.column("State", anchor="center", width=100)
        self.tree.column("Version", anchor="center", width=100)
        self.tree.column("Vulnerability", anchor="center", width=100)

        self.tree.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

        # Ajouter un bouton Scan
        self.scan_button = tk.Button(
            master, text="Scan", command=lambda: self.scan(self.target)
        )
        self.scan_button.grid(row=1, column=0, padx=10, pady=10)

        def scan(self, target):
            # Stocker la valeur de la zone de saisie de la cible dans la variable "target"
            target = self.target_entry.get()

    # Afficher la valeur dans le label
    self.target_label.config(text="Target: " + target)

    # Afficher la valeur dans le terminal
    print(target)

    # Ajouter ici la logique de scan du réseau
    # Ajouter une nouvelle ligne dans le tableau pour chaque hôte détecté
    self.tree.insert(
        parent="",
        index=tk.END,
        iid=90,
        text="",
        values=(
            "example.com",
            "192.168.0.1",
            "00:11:22:33:44:55",
            "80",
            "open",
            "HTTP/1.1",
            "vulnerable",
        ),
    )
