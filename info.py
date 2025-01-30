import tkinter as tk


class Info_Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("programm Info")
        self.geometry("600x280")

        label = tk.Label(self, text="Informationen:")
        label.pack(pady=15)

        label = tk.Label(self, text="Programmiert von Christian Zenger")
        label.pack(pady=10)

        label = tk.Label(self, text="GitHub: https://github.com/devZenger/Netzwerkrechner")
        label.pack(pady=10)

        bt_close = tk.Button(self, text="schließen", command=self.close_window)
        bt_close.pack(pady=20)

    def close_window(self):
        self.destroy()
