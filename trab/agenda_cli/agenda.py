import sys
import shelve
# abrimos os dados serializados
agenda = shelve.open('agenda.dat')


def sobre():
    print("agenda.py 2025 (cli) versão 0.1.0")    
    print("------------------------------")
    print("autor: Prof. Gustavo")
    print("SENAC Tech - Porto Alegre, RS")

def ajuda():
    print('''
Comandos:
---------
consultar <chave>
    Ex. C:\\> python agenda.py consultar sry@email.com

cadastrar <chave> <nome> <idade> <endereco> <favorito>
    Ex. C:\\> python agenda.py cadastrar pessoay@email.com "Sr. Y" 34 "Rua Xis, 80"

excluir <chave>
    Ex. C:\\> python agenda.py excluir sry@email.com

atualizar <chave> <nome> <idade> <endereco> <favorito>
    Ex. C:\\> python agenda.py atualizar pessoay@email.com "Senhor Ipsilon" 34 "Rua Xis, 80"
''')

# definição das funções do sistama

def adicionar(email, dados): # dados é uma list    
    global agenda
    agenda[email] = dados

def consultar(email):
    global agenda
    return agenda[email]

def excluir(email):
    global agenda
    try:
        del agenda[email]
    except KeyError:
        return False
    
    return True

def atualizar(email, dados): # dados é uma list com os novos valores do registro
    global agenda
    agenda[email] = dados

def listar_todos():
    for email, dados in agenda.items():
        print(email, dados)

def listar_por_email(email):
    dados = consultar(email)
    print(dados)

# Tratamento de comandos

if len(sys.argv) > 1: # se recebemos pelo menos 1 parâmetro...
    comando = sys.argv[1]

    if comando == 'sobre':
        sobre()
    
    elif comando == 'ajuda':
        ajuda()

    elif comando == 'consultar':
        try:
            email = sys.argv[2]            
            listar_por_email(email)
        except:
            listar_todos()
    
    elif comando == 'excluir':
        try:
            email = sys.argv[2] # tenta acessar o parâmetro email
            sucesso = excluir(email)
            if sucesso:
                print("Registro excluído")
            else:
                print("Registro inexistente")
        except: # caso não tenha sido informado email...
            print('Você precisa informar um email')
        
    elif comando == 'cadastrar':
        email = input('email: ')
        nome = input('nome: ')
        idade = int(input('idade: '))
        telefone = input('telefone: ')
        favorito = False
        adicionar(email, [nome, idade, telefone, favorito])
        listar_todos()
    else:
        print("Comando não reconhecido")

else: # se não recebemos parâmetros...
    ajuda()

# Antes de terminar o programa
# salvamos os dados no arquivo agenda.dat

agenda.close()