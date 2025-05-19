# CSS

## Aplicar CSS - Externo

Considere um arquivo CSS como este:

``` css

p {
    color: red;
}

a {
    color: blue;
}

```

Considere também que ele está gravado em um arquivo chamado <code>estilo.css</code> que está no mesmo diretório do arquivo html onde você quer aplicá-lo.

Para aplicar o CSS o código ficaria assim:

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de CSS Externo</title>
    <link rel="stylesheet" href="estilo.css">
</head>
</html>
```

> Podemos também linkar um arquivo CSS que está em outro servidor usando o URL completo para ele.
>
> ## Experimente!
>
> 1. Visite o site [simplecss.org](https://simplecss.org) e veja o estilo da página.
>
> Ele está definido no arquivo que está no link abaixo:
> 
> [https://cdn.simplecss.org/simple.css](https://cdn.simplecss.org/simple.css)
>
> 2. Use esse estilo no projeto do Blog que começamos a fazer.
> 
> Para isso, coloque a linha abaixo no <code>head</code> do arquivo <code>index.html</code>.
> ```
> <link rel="stylesheet" href="https://cdn.simplecss.org/simple.css">
> ```
> 3. Repare no resultado...


## Interno

O código CSS também pode ficar no mesmo arquivo HTML que aplica ele.

Aplicamos os CSS interno ao arquivo HTML colocando o código CSS entre tags <code>style</code> no <code>head</code> do arquivo.

O exemplo acima ficaria assim:

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de CSS Interno</title>
    <style>
    p {
       color: red;
    }

    a {
       color: blue;
    }   
    </style>
</head>
  <p>
    Um parágrafo com texto em vermelho.
    <a href=".">e um link azul</a>
  </p>

</html>
```

## Inline

O código CSS também pode ser aplicado diretamente a um elemento do HTML.

Para aplicar o CSS inline usamos a propriedade <code>style</code> da tag e o código CSS como valor dela.

O exemplo acima ficaria assim:

``` html
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo de CSS Inline</title>
</head>
  <p style="color: red">
    Um parágrafo com texto em vermelho.
    <a href="." style="color: blue">e um link azul</a>
  </p>

</html>
```


## Seletores, propriedades e valores

Seletores são expressões usadas para selecionar elementos da árvore do documento HTML que receberão um estilo.

Uma expressão de seleção simples é o próprio nome de uma tag, que pode ser usado para selecionar um tipo de tag para receber um estilo.

Por exemplo, o <code>p</code> no código abaixo seleciona todos os elementos <code>p</code> do documento.

``` css
p {
    color: blue;
    font-size: 20px;
}
```

Entre as chaves (<code>{ }</code>) estão as propriedades do elemento que serão afetadas.

Cada linha segue a forma:
```
chave: valor;
```

Nesse exemplo, o texto de todos os parágrafos do documento apareceriam na cor azul e com tamanho 20 pixels.

Note que não usamos <code>=</code> como sinal de atribuição e que cada linha é terminada por um ponto e vírgula (<code>;</code>).

## Unidades

No último exemplo usamos uma unidade de medida na propriedade que expressou seu valor em pixels. 

Existem várias outras unidades de medida que podemos usar com CSS mas as mais usadas são:

- px (font-size: 20px) - pixels
- em (font-size: 2em) - tamanho é calculado com base no tamanho atual da fonte - nesse caso 2x o tamanho atual da fonte em uso.
- % para percentuais

## Cores

### Predefinidas

São várias! Por exemplo:

aqua, black, blue, fuchsia, gray, green, lime, maroon, navy, olive, purple, red, silver, teal, white,yellow...

### RGB

É a cor expressa em suas componentes primárias - Vermelho, Verde e Azul.

Cada componente pode ser expressa em decimal, hexadecimal ou porcentagem.

- Decimal - valor vai de 0-255, sendo 0 a menor intensidade da cor e 255 a maior intensidade.
- Porcentagem - valor vai de 0% a 100% da cor

Exemplos em decimal:

```
vermelho máximo: 255, 0 , 0
verde máximo: 0, 255, 0
azul máximo: 0, 0, 255

vermelho médio: 128, 0, 0
cinza médio: 128, 128, 128

preto: 0, 0, 0
branco: 255, 255, 255

amarelo: 255, 255, 0
magenta: 255, 0, 255
ciano: 0, 255, 255
```
Para usar a cor em RGB no CSS usamos uma função do CSS chamada <code>rgb()</code>

Exemplo:

``` css
p {
    color: rgb(255,0,0);
    background-color: rgb(0%,0%,50%);
}
```

O CSS acima estila os parágrafos com cor de texto vermelho e cor de fundo azul médio.

## Texto

- font-family:
- font-size:
- font-weight:
- font-style: italic, normal
- text-decoration: underline, overline, line-through
- text-transform: capitalize, uppercase, lowercase, none 
- text-align: left, right, center, justify

# Margens e preenchimento

Margens
- margin-top
- margin-right
- margin-bottom
- margin-left

Preenchimento

- padding-top
- padding-right
- padding-bottom
- padding-left

## Modelo de caixa

```
margin - > border -> padding -> element
```

# Bordas

- border-style: solid, dotted, dashed, double, groove, ridge, inset, outset
- border-width: - valor expresso em pixels (px)
- border-top-width, border-right-width, border-bottom-width, border-left-width
- border-color: - seguido de uma cor 

