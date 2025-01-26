import tkinter as tk

class IPv6Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="IPv6:", font=("Arial", 14))
        label.grid(row=0, column=0, pady=10)

        ipv6_label = tk.Label(self, text="IP Adresse: ")
        ipv6_label.grid(row=2, column=0)
        ipv6_input = tk.Entry(self)
        ipv6_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        cidir_input = tk.Entry(self)
        cidir_input.grid(row=3, column=1)

        cal_ipv6 = tk.Button(self, text="berechnen")
        cal_ipv6.grid(row=3, column=2)
