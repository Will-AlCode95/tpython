# HTML Semântico

Você notou que praticamente todas as tags que usamos durante o projeto 1 quase não tem efeito visual sobre o documento.

O objetivo dessas tags foi apenas o de dar **significado** ao conteúdo do documento (ao texto).

Por isso são chamadas **tags semânticas** ou **HTML semântico**

> semântico = relativo ao significado das coisas

Este é um resumo das novas tags semânticas que vimos durante o projeto 1.

Semânticas

<code>header</code> - Significa que o seu conteúdo é um cabeçalho - pode ser da página, de um artigo, de uma seção...

``` html
<header>
    Título de alguma coisa
</header>
```
<code>main</code> - Indica que seu conteúdo é a parte principal da página, de um artigo, seção...

<code>footer</code> - Significa rodapé - da página, artigo...

<code>article</code> - Um artigo pode ser um post de blog, um tweet, uma mensagem em chat...

``` html
<article>
    <header>Primeiro Post</header>
    <main>
        <p>Texto do primeiro post.</p>
        <p>Nada muito interessante. Só estes dois parágrafos...</p>
    </main>
</article>
```

<code>time</code> - contém uma data, hora ou ambas. O formato é livre, mas podemos usar a propriedade **datetime** para guardar um valor de data/hora formal, para usarmos em scripts, por exemplo.

``` html
<time datetime="2023-06-20 19:00">
 20 de junho de 2023
</time>
```

<code>details</code> e <code>summary</code>

<code>aside</code> - um texto/imagem de comentário, um aparte. Costuma ser estilado para aparecer 'flutuando' ao lado conteúdo principal (ex. infográficos)

<code>figure</code> e <code>figcaption</code> - dentro de **figure** vai estar uma imagem (tag **img**) e **figcaption** contém a legenda (caption) da imagem.

<code>nav</code> - dentro de **nav** estão os elementos responsáveis pela navegação da página/site - normalmente links.

## Mais tags HTML

<code>kbd</code> - uma tecla ou uma entrada de dados via teclado (kbd = keyboard)

<code>code</code> - um trecho de código - mas diferente de **pre** pois não é preformatado.