import tkinter as tk


def in_one_binary_string(to_form, cidir):
    out = []
    for i in range(4):
        out.append(format(to_form[i], '08b'))
    in_process = True
    j = 0
    while in_process is True:
        if 0 < cidir < 8:
            out[j] = out[j][:cidir] + " " + out[j][cidir:]
            in_process = False
        elif cidir == 0:
            in_process = False
        else:
            cidir = cidir - 8
        j += 1

    in_one = f"{out[0]}.{out[1]}.{out[2]}.{out[3]}"
    return in_one

def in_one_decimal_string(to_form):
    out = ""
    for form in to_form:
        out = out + str(form) + "."
    out = out[:-1]
    return out



class IPv4Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="IPv4:", font=(14))
        label.grid(row=0, column=0, pady=10)

        ipv4_label = tk.Label(self, text="IP Adresse: ")
        ipv4_label.grid(row=2, column=0)
        self.ipv4_input = tk.Entry(self)
        self.ipv4_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        self.cidir_input = tk.Entry(self)
        self.cidir_input.grid(row=3, column=1)

        cal_ipv4 = tk.Button(self, text="berechnen", command=self.ipv4_cal)
        cal_ipv4.grid(row=3, column=2)

        default_setting = {'padx':(20,5), 'pady': 5, 'sticky': "ew"}

        self.error_output = tk.Label(self, text="")
        self.error_output.grid(row=4, column=1)

        ipv4_output_label = tk.Label(self, text="IPv4 Adresse: ", anchor="w")
        ipv4_output_label.grid(**default_setting, row=5, column=0)
        self.deci_ipv4_output = tk.Label(self, text="")
        self.deci_ipv4_output.grid(row=5, column=1)
        self.binary_ipv4_output = tk.Label(self, text="")
        self.binary_ipv4_output.grid(row=5, column=2)

        subnet_mask_output_label = tk.Label(self, text="Subnetzmaske: ", anchor="w")
        subnet_mask_output_label.grid(**default_setting, row=6, column=0)
        self.deci_subnet_mask_output = tk.Label(self, text="")
        self.deci_subnet_mask_output.grid(row=6, column=1)
        self.binary_subnet_mask_output = tk.Text(self, height=1, width=36)
        self.binary_subnet_mask_output.grid(row=6, column=2)
        self.binary_subnet_mask_output.tag_configure("red", foreground="red")
        self.binary_subnet_mask_output.tag_configure("green", foreground="green")

        wildcard_mask_output_label = tk.Label(self, text="Wildcard-Maske: ", anchor="w")
        wildcard_mask_output_label.grid(**default_setting, row=7, column=0)
        self.deci_wildcard_mask_output = tk.Label(self, text="")
        self.deci_wildcard_mask_output.grid(row=7, column=1)
        self.binary_wildcard_mask_output = tk.Label(self, text="")
        self.binary_wildcard_mask_output.grid(row=7, column=2)

        net_id_output_label = tk.Label(self, text="Netzwerkadresse: ", anchor="w")
        net_id_output_label.grid(**default_setting, row=9, column=0)
        self.deci_net_id_output = tk.Label(self, text="")
        self.deci_net_id_output.grid(row=9, column=1)
        self.binary_net_id_output = tk.Label(self, text="")
        self.binary_net_id_output.grid(row=9, column=2)

        broadcast_output_label = tk.Label(self, text="Broadcast-Adresse:", anchor="w")
        broadcast_output_label.grid(**default_setting, row=10, column=0)
        self.deci_broadcast_output = tk.Label(self, text="")
        self.deci_broadcast_output.grid(row=10, column=1)
        self.binary_broadcast_output = tk.Label(self, text="")
        self.binary_broadcast_output.grid(row=10, column=2)

    # calculation
    def ipv4_cal(self):
        # IPv4 input check
        try:
            ipv4_input = self.ipv4_input.get()
            ipv4_splits = ipv4_input.split(".")
            ipv4_adresses = []
            for i in range(4):
                ipv4_adresses.append(int(ipv4_splits[i]))
        except:
            return self.error_output.config(text="Fehlerhafte Eingabe")

        for ipv4_adress in ipv4_adresses:
            if ipv4_adress < 0 or ipv4_adress > 255:
                return self.error_output.config(text="Fehlerhafte Eingabe")

        # CIDIR input check
        try:
            cidir = int(self.cidir_input.get())
        except:
            return self.error_output.config(text="Fehlerhafte Eingabe")

        if cidir < 0 or cidir > 32:
            return self.error_output.config(text="Fehlerhafte Eingabe")

        subnet_mask = [0]*4
        wildcard_mask = [255]*4
        j = 0
        in_process = True
        cidir_use = cidir
        while in_process is True:

            if cidir_use == 0:
                in_process = False

            elif cidir_use >= 8:
                subnet_mask[j] = 255
                wildcard_mask[j] = 0

            elif 0 < cidir_use < 8:
                wild = 8 - cidir_use
                oktett = 0
                for w in range(wild):
                    oktett = oktett + 2**w
                oktett_re = 255 - oktett
                subnet_mask[j] = oktett_re
                wildcard_mask[j] = oktett
                break

            cidir_use = cidir_use - 8
            j += 1

        # net id calculation & broadcast ip
        net_ids = []
        broadcasts = []
        for i in range(4):
            net_ids.append(ipv4_adresses[i] & subnet_mask[i])
            broadcasts.append(net_ids[i] | wildcard_mask[i])

        # format to decimal string
        deci_ipv4_str = in_one_decimal_string(ipv4_adresses)
        self.deci_ipv4_output.config(text=f"{deci_ipv4_str}")
        deci_subnets_str = in_one_decimal_string(subnet_mask)
        self.deci_subnet_mask_output.config(text=f"{deci_subnets_str}")
        deci_wildcard_maks_str = in_one_decimal_string(wildcard_mask)
        self.deci_wildcard_mask_output.config(text=f"{deci_wildcard_maks_str}")
        
        deci_net_id_str = in_one_decimal_string(net_ids)
        self.deci_net_id_output.config(text=f"{deci_net_id_str}")
        deci_broadcast_str = in_one_decimal_string(broadcasts)
        self.deci_broadcast_output.config(text=f"{deci_broadcast_str}")

        # format to binary
        binary_ipv4_ads = in_one_binary_string(ipv4_adresses, cidir)
        #binary_subnets = in_one_binary_string(subnet_mask, cidir)
        binary_wildcards = in_one_binary_string(wildcard_mask, cidir)

        binary_net_id = in_one_binary_string(net_ids, cidir)
        binary_broadcast_ip = in_one_binary_string(broadcasts, cidir)

        self.binary_ipv4_output.config(text=f"{binary_ipv4_ads}") 
        #self.binary_subnet_mask_output.config(text=f"{binary_subnets}")
        self.binary_wildcard_mask_output.config(text=f"{binary_wildcards}")
        self.binary_net_id_output.config(text=f"{binary_net_id}")
        self.binary_broadcast_output.config(text=f"{binary_broadcast_ip}")

        binary_subnets = []
        for i in range(4):
            binary_subnets.append(format(subnet_mask[i], '08b'))

        for i in range(len(binary_subnets)):
            count = binary_subnets[i].count("1")
            print(count)
            if count == 8:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i], "red")
                self.binary_subnet_mask_output.insert("end", ".", "black")
            if 0 < count < 8:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i][:count], "red")
                self.binary_subnet_mask_output.insert("end", binary_subnets[i][count:], "green")
                self.binary_subnet_mask_output.insert("end", ".", "black")
            if count == 0 and i != 3:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i], "green")
                self.binary_subnet_mask_output.insert("end", ".", "black")
            if count == 0 and i == 3:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i], "green")
              




        return self.error_output.config(text="Ergebnis:")
