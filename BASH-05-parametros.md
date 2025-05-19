# Passando parâmetros para um script BASH


Podemos passar parâmetros em linha de comando para um script BASH. Para isso, no corpo do código do script escrevemos `$1`, `$2`, `$3`, etc... no lugar onde queremos que o valor do parâmetro seja inserido.

Por exemplo, para usar o valor do parâmetro que está sendo passado em linha de comando para o script abaixo (o valor é 'Gustavo'), usamos `$1` no nosso script:

```bash
$dizOiPara Gustavo
```
E no script escrevemos assim:

```bash
#!/bin/bash

printf "Oi, $1!!\n"
```

O resultado deve ser:

```
Oi, Gustavo!!
```

## Variáveis e múltiplos parâmetros

O melhor é que agora o script funciona para qualquer palavra que passarmos como parâmetro.

```bash
$dizOiPara Luana

Oi, Luana!!
```
Note, portanto, que `$1` é uma variável no código do script!

E podemos usar mais de uma dessas variáveis para podermos receber mais de um parâmetro em linha de comando

Por Exemplo, considere um script que recebe um nome, uma idade e um email em linha de comando e imprime como resposta um texto formatado:

```bash
$ficha Gustavo 45 gustavo@prof.pro

nome: Gustavo
idade: 45
email: gustavo@prof.pro
```

Ele seria escrito assim:

```bash
#!/bin/bash
printf "nome: $1\n"
printf "idade: $2\n"
printf "email: $3\n"
```
