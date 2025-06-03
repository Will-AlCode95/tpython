import tkinter as tk

janela = tk.Tk()
janela.title("Exercício com gerenciador de layout pack")
janela.geometry("400x300+500+200")

texto1 = tk.Label(janela, text="Texto 1 (label)",bg='gray',fg='white')
texto2 = tk.Label(janela, text="Texto 2 (label)",bg='gray',fg='white')
texto3 = tk.Label(janela, text="Texto 3 (label)",bg='gray',fg='white')

texto1.pack(side='left', fill='x', expand=True)
texto2.pack(side='left', fill='y', expand=True)
texto3.pack(side='right', fill='x', expand=True)

janela.mainloop()
