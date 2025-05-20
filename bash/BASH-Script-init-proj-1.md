# Escrever um script de inicialização de projeto

Aproveitar o que vimos sobre o uso de parâmetros em linha de comando para scripts BASH, vamos fazer um script para criar um ambiente de trabalho para nós. Um primeiro script útil!

O script abaixo cria um diretório com o nome que passarmos para o Script em linha de comando:

```bash
#!/bin/bash

printf "Criando projeto em $1...\n\n"
mkdir $1
```

Salve ele como: `cproj` e dê permissão de execução ao arquivo.

Para usá-lo, digite, por exemplo:

```bash
$ ./cproj aula05
```

O resultado deve ser:

```
Criando projeto em aula05...
```

Esse script é só um pouquinho melhor que usar o comando `mkdir` para criar o diretório.

Vamos melhorá-lo:

```bash
#!/bin/bash

printf "Criando projeto em $1...\n\n"
mkdir $1
mkdir $1/versoes
mkdir $1/docs

printf "Pronto\n"
```

Agora ele já ficou mais útil, porque nos poupou a digitação de pelo menos duas linhas de comando - além dos erros que poderíamos cometer a cada vez que digitássemos os comandos.


## Exercício

Por fim, podemos colocar alguns arquivos vazios nesses diretórios, já que teríamos que criá-los depois de qualquer forma.


Altere o script para que ele crie:

- um arquivo chamado `README.md` no diretório raíz do projeto
- um arquivo chamado `index.html` no diretório `docs` do projeto

