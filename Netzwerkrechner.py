import tkinter as tk
import tkinter.font as font
from ipv4_calculation import IPv4Page
from ipv6_calculation import IPv6Page
from info import Info_Window


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Netzwerkrechner")
        self.geometry("900x500")

        default_font = font.Font(family="Consolas", size=14)
        self.option_add("*Font", default_font) 

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.top_frame = tk.Frame(self.container, bg="lightgray")
        self.top_frame.pack(fill="x", side="top")

        ipv4_button = tk.Button(self.top_frame, text="IPv4 Rechner",
                                command=self.show_frame_ipv4)
        ipv4_button.grid(row=0, column=0, padx=10, pady=10)
        ipv6_button = tk.Button(self.top_frame, text="IPv6 Rechner",
                                command=self.show_frame_ipv6)
        ipv6_button.grid(row=0, column=1, padx=10, pady=10)

        info_button = tk.Button(self.top_frame, text="Infos",
                                command=self.show_info_window)
        info_button.grid(row=0, column=2, padx=10, pady=10)

        close_button = tk.Button(self.top_frame, text="Schließen",
                                 command=self.close_window)
        close_button.grid(row=0, column=3, padx=10, pady=10)

        self.main_frame = tk.Frame(self.container)
        self.main_frame.pack(fill="both", expand=True, side="bottom")

        self.frames = {}

        for Page in (IPv4Page, IPv6Page):
            frame = Page(parent=self.main_frame)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IPv4Page)

    def show_frame_ipv4(self):
        self.show_frame(IPv4Page)
    
    def show_frame_ipv6(self):
        self.show_frame(IPv6Page)
    
        
    
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    def show_info_window(self):
        info_window = Info_Window(self)
        info_window.grab_set()

    def close_window(self):
        self.destroy()


#  start programm
start = Main()
start.mainloop()
