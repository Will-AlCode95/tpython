# printf - imprimindo mensagens no console

Para imprimir uma mensagem no console, em BASH usamos o comando `printf`

Exemplo:

```bash
#!/usr/bin/bash

printf "Oi, oi, oi!!!"
```

O resultado deve ser

```
Oi, oi, oi!!!
```

## Formatando a saída do printf

O printf aceita imprimir caracteres especiais chamados `caracteres de controle` e também consegue incluir valores numéricos ou de texto no texto de saída final, permitindo assim a criação de saídas formatadas.

Exemplo de saída formatada

```bash
#!/bin/bash

printf "*******************\n"
printf "* Texto formatado *\n"
printf "*******************\n"
```

Nesse caso o caractere especial é o `\n` que está no final de cada linha. Ele causa uma quebra de linha, fazendo com que a próxima linha seja escrita a partir da primeira coluna da linha de baixo.

> Caracteres de controle
> - `\n` - Nova linha
> - `\t` - Tabulação horizontal
> - `\a` - Alerta (um sinal sonoro)

Para inserir uma string no meio do texto que o printf vai imprimir:

1. marcamos o lugar onde a inserção vai ocorrer usando a sequência `%s`
2. passamos o valor a ser inserido como parâmetro para o printf

Exemplo

```bash
#!/bin/bash
printf "* %s *\n" Oi!!!
```

Podemos passar vários valores como parâmetro. Para isso separamos eles com um espaço.

E para usar cada um deles no texto, usamos um `%s` para cada valor

Exemplo:

```bash
#!/bin/bash
printf "* %s, %s! *\n" Oi Gustavo 
```
O resultado deve ser:

```sh 
* Oi, Gustavo *
```
