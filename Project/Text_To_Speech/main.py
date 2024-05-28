import pyttsx3
import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Text To Speech")
        self.root.geometry("500x180")

        self.label = tk.Label(self.root, text="Type what you want me to say!", font=('serif', 18))
        self.label.pack(padx=10, pady=12)

        self.textbox = tk.Entry(font=('serif', 18))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(text="CLICK ME!", font=('serif', 12), command=self.button_click)
        self.button.pack(padx=20, pady=15)

        self.root.mainloop()

    def button_click(self):
        engine = pyttsx3.init()
        engine.say(self.textbox.get())
        engine.runAndWait()

GUI()