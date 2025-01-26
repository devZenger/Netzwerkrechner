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

        label = tk.Label(self, text="IPv6:", font=("Arial", 14))
        label.grid(row=0, column=0, pady=10)

        ipv6_label = tk.Label(self, text="IP Adresse: ")
        ipv6_label.grid(row=2, column=0)
        self.ipv6_input = tk.Entry(self)
        self.ipv6_input.grid(row=2, column=1)

        cidir_label = tk.Label(self, text="CIDIR: ")
        cidir_label.grid(row=3, column=0)
        cidir_input = tk.Entry(self)
        cidir_input.grid(row=3, column=1)

        cal_ipv6 = tk.Button(self, text="berechnen", command=self.ipv6_cal)
        cal_ipv6.grid(row=3, column=2)

        self.error_output = tk.Label(self, text="")
        self.error_output.grid(row=4, column=1)


    # ipv6 calculation
    def ipv6_cal(self):
        ipv6_input = self.ipv6_input.get()
        try:
            ipv6_input = add_zero_to_ipv6_input(ipv6_input)
        except:
            self.error_output.config(text="Fehlerhafte Eingabe")
            

            
            
            
        print(ipv6_input)