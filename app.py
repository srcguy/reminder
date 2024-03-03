import customtkinter
import os
import subprocess

godzina_var2 = "0"
minuta_var2 = "0"

def button_callback():
    file = open("data.txt", "w")
    file.write(godzina_var2)
    file.write("\n")
    file.write(minuta_var2)
    file.close()
    subprocess.run(["python", "timer.py"])

app = customtkinter.CTk()
app.geometry("180x270")

button = customtkinter.CTkButton(app, text="Ustaw przypomnienie", command=button_callback)
button.grid(row=5, column=0, padx=20, pady=(0, 20))

def godzina_callback(choice):
    global godzina_var2
    godzina_var2 = choice

def minuta_callback(choice):
    global minuta_var2
    minuta_var2 = choice

godzina_var = customtkinter.StringVar(value="00")
godzina = customtkinter.CTkOptionMenu(app,values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"],
                                         command=godzina_callback,
                                         variable=godzina_var)

godzina.grid(row=1, column=0, padx=20, pady=(0, 20))

godzina_tekst = customtkinter.CTkLabel(app, text="Wybierz godzine", fg_color="transparent")
godzina_tekst.grid(row=0, column=0, padx=20, pady=(0, 20))

minuta_var = customtkinter.StringVar(value="00")
minuta = customtkinter.CTkOptionMenu(app,values=["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"],
                                         command=minuta_callback,
                                         variable=minuta_var)

minuta.grid(row=3, column=0, padx=20, pady=(0, 20))

minuta_tekst = customtkinter.CTkLabel(app, text="Wybierz minute", fg_color="transparent")
minuta_tekst.grid(row=2, column=0, padx=20, pady=(0, 20))

app.mainloop()
