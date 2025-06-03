import tkinter as tk
from tkinter import messagebox

def diz_oi():
    valor_a = tx_a.get()
    valor_b = tx_b.get()
    messagebox.showinfo("Diz oi", f"Olá: {valor_a} {valor_b}!")

def somar():
    valor_a = float(tx_a.get())
    valor_b = float(tx_b.get())
    messagebox.showinfo("A soma é...", f"{valor_a} + {valor_b} = {valor_a + valor_b}")

janela = tk.Tk()
janela.geometry("500x400+100+100")

frame_topo = tk.Frame(janela, bg='gray')
frame_esq = tk.Frame(janela, bg='gray')
frame_principal = tk.Frame(janela)

botao1 = tk.Button(frame_topo, text='Dizer oi', command = diz_oi)
botao2 = tk.Button(frame_topo, text='Somar', command = somar)
botao3 = tk.Button(frame_topo, text='Botão 3')
botao4 = tk.Button(frame_esq, text='Botão 4')

lbl_a = tk.Label(frame_principal, text="A:")
lbl_b = tk.Label(frame_principal, text="B:")

tx_a = tk.Entry(frame_principal)
tx_b = tk.Entry(frame_principal)

frame_topo.pack(side='top', fill='x')
frame_esq.pack(side='left', fill='y')
frame_principal.pack(side='left', fill='both', expand=True)

botao1.pack(padx=5, pady=10, side='left')
botao2.pack(padx=5, pady=10, side='left', expand=True)
botao3.pack(padx=5, pady=10, side='right')
botao4.pack(padx=20, pady=20)

lbl_a.pack(side='left')
tx_a.pack(side='left')
lbl_b.pack(side='left')
tx_b.pack(side='left')

janela.mainloop()