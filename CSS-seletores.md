# CSS - Seletores

Até agora os seletores CSS que usamos permitiram que selecionássemos elementos HTML segundo seu nome fazendo com que a regra de estilagem valesse para todas as ocorrências desses elementos na página.

Os seletores do CSS podem ser mais específicos que isso.

# id e class

Os elementos HTML tem duas propriedades, chamadas <code>id</code> e <code>class</code>, que podem ser usadas em conjunto com o CSS para selecionar elementos e também agrupá-los arbitrariamente, não apenas segundo o nome do elemento.

## id

A propriedade <code>id</code> é usada usada para identificar um único elemento entre todos.

No CSS, o seletor de id inicia por <code>#</code> seguido pelo nome do id.

- HTML

``` html
<header>Título da página</header>
<article>
    <header id='nome-post'>Nome do post</header>
</article>
```

- CSS

``` css
header {
    font-size: 20px;
}

#nome-post {
    font-size: 16px;
}
```

A primeira regra do exemplo vale para todos os elementos <code>header</code>.

A segunda regra vale apenas para o elemento que tiver id="<code>nome-post</code>".

O <code>id</code> deve ser usado como um identificador único e é útil também para os scripts que escreveremos mais tarde com javascript.

## class

A propriedade <code>class</code> é usada para criar uma classe de elementos. 

Um elemento pertence a uma classe quando ele compartilha uma ou mais características definidas pela classe. 

Usamos classes para criar novos **tipos** independentemente dos elementos HTML já existentes.

O seletor do CSS que define uma classe é iniciado por <code>.</code> seguido do nome da classe.

Exemplo:

- HTML

``` html
<article class='post'>
    <header>Nome do post</header>
    <p>Texto do artigo</p>
</article>

<article class='post'>
    <header>Nome do post</header>
    <p>Texto do artigo</p>
</article>
```

- CSS

``` css
header {
    font-size: 20px;
}

.post {
    font-size: 16px;
    background-color: yellow;
    padding: 8px;
    margin: 14px;
}
```

> Também podemos selecionar elementos específicos que possuam o <code>id</code> ou <code>class</code> que quisermos.
> Para isso escrevemos na regra CSS o nome do elemento seguido do nome do <code>id</code> ou <code>class</code>.
>
>``` css 
> article.post {
>   background-color: yellow;
>}
>```
>
> seleciona apenas as tags <code>article</code> pertencentes à classe <code>post</code>.

# Aninhamento

Não é preciso criar uma classe para cada tag que está aninhada a uma tag raíz, como nos exemplos acima com <code>article</code>.

Se quisermos estilar o <code>header</code> de um elemento (nesse caso um <code>article</code>) da classe <code>post</code> não precisamos de uma class **titulo-post**, por exemplo. 

Para isso escrevemos o seletor CSS assim:

``` css
.post header {
        background-color: blue;
        color: aliceblue;
        padding: 4px;
    }
```

Assim reduzimos a quantidade de classes que precisamos usar e facilitamos a manutenção e uso do CSS que criamos.

# Estados e pseudo classes

Toda vez que trocamos o valor de uma propriedade de um elemento ele passa pelo que é chamado de uma **mudança de estado**. 

Pense na mudança de estado assim:

1. Num momento, o valor da propriedade *x* do elemento é *tal* e esse elemento **está** de um determinado jeito.
1.  Noutro momento o valor da propriedade *x* muda e agora o elemento **está** de outro jeito. 
1. O elemento passou por uma *mudança de estado**.

E agora? Se a classe é definida pelas propriedades que o elemento compartilha com outros, se uma propriedade muda então o elemento muda de classe?
Como selecionar o elemento que está em transição de estado?

Não. Não há mudança de classe. O CSS trata as transições de estado como <code>pseudo classes</code>.

Podemos selecionar pseudo-classes e estilar os elementos de acordo com esses seus estados transitórios.

Por exemplo, <code>hover</code> é o estado em que um elemento está quando **o mouse está passando por cima** dele:

``` css
.post:hover {
    background-color: aquamarine;
    transition: 0.25s;
}

.post header:hover {
    background-color: yellow;
    color: black;
}
```

