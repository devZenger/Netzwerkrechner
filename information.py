import tkinter as tk


class Info_Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("programm Info")
        self.geometry("600x490")

        label = tk.Label(self, text="Informationen:")
        label.pack(pady=15)

        label = tk.Label(self, text="Netzwerkrechner")
        label.pack(pady=10)

        label = tk.Label(self, text="Version 1.0.0 - Mai 2025")
        label.pack(pady=10)

        label = tk.Label(self, text="Desktop-Tool zur Berechnung\nvon IPv4- und IPv6_Netzwerkdaten.")
        label.pack(pady=10)

        label = tk.Label(self, text="Entwickelt von Christian Zenger.")
        label.pack(pady=10)

        label = tk.Label(self, text=("Feedback und Fragen gerne unter:\n"
                                     "GitHub: https://github.com/devZenger/Netzwerkrechner"))
        label.pack(pady=10)
        label = tk.Label(self, text="Dieses Programm steht unter der MIT-Lizenz")
        label.pack(pady=10)

        bt_close = tk.Button(self, text="Schließen", command=self.close_window)
        bt_close.pack(pady=20)

    def close_window(self):
        self.destroy()
