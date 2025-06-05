import tkinter as tk

# Usuário e senha secretos ;)
usuario = "prof"
senha = "abcde"

def validar_login():
    val_login = tx_login.get()
    val_senha = tx_senha.get()
   
    if val_login == usuario and val_senha == senha:
        print("Login válido")
    else:
        print("Login inválido")

janela_login = tk.Tk()

janela_login.title("Login")

lbl_login = tk.Label(janela_login, text="Login:")
lbl_senha = tk.Label(janela_login, text="Senha:")

tx_login = tk.Entry(janela_login)
tx_senha = tk.Entry(janela_login, show='*')

bt_login = tk.Button(janela_login, text="Login", command=validar_login)


lbl_login.grid(row=0, column=0)
tx_login.grid(row=0, column=1)
lbl_senha.grid(row=1, column=0)
tx_senha.grid(row=1, column=1)

bt_login.grid(row=2, column=1)

janela_login.mainloop()