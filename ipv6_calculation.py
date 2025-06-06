import tkinter as tk
from save_output import Save_Output_Window


def in_short(to_forms):
    current_count = 0
    max_count = 0
    current_index = 0
    max_index = -1
    for i, form in enumerate(to_forms):
        if form == 0:
            if current_count == 0:
                current_index = i
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_index = current_index
            current_count = 0

    if current_count > max_count:
        max_count = current_count
        max_index = current_index

    strForm = ""

    for i, form in enumerate(to_forms):

        if i == max_index:
            strForm = f"{strForm}:"

        elif max_index < i < (max_index + max_count):
            continue
        else:
            strForm = f"{strForm}{form:x}:"

    if strForm[-2] != ":":
        strForm = strForm[:-1]
    return strForm


def in_one_hex_str(to_form):
    str_hex = ""
    for form in to_form:
        hex = f"{form:x}".rjust(4, '0')
        str_hex = f"{str_hex}{hex}:"

    return str_hex[:-1]


def input_zero(input, zero):
    for i in range(len(input)):
        if input[i] == ":" and input[i+1] == ":":
            rev = i + 1 - len(input)
            input = input[:i] + zero + input[rev:]
            break

    return input


def add_zero_to_ipv6_input(input):
    if input[len(input)-1] == ":":
        input = input + "0"

    count = input.count(":")
    if count < 8:
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
    else:
        raise ValueError("too many ':'")
    return input


