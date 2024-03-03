import customtkinter
import pygame

def play_wav(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

wav_file_path = "reminder.wav"

app = customtkinter.CTk()
app.geometry("300x300")

tekst = customtkinter.CTkLabel(app, text="Przypominajka!", fg_color="transparent")
tekst.pack(side='left', fill='both', expand=True)

play_wav(wav_file_path)

app.mainloop()