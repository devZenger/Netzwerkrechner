import tkinter as tk
import sys


class Save_Output_Window(tk.Toplevel):
    def __init__(self, parent, output):
        super().__init__(parent)
        self.title("Speichere Ergebnisse")
        self.geometry("300x240")
        self.to_save = output

        label = tk.Label(self, text="Dateiname eingeben:")
        label.pack(pady=20)
        self.file_name_input = tk.Entry(self)
        self.file_name_input.pack(pady=10)

        bt_frame = tk.Frame(self)
        bt_frame.pack(expand=True, pady=(0, 10))

        bt_save = tk.Button(bt_frame, text="speichern",
                            command=self.save_output)
        bt_save.pack(pady=0, padx=10, side=tk.LEFT)

        bt_close = tk.Button(bt_frame, text="schließen",
                             command=self.close_window)
        bt_close.pack(pady=0, padx=10, side=tk.LEFT)

        self.message = tk.Label(self)
        self.message.pack(pady=(10, 30))

    def save_output(self):
        try:
            file_name = self.file_name_input.get()
            d = open(f"{file_name}", "w")

            for save in self.to_save:
                d.write(f"{save}")

            d.close()
            self.message.config(text="gespeichert")

        except Exception as e:
            self.message.config(text=f"Fehler: {e}")

    def close_window(self):
        self.destroy()