class IPv6Page(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        default_setting = {'padx': (20, 5), 'pady': 5, 'sticky': "ew"}

        label = tk.Label(self, text="IPv6:", font=(14))
        label.grid(row=0, column=0, pady=10)

        self.grid_columnconfigure(0, minsize=240)

        ipv6_label = tk.Label(self, text="IP Adresse: ")
        ipv6_label.grid(row=2, column=0)
        self.ipv6_input = tk.Entry(self, width=39)
        self.ipv6_input.grid(row=2, column=1, sticky="e")

        prefix_label = tk.Label(self, text="Präfix: ")
        prefix_label.grid(row=3, column=0)
        self.prefix_input = tk.Entry(self, width=3)
        self.prefix_input.grid(row=3, column=1,  sticky="e")

        cal_ipv6 = tk.Button(self, text="Berechnen", command=self.ipv6_cal)
        cal_ipv6.grid(row=3, column=2)

        self.error_output = tk.Label(self, text="")
        self.error_output.grid(row=4, column=1, sticky="w")

        ipv6_output_label = tk.Label(self, text="IPv6 Adresse: ", anchor="w")
        ipv6_output_label.grid(**default_setting, row=5, column=0)
        self.ipv6_output = tk.Label(self, text="")
        self.ipv6_output.grid(row=5, column=1)
        self.ipv6_short_output = tk.Label(self, text="")
        self.ipv6_short_output.grid(row=5, column=2)

        prefix_output_label = tk.Label(self, text="Präfix: ", anchor="w")
        prefix_output_label.grid(**default_setting, row=6, column=0)
        self.prefix_output = tk.Label(self, text="")
        self.prefix_output.grid(row=6, column=1)
        self.prefix_short_output = tk.Label(self, text="")
        self.prefix_short_output.grid(row=6, column=2)

        net_id_output_label = tk.Label(self, text="Netzwerkadresse: ", anchor="w")
        net_id_output_label.grid(**default_setting, row=7, column=0)
        self.net_id_output = tk.Label(self, text="")
        self.net_id_output.grid(row=7, column=1)
        self.net_id_short_output = tk.Label(self, text="")
        self.net_id_short_output.grid(row=7, column=2)

        last_host_output_label = tk.Label(self, text="Letzte Hostadresse:", anchor="w")
        last_host_output_label.grid(**default_setting, row=8, column=0)
        self.last_host_output = tk.Label(self, text="")
        self.last_host_output.grid(row=8, column=1)
        self.last_hosts_short_output = tk.Label(self, text="", width=42)
        self.last_hosts_short_output.grid(row=8, column=2)

        hosts_output_label = tk.Label(self, text="Hostanzahl: ", anchor="w")
        hosts_output_label.grid(**default_setting, row=9, column=0)
        self.hosts_output = tk.Label(self, text="")
        self.hosts_output.grid(row=9, column=1)
        self.hosts_short_output = tk.Label(self, text="")
        self.hosts_short_output.grid(row=9, column=2)

        bt_frame = tk.Frame(self)
        bt_frame.grid(row=10, column=2)

        bt_save_ipv4_output = tk.Button(bt_frame, text="Ergebnis speichern", command=self.open_save_window)
        bt_save_ipv4_output.pack(pady=0, padx=10, side=tk.LEFT)

        bt_clear_output = tk.Button(bt_frame, text="Zurücksetzen", command=self.clear_output)
        bt_clear_output.pack(pady=0, padx=10, side=tk.LEFT)

    # open save window
    def open_save_window(self):
        try:
            output_head = f"IPv6:\nBerechnung für {self.ipv6_hex_str.strip()}"
            output_ip = (
                f"Ipv6 Adresse:       {self.ipv6_hex_str}\t {self.ipv6_short_str}")
            output_prefix = (
                f"Präfix:             {self.prefix_hex_str}\t {self.prefix_short_str}\n")
            output_net_id = (
                f"Netzwerkadresse:    {self.net_id_hex_str}\t {self.net_id_short_str}")
            output_hosts = (
                f"Hostanzahl:{" "*(51-len(self.hosts_str))}{self.hosts_str}\n")
            output_last_adress = (
                f"Letzte Hostadresse: {self.last_host_adress_hex_str}\n\n")
            output_head = f"{output_head}\n{"─"*len(output_prefix)}"
            output = [output_head, output_ip, output_prefix, output_net_id, output_hosts, output_last_adress]
            save_window = Save_Output_Window(self, output)
            save_window.grab_set()
        except Exception as e:
            self.error_output.config(text=f"Fehlerhafte Eingabe: {type(e).__name__}")

    # ipv6 calculation
    def ipv6_cal(self):
        error_message = "Fehlerhafte IPv6 Adresse"
        ipv6_input = self.ipv6_input.get()
        try:
            ipv6_input = add_zero_to_ipv6_input(ipv6_input)

        except ValueError:
            self.clear_output()
            return self.error_output.config(text=error_message)

        except Exception as e:
            self.clear_output()
            return self.error_output.config(text=f"Fehlerhafte Eingabe: {type(e).__name__}")

        ipv6_adresses = []
        try:
            ipv6_input_splits = ipv6_input.split(":")
            for ipv6 in ipv6_input_splits:
                ipv6_adresses.append(int(ipv6, 16))
        except ValueError:
            self.clear_output()
            return self.error_output.config(text=error_message)
        except Exception as e:
            self.clear_output()
            return self.error_output.config(text=f"Fehlerhafte Eingabe: {type(e).__name__}")

        if len(ipv6_adresses) != 8:
            self.clear_output()
            return self.error_output.config(text="Fehlerhafte Adresseingabe")
        try:
            prefix_bit = int(self.prefix_input.get())
        except ValueError:
            self.clear_output()
            return self.error_output.config(text="Fehlerhafte Präfix Eingabe")
        except Exception as e:
            self.clear_output()
            return self.error_output.config(text=f"Fehlerhafte Eingabe: {type(e).__name__}")

        if prefix_bit < 0 or prefix_bit > 128:
            self.clear_output()
            return self.error_output.config(text="Fehlerhafte Präfix Eingabe")

        # prefix calculation
        in_process = True
        j = 0
        prefix = [0]*8
        prefix_bit_save = prefix_bit

        while in_process is True:
            if prefix_bit == 0:
                in_process = False
            elif prefix_bit >= 16:
                prefix[j] = 65_535
            elif 0 < prefix_bit < 16:
                wild = 16 - prefix_bit
                dekaexi = 0
                for w in range(wild):
                    dekaexi = dekaexi + 2**w
                dekaexi_re = 65_535 - dekaexi
                prefix[j] = dekaexi_re
                break

            prefix_bit = prefix_bit - 16
            j += 1

        prefix_bit = prefix_bit_save

        # net id calculation and last adress
        net_ids = []
        last_adresses = [65_535] * 8
        for i in range(8):
            net_ids.append(ipv6_adresses[i] & prefix[i])
            last_adresses[i] = last_adresses[i] - prefix[i]
            last_adresses[i] = last_adresses[i] + net_ids[i]

        prefix_bit_str = f"/{prefix_bit}"
        prefix_space = " " * len(prefix_bit_str)

        # number of hosts
        hosts_bits = 128 - prefix_bit
        hosts = 2**hosts_bits
        self.hosts_str = f"{hosts:,.0f}".rjust((39+len(prefix_bit_str)))
        self.hosts_output.config(text=f"{self.hosts_str}")

        self.ipv6_hex_str = f"{in_one_hex_str(ipv6_adresses)}{prefix_bit_str}"
        self.ipv6_output.config(text=f"{self.ipv6_hex_str}")

        self.prefix_hex_str = f"{in_one_hex_str(prefix)}{prefix_space}"
        self.prefix_output.config(text=f"{self.prefix_hex_str}")

        self.net_id_hex_str = f"{in_one_hex_str(net_ids)}{prefix_bit_str}"
        self.net_id_output.config(text=f"{self.net_id_hex_str}")

        self.last_host_adress_hex_str = f"{in_one_hex_str(last_adresses)}{prefix_bit_str}"
        self.last_host_output.config(text=f"{self.last_host_adress_hex_str}")

        self.ipv6_short_str = f"{in_short(ipv6_adresses)}{prefix_bit_str}"
        str_length = len(self.ipv6_short_str)
        self.prefix_short_str = f"{in_short(prefix)}"
        if len(self.prefix_short_str) > str_length:
            str_length = len(self.prefix_short_str)
        self.net_id_short_str = f"{in_short(net_ids)}{prefix_bit_str}"
        if len(self.net_id_short_str) > str_length:
            str_length = len(self.net_id_short_str)
        self.hosts_short = "{:.2e}".format(hosts)
        if len(self.hosts_short) > str_length:
            str_length = len(self.hosts_short)
        self.last_host_adress_short = f"{in_short(last_adresses)}{prefix_bit_str}"
        if len(self.last_host_adress_short) > str_length:
            str_length = len(self.last_host_adress_short)

        self.hosts_short_output.config(text=f"{self.hosts_short.rjust(str_length)}")

        self.ipv6_short_output.config(text=f"{self.ipv6_short_str.rjust(str_length)}")

        self.prefix_short_output.config(text=f"{self.prefix_short_str.rjust(str_length)}")

        self.net_id_short_output.config(text=f"{self.net_id_short_str.rjust(str_length)}")

        self.last_hosts_short_output.config(text=f"{self.last_host_adress_short.rjust(str_length)}")

        return self.error_output.config(text="Ergebnis:")

    def clear_output(self):
        self.ipv6_output.config(text=" ")
        self.prefix_output.config(text=" ")
        self.net_id_output.config(text=" ")
        self.last_host_output.config(text=" ")
        self.ipv6_short_output.config(text=" ")
        self.prefix_short_output.config(text=" ")
        self.net_id_short_output.config(text=" ")
        self.hosts_short_output.config(text=" ")
        self.hosts_output.config(text=" ")
        self.last_hosts_short_output.config(text=" ")
