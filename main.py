import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    milha = entradaInt.get()
    km = milha * 1.61
    outputString.set(km)

#janela
janela = ttk.Window(themename="darkly")
janela.title("demo")
janela.geometry("300x150")

#titulo
textoTitulo = ttk.Label(master=janela, text="Milhas para quilometros", font="Calibre 16")
textoTitulo.pack()

#campo de imput
imputFrame = ttk.Frame(master=janela)
entradaInt = tk.IntVar()
entrada = ttk.Entry(master=imputFrame, textvariable=entradaInt)
button = ttk.Button(master=imputFrame, text="converter", command= convert)
imputFrame.pack(pady=10)
entrada.pack(side="left", padx=10)
button.pack(side="left")

#output
outputString = tk.StringVar()
outputFrame = ttk.Label(master=janela, text="saida", font="Calibre 16", textvariable=outputString)
outputFrame.pack()

#run app
janela.mainloop()