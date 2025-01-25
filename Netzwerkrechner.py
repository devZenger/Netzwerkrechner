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
        self.ipv4_input = tk.Entry(self)
        self.ipv4_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        self.cidir_input = tk.Entry(self)
        self.cidir_input.grid(row=3, column=1)

        cal_ipv4 = tk.Button(self, text="berechnen",
                             command=self.ipv4_calculation)
        cal_ipv4.grid(row=3, column=2)

        self.ipv4_output = tk.Label(self, text="")
        self.ipv4_output.grid(row=4, column=1)

        self.binary_ipv4_output = tk.Label(self, text="")
        self.binary_ipv4_output.grid(row=5, column=1)
        self.binary_subnet_mask_output = tk.Label(self, text="")
        self.binary_subnet_mask_output.grid(row=6, column=1)
        self.binary_net_id_output = tk.Label(self, text="")
        self.binary_net_id_output.grid(row=7, column=1)

    # calculation
    def ipv4_calculation(self):
        # IPv4 input check
        try:
            ipv4_input = self.ipv4_input.get()
            ipv4_splits = ipv4_input.split(".")
            ipv4_adresses = []
            for i in range(4):
                ipv4_adresses.append(int(ipv4_splits[i]))
        except:
            return self.ipv4_output.config(text="Fehlerhafte Eingabe")

        for ipv4_adress in ipv4_adresses:
            if ipv4_adress < 0 or ipv4_adress > 255:
                return self.ipv4_output.config(text="Fehlerhafte Eingabe")

        # CIDIR input check
        try:
            cidir = int(self.cidir_input.get())
        except:
            return self.ipv4_output.config(text="Fehlerhafte Eingabe")

        if cidir < 0 or cidir > 32:
            return self.ipv4_output.config(text="Fehlerhafte Eingabe")

        subnet_mask = [0]*4

        j = 0
        in_process = True
        while in_process is True:

            if cidir == 0:
                in_process = False

            elif cidir >= 8:
                subnet_mask[j] = 255

            elif 0 < cidir < 8:
                wild = 8 - cidir
                var_a = 0
                for w in range(wild):
                    var_a = var_a + 2**w
                var_b = 255 - var_a
                subnet_mask[j] = var_b
                break

            cidir = cidir - 8
            j += 1
        
        # net id calculation
        net_ids = []
        for i in range(4):
            net_ids.append(ipv4_adresses[i] & subnet_mask[i])

        net_id = " "
        for net in net_ids:
            net_id = net_id + str(net) + "."

        # format to binary
        binary_net_ids = []
        binary_subnets = []
        binary_ipv4_ads = []
        for i in range(4):
            binary_net_ids.append(format(net_ids[i], '08b'))
            binary_subnets.append(format(subnet_mask[i], '08b'))
            binary_ipv4_ads.append(format(ipv4_adresses[i], '08b'))

        binary_net_id_str = binary_net_ids[0] + binary_net_ids[1] + binary_net_ids[2] + binary_net_ids[3]
        binary_subnets_str = binary_subnets[0] + binary_subnets[1] +binary_subnets[2] + binary_subnets[3]
        binary_ipv4_ads_str = binary_ipv4_ads[0] + binary_ipv4_ads[1] +binary_ipv4_ads[2] +binary_ipv4_ads[3]
        
        self.binary_ipv4_output.config(text=f"{binary_ipv4_ads_str}")
       
        self.binary_subnet_mask_output.config(text=f"{binary_subnets_str}")
        
        self.binary_net_id_output.config(text=f"{binary_net_id_str}")
       
        
        return self.ipv4_output.config(text=f"{binary_net_id_str}")



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
