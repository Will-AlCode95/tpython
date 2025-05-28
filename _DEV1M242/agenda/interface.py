import sys
import random
#model
numero_secreto = random.randrange(0,10)

#view
def mostrar_numero(numero):
    print(f'Numero é: {numero}')

def listar():
    print("listando registros...")

def ajuda():
    print("Este é o programa interface.py\nComandos: listar, ajuda, nsecreto")

# CTRL (roteador de comandos)
try:
    comando = sys.argv[1] # CTRL recebe da VIEW o comando do USUÁRIO
except IndexError:
    ajuda()
    sys.exit(0) # sai do programa, voltado ao Sist. Operacional informando
                # código de status 0 (Programa terminou Ok, sem erros)

if comando == 'listar':
    listar()
elif comando == 'nsecreto':
    mostrar_numero(numero_secreto) #ctrl pede à view p/ mostrar numero
elif comando == 'ajuda':
    ajuda()