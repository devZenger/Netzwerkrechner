import tkinter as tk


def input_zero(input, zero):
    for i in range(len(input)):
        if input[i] == ":" and input[i+1] == ":":
            rev = i + 1- len(input)
            print(f"i ={i}  und rev = {rev}  und länge = {len(input)}")
            print(input[:i])
            input = input[:i] + zero + input[rev:]
    return input


def add_zero_to_ipv6_input(input):
    if input[len(input)-1] == ":":
        input = input + "0"

    count = input.count(":")
    if count < 8:
        print("matchS")
        match count:
            case 7:
                input = input_zero(input, ":0")
            case 6:
                input = input_zero(input, ":0:0")
            case 5:
                input = input_zero(input, ":0:0:0")
            case 4:
                input = input_zero(input, ":0:0:0:0")
            case 3:
                input = input_zero(input, ":0:0:0:0:0")
            case 2:
                input = input_zero(input, ":0:0:0:0:0:0")
            case 1:
                input = input_zero(input, ":0:0:0:0:0:0:0")
            case _:
                input = "Error"

    return input



class IPv6Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        default_setting = {'padx':(20,5), 'pady': 5, 'sticky': "ew"}

        label = tk.Label(self, text="IPv6:", font=(14))
        label.grid(row=0, column=0, pady=10)

        ipv6_label = tk.Label(self, text="IP Adresse: ")
        ipv6_label.grid(row=2, column=0)
        self.ipv6_input = tk.Entry(self)
        self.ipv6_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        self.cidir_input = tk.Entry(self)
        self.cidir_input.grid(row=3, column=1)

        cal_ipv6 = tk.Button(self, text="berechnen", command=self.ipv6_cal)
        cal_ipv6.grid(row=3, column=2)

        self.error_output = tk.Label(self, text="")
        self.error_output.grid(row=4, column=1)
        
        ipv6_output_label = tk.Label(self, text="IPv6 Adresse: ", anchor="w")
        ipv6_output_label.grid(**default_setting, row=5, column=0)
        self.ipv6_output = tk.Label(self, text="")
        self.ipv6_output.grid(row=5, column=1)

        subnet_mask_output_label = tk.Label(self, text="Subnetzmaske: ", anchor="w")
        subnet_mask_output_label.grid(**default_setting, row=6, column=0)
        self.subnet_mask_output = tk.Label(self, text="")
        self.subnet_mask_output.grid(row=6, column=1)

        wildcard_mask_output_label = tk.Label(self, text="Wildcard-Maske: ", anchor="w")
        wildcard_mask_output_label.grid(**default_setting, row=7, column=0)
        self.wildcard_mask_output = tk.Label(self, text="")
        self.wildcard_mask_output.grid(row=7, column=1)

        net_id_output_label = tk.Label(self, text="Netzwerkadresse: ", anchor="w")
        net_id_output_label.grid(**default_setting, row=8, column=0)
        self.net_id_output = tk.Label(self, text="")
        self.net_id_output.grid(row=8, column=1)

        broadcast_output_label = tk.Label(self, text="Broadcast-Adresse:", anchor="w")
        broadcast_output_label.grid(**default_setting, row=9, column=0)
        self.broadcast_output = tk.Label(self, text="")
        self.broadcast_output.grid(row=9, column=1)


    # ipv6 calculation
    def ipv6_cal(self):
        ipv6_input = self.ipv6_input.get()
        try:
            ipv6_input = add_zero_to_ipv6_input(ipv6_input)
        except:
            return self.error_output.config(text="Fehlerhafte Eingabe")  

        ipv6_adresses = []
        try:
            ipv6_input_splits = ipv6_input.split(":")
            for ipv6 in ipv6_input_splits:
                ipv6_adresses.append(int(ipv6, 16))
        except:
            self.error_output.config(text="Fehlerhafte Eingabe")

        if len(ipv6_adresses) != 8:
            print(len(ipv6_adresses))
            self.error_output.config(text="Fehlerhafte Eingabe")

        try:
            cidir = int(self.cidir_input.get())
        except:
            self.error_output.config(text="Fehlerhafte Eingabe")
            

        if cidir < 0 or cidir > 128 :
            self.error_output.config(text="Fehlerhafte Eingabe")
        
        for i in ipv6_adresses:
            print(i, end="  ")



        print(ipv6_input)