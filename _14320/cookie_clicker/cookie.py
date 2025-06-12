#
# Model
#

class Cookie():
    def __init__(self):
        self.quantidade = 0
        self.cursores = 0
        self.vovos = 0
        self.preco_do_cursor = 50
        self.preco_da_vovo = 1000


cookie = Cookie()


#
# Controller
#

def atualizar_botoes_upgrades():
    # atualizar botões interface de controle
    if cookie.quantidade > cookie.preco_do_cursor:
        botao_cursor.configure(state="active")
    else:
        botao_cursor.configure(state="disabled")
       
    if cookie.quantidade > cookie.preco_da_vovo:
        botao_vovo.configure(state="active")
    else:
        botao_vovo.configure(state="disabled")

def ganhar_cookie():
    cookie.quantidade += 1 + (2 * cookie.cursores) + (10 * cookie.vovos)
    label_cookies.config(text=f"{cookie.quantidade} cookies")
    atualizar_botoes_upgrades()
    
def comprar_cursor():    
    if cookie.quantidade >= cookie.preco_do_cursor:
        cookie.quantidade -= cookie.preco_do_cursor
        cookie.cursores += 1
        label_cookies.config(text=f"{cookie.quantidade} cookies")
        botao_cursor.config(text=f"Cursor ({cookie.cursores})")
        # atualizar o preço do cursor para próxima compra
        cookie.preco_do_cursor += 50
    
    atualizar_botoes_upgrades()

def comprar_vovo():
    # vejo se tenho dinheiro (cookies) para comprar
    if cookie.quantidade >= cookie.preco_da_vovo:
        cookie.quantidade -= cookie.preco_da_vovo # pago pelo upgrade
        cookie.vovos += 1 # recebo o upgrade (ganho 1 vovó)

        # peço à view que mostre as mudanças para o jogador
        label_cookies.config(text = f"{cookie.quantidade} cookies")
        botao_vovo.config(text = f"Vovós ({cookie.vovos})")
        # atualizar o preço do upgrade para a próxima compra
        cookie.preco_da_vovo += 1000

    atualizar_botoes_upgrades()
#
# View (Interface Gráfica)
#

import tkinter as tk

root = tk.Tk()
root.title("Cookie Clicker")
root.geometry("400x500+1100+100")

frame_jogo = tk.Frame(root)
frame_upgrades = tk.Frame(root)

frame_jogo.pack(side='left')
frame_upgrades.pack(side='right')


label_cookies = tk.Label(frame_jogo, text="0 cookies")
img_cookie = tk.PhotoImage(file = "cookie.png")
botao_cookie = tk.Button(frame_jogo, command = ganhar_cookie, image=img_cookie, width=250, height=250, background='cyan', foreground='white')



botao_cursor = tk.Button(frame_upgrades, command = comprar_cursor, text="Cursor", width=15)
botao_vovo = tk.Button(frame_upgrades, command = comprar_vovo, text="Vovó", width=15)

botao_cursor.configure(state="disabled")
botao_vovo.configure(state="disabled")

botao_cursor.pack()
botao_vovo.pack()

label_cookies.pack()
botao_cookie.pack()


root.mainloop()
