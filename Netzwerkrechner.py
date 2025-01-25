import tkinter as tk


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Netzwerkrechner")
        self.geometry("500x300")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.top_frame = tk.Frame(self.container, bg="lightgray")
        self.top_frame.pack(fill="x", side="top")

        ipv4_button = tk.Button(self.top_frame, text="IPv4 Rechner",
                                command=lambda: self.show_frame(IPv4Page))
        ipv4_button.grid(row=0, column=0, padx=10, pady=10)
        ipv6_button = tk.Button(self.top_frame, text="IPv6 Rechner",
                                command=lambda: self.show_frame(IPv6Page))
        ipv6_button.grid(row=0, column=1, padx=10, pady=10)

        self.main_frame = tk.Frame(self.container)
        self.main_frame.pack(fill="both", expand=True, side="bottom")

        self.frames = {}

        for Page in (IPv4Page, IPv6Page):
            frame = Page(parent=self.main_frame, controller=self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IPv4Page)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class IPv4Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="IPv4:", font=("Arial", 14))
        label.grid(row=0, column=0, pady=10)

        ipv4_label = tk.Label(self, text="IP Adresse: ")
        ipv4_label.grid(row=2, column=0)
        ipv4_input = tk.Entry(self)
        ipv4_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        cidir_input = tk.Entry(self)
        cidir_input.grid(row=3, column=1)

        cal_ipv4 = tk.Button(self, text="berechnen")
        cal_ipv4.grid(row=3, column=2)


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


#  start programm
start = Main()
start.mainloop()
