import tkinter as tk
from save_output import Save_Output_Window


def number_of_hosts(wildmask):
    numbers = wildmask.count("1")
    hosts = 2**numbers - 2
    if hosts == -1:
        hosts = 1
    elif hosts == 0:
        hosts = 2
    return str(hosts)


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
    def __init__(self, parent):
        super().__init__(parent)

        label = tk.Label(self, text="IPv4:", font=(14))
        label.grid(row=0, column=0, pady=10)

        self.grid_columnconfigure(0, minsize=240)

        ipv4_label = tk.Label(self, text="IP Adresse: ")
        ipv4_label.grid(row=2, column=0)
        self.ipv4_input = tk.Entry(self)
        self.ipv4_input.grid(row=2, column=1, sticky="w")

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        self.cidir_input = tk.Entry(self)
        self.cidir_input.grid(row=3, column=1, sticky="w")

        cal_ipv4 = tk.Button(self, text="berechnen", command=self.ipv4_cal)
        cal_ipv4.grid(row=3, column=2)

        default_setting = {'padx': (20, 5), 'pady': 5, 'sticky': "ew"}

        self.error_output = tk.Label(self, text="")
        self.error_output.grid(row=4, column=1, sticky="w")

        ipv4_output_label = tk.Label(self, text="IPv4 Adresse: ", anchor="w")
        ipv4_output_label.grid(**default_setting, row=5, column=0)
        self.deci_ipv4_output = tk.Label(self, text="")
        self.deci_ipv4_output.grid(row=5, column=1)
        self.binary_ipv4_output = tk.Label(self, text="")
        self.binary_ipv4_output.grid(row=5, column=2, padx=(20, 0), sticky="e")

        subnet_mask_output_label = tk.Label(self, text="Subnetzmaske: ", anchor="w")
        subnet_mask_output_label.grid(**default_setting, row=6, column=0)
        self.deci_subnet_mask_output = tk.Label(self, text="")
        self.deci_subnet_mask_output.grid(row=6, column=1)
        self.binary_subnet_mask_output = tk.Text(self, height=1, width=36,
                                                 relief=tk.FLAT, bg=self['bg'], state=tk.DISABLED)
        self.binary_subnet_mask_output.grid(row=6, column=2, padx=(20, 0), sticky="e")

        self.binary_subnet_mask_output.tag_configure("red", foreground="red")
        self.binary_subnet_mask_output.tag_configure("green", foreground="green")

        wildcard_mask_output_label = tk.Label(self, text="Wildcard-Maske: ", anchor="w")
        wildcard_mask_output_label.grid(**default_setting, row=7, column=0)
        self.deci_wildcard_mask_output = tk.Label(self, text="")
        self.deci_wildcard_mask_output.grid(row=7, column=1)
        self.binary_wildcard_mask_output = tk.Label(self, text="")
        self.binary_wildcard_mask_output.grid(row=7, column=2, padx=(20, 0), sticky="e")

        net_id_output_label = tk.Label(self, text="Netzwerkadresse: ", anchor="w")
        net_id_output_label.grid(**default_setting, row=8, column=0)
        self.deci_net_id_output = tk.Label(self, text="")
        self.deci_net_id_output.grid(row=8, column=1)
        self.binary_net_id_output = tk.Label(self, text="")
        self.binary_net_id_output.grid(row=8, column=2, padx=(20, 0), sticky="e")

        broadcast_output_label = tk.Label(self, text="Broadcast-Adresse:", anchor="w")
        broadcast_output_label.grid(**default_setting, row=9, column=0)
        self.deci_broadcast_output = tk.Label(self, text="")
        self.deci_broadcast_output.grid(row=9, column=1)
        self.binary_broadcast_output = tk.Label(self, text="")
        self.binary_broadcast_output.grid(row=9, column=2, padx=(20, 0), sticky="e")

        hosts_output_label = tk.Label(self, text="Hostanzahl: ", anchor="w")
        hosts_output_label.grid(**default_setting, row=10, column=0)
        self.hosts_output = tk.Label(self, text="")
        self.hosts_output.grid(row=10, column=1)

        bt_frame = tk.Frame(self)
        bt_frame.grid(row=11, column=2)

        bt_save_ipv4_output = tk.Button(bt_frame, text="Ergebnis speichern", command=self.open_save_window)
        bt_save_ipv4_output.pack(pady=0, padx=10, side=tk.LEFT)

        bt_clear_output = tk.Button(bt_frame, text="zurücksetzen", command=self.clear_output)
        bt_clear_output.pack(pady=0, padx=10, side=tk.LEFT)

    # open save window
    def open_save_window(self):
        try:
            output_head = f"IPv4:\nBerechnung für {self.deci_ipv4_str}\\{cidir}\n\n"
            output_ip = f"Ipv4 Adresse:\t\t{self.deci_ipv4_str}\t\t{self.binary_ipv4_ads}\n"  
            output_subnet = f"Subnetzmaske:\t\t{self.deci_subnets_str}\t\t{self.binary_subnets_black}\n"
            output_wildcard = f"Wildcard-Maske:\t\t{self.deci_wildcard_maks_str}\t\t{self.binary_wildcards}\n"
            output_net_id = f"Netzwerkadresse:\t{self.deci_net_id_str}\t\t{self.binary_net_id}\n"
            output_broadcast = f"Broadcast-Adresse:\t{self.deci_broadcast_str}\t\t{self.binary_broadcast_ip}\n"
            output_hosts = f"Hostanzahl:\t\t\t{self.hosts_str}\n" 
            output = [output_head, output_ip, output_subnet, output_wildcard, output_net_id, output_broadcast, output_hosts]
            save_window = Save_Output_Window(self, output)
            save_window.grab_set()
        except Exception as e:
            self.error_output.config(text=f"Fehlerhafte Eingabe, {type(e).__name__}")

    # calculation
    def ipv4_cal(self):
        error_message = "Fehlerhafte IPv4 Adresse"
        # IPv4 input check
        try:
            ipv4_input = self.ipv4_input.get()
            ipv4_splits = ipv4_input.split(".")
            ipv4_adresses = []
            if len(ipv4_splits) != 4:
                self.clear_output()
                return self.error_output.config(text=f"{error_message}")
            for i in range(4):
                ipv4_adresses.append(int(ipv4_splits[i]))
        except ValueError:
            self.clear_output()
            return self.error_output.config(text=error_message)
        except Exception as e:
            self.clear_output()
            return self.error_output.config(text=f"Fehler: {type(e).__name__}")


        for ipv4_adress in ipv4_adresses:
            if ipv4_adress < 0 or ipv4_adress > 255:
                self.clear_output()
                return self.error_output.config(text=f"{error_message}")

        # CIDIR input check
        try:
            global cidir
            cidir = int(self.cidir_input.get())
        except Exception as e:
            self.clear_output()
            return self.error_output.config(text=f"Fehler: {type(e).__name__}")

        if cidir < 0 or cidir > 32:
            self.clear_output()
            return self.error_output.config(text="Fehlerhafte CIDIR Eingabe")

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
        self.deci_ipv4_str = (in_one_decimal_string(ipv4_adresses)).rjust(15)
        self.deci_ipv4_output.config(text=f"{self.deci_ipv4_str}")
        self.deci_subnets_str = (in_one_decimal_string(subnet_mask)).rjust(15)
        self.deci_subnet_mask_output.config(text=f"{self.deci_subnets_str}")
        self.deci_wildcard_maks_str = (in_one_decimal_string(wildcard_mask)).rjust(15)
        self.deci_wildcard_mask_output.config(text=f"{self.deci_wildcard_maks_str}")
        self.deci_net_id_str = (in_one_decimal_string(net_ids)).rjust(15)
        self.deci_net_id_output.config(text=f"{self.deci_net_id_str}")
        self.deci_broadcast_str = (in_one_decimal_string(broadcasts)).rjust(15)
        self.deci_broadcast_output.config(text=f"{self.deci_broadcast_str}")

        # format to binary
        self.binary_ipv4_ads = in_one_binary_string(ipv4_adresses, cidir)
        self.binary_ipv4_output.config(text=f"{self.binary_ipv4_ads}")

        self.binary_subnets_black = in_one_binary_string(subnet_mask, cidir)

        self.binary_wildcards = in_one_binary_string(wildcard_mask, cidir)
        self.binary_wildcard_mask_output.config(text=f"{self.binary_wildcards}")

        self.binary_net_id = in_one_binary_string(net_ids, cidir)
        self.binary_net_id_output.config(text=f"{self.binary_net_id}")

        self.binary_broadcast_ip = in_one_binary_string(broadcasts, cidir)
        self.binary_broadcast_output.config(text=f"{self.binary_broadcast_ip}")

        self.hosts_str = number_of_hosts(self.binary_wildcards).rjust(15)
        self.hosts_output.config(text=self.hosts_str)

        binary_subnets = []
        for i in range(4):
            binary_subnets.append(format(subnet_mask[i], '08b'))

        self.binary_subnet_mask_output.config(state=tk.NORMAL)
        self.binary_subnet_mask_output.delete('1.0', tk.END)

        if cidir == 8 or cidir == 16 or cidir == 24 or cidir == 32:
            self.binary_subnet_mask_output.insert("end", " ")

        for i in range(len(binary_subnets)):
            count = binary_subnets[i].count("1")
            if count == 8:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i],
                                                      "red")
                if i < 3:
                    self.binary_subnet_mask_output.insert("end", ".", "black")

            if 0 < count < 8:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i][:count], "red")
                self.binary_subnet_mask_output.insert("end", " ", "black")
                self.binary_subnet_mask_output.insert("end", binary_subnets[i][count:], "green")
                self.binary_subnet_mask_output.insert("end", ".", "black")
            if count == 0 and i != 3:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i], "green")
                self.binary_subnet_mask_output.insert("end", ".", "black")
            if count == 0 and i == 3:
                self.binary_subnet_mask_output.insert("end", binary_subnets[i], "green")

        self.binary_subnet_mask_output.config(state=tk.DISABLED)

        return self.error_output.config(text="Ergebnis:")

    def clear_output(self):
        self.deci_ipv4_output.config(text=" ")
        self.deci_subnet_mask_output.config(text=" ")
        self.deci_wildcard_mask_output.config(text=" ")
        self.deci_net_id_output.config(text=" ")
        self.deci_broadcast_output.config(text=" ")
        self.binary_ipv4_output.config(text=" ")
        self.binary_subnet_mask_output.config(state=tk.NORMAL)
        self.binary_subnet_mask_output.delete("1.0", tk.END)
        self.binary_subnet_mask_output.config(state=tk.DISABLED)
        self.binary_wildcard_mask_output.config(text=" ")
        self.binary_net_id_output.config(text=" ")
        self.binary_broadcast_output.config(text=" ")
        self.hosts_output.config(text=" ")
