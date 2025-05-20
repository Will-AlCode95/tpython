# Fazer a listagem dos posts na página principal

Este é outro dos requisitos do site. A página principal deve ter uma listagem com todos os artigos que foram publicados.


- listagem dos artigos/posts, sendo que cada ítem contém:
    - título
    - data
    - imagem de capa ou ícone que ilustre o conteúdo do artigo
    - resumo do artigo    
    - link para página com o texto completo do artigo

## Passo 1. Preparar a estrutura da página principal para conter a lista de artigos.

A página principal, por enquanto, está vazia. Repare no corpo da página (elementos <code>body</code>) que não tem conteúdo.


``` html
<!DOCTYPE html>

<html>

    <head>
        <meta charset="UTF-8">
        <title>Título do site ou nome da página</title>    
    </head>

    <body>
        
    </body>
</html>
```

Vamos dividir o corpo da página em três partes:

- cabeçalho
- principal (onde está o conteúdo principal da página)
- rodapé

O HTML 5 tem três elementos para indicar essas partes

- <code>header</code> - cabeçalho
- <code>main</code> - principal
- <code>footer</code> - rodapé

O código fica assim:


``` html
<!DOCTYPE html>
<html>

    <head>
        <meta charset="UTF-8">
        <title>Coloque aqui o título do seu site</title>    
    </head>

    <body>
        
        <header>
        </header>

        <main>
        </main>

        <footer>
        </footer>

    </body>
</html>
```

Vamos deixar <code>header</code> e <code>footer</code> para depois. 

## Passo 2. Criar uma seção contendo a lista de artigos

<code>main</code> pode conter várias seções. Por enquanto, teremos apenas uma seção, com a lista dos artigos. Porém, futuramente, podemos pensar em acrescentar seções do tipo "assine nossa newsletter" ou "capa do site"...

Pensando no que podemos vir a acrescentar na página principal no futuro, vamos desde já organizar o conteúdo nessas seções, para não ter mais trabalho depois.

Para não poluir os exemplos com código demais, abaixo está apenas a parte do código que estamos modificando. O elemento <code>main</code> agora fica assim:

``` html
<main>
    <section>
        <header>
            <h2>Lista de artigos</h2>
        </header>
        
        <article>
            <header>
                <h3>Primeiro post</h3>
                <time datetime="2023-03-14 19:00">
                    14 de março de 2023
                </time>
            </header>                        
        </article>

    </section>
</main>
```

Acrescentamos:

- <code>section</code> - indica uma seção da página
- <code>article</code> - indica que o que está entre as tags é um artigo

Note que tanto <code>section</code> quanto <code>article</code> podem ter um <code>header</code>.

Para diferenciar o <code>header</code> da seção do <code>header</code> do artigo estamos usando uma cabeçalho de nível 2 (<code>h2</code>) para a seção e um de nível 3 (<code>h3</code>) para o artigo.

Note também que o artigo não é o artigo completo. Não temos aqui os parágrafos com o conteúdo do artigo, como fizemos antes. Isso é porque queremos fazer apenas uma listagem com os nomes deles e um resumo. 

## Passo 3. Fazer um resumo para o artigo 

Para fazer o resumo, podemos também usar um elemento <code>p</code>, mas o HTML 5 tem um outro elemento mais interessante para esse caso, que é o elemento <code>summary</code> usado com um outro elemento chamado <code>details</code>

Resumo do artigo vai usar os elementos:

- <code>details</code> - indica que o conteúdo traz mais detalhes sobre alguma informação já presente no documento (no nosso caso, mais detalhes sobre o título do artigo)
- <code>summary</code> - é um cabeçalho que resume o que está nos detalhes

O artigo com o resumo fica assim:

``` html
<article>
    <header>
        <h3>Primeiro post</h3>
        <time datetime="2023-03-14 19:00">
            14 de março de 2023
        </time>
        <details>
            <summary>veja um resumo...</summary>
            <p>
                Este é o super conteúdo do primeiro post
                do blog. 
            </p>
        </details>
    </header>                        
</article>
```


## Passo 4. Colocar um link para a página do artigo

Agora vamos usar a página html com o artigo completo, que fizemos anteriormente. Vamos incluir um link para ela na listagem dos artigos que estamos fazendo.

Podemos inserir esse link de várias formas. Ele pode ser um link que usa o próprio título do post como link, ou pode ser um texto separado, como "vá para o artigo". Vamos fazer um texto separado.

Após o <code>header</code> do elemento <code>article</code>, vamos colocar um parágrafo contendo o link.

O código do <code>article</code> vai ficar assim:

``` html
<article>
    <header>
        <h3>Primeiro post</h3>
        <time datetime="2023-03-14 19:00">
            14 de março de 2023
        </time>
        <details>
            <summary>veja um resumo...</summary>
            <p>
                Este é o super conteúdo do primeiro post
                do blog. 
            </p>
        </details>                        
    </header>
    <p>
        <a href="posts/20230314-primeiro-post.html">vá para o artigo</a>
    </p>
</article>
```

## Passo 5. Colocar um ícone ou imagem ilustrando conteúdo do artigo

Para fazer essa imagem que vai ilustrar o conteúdo do artigo, vamos usar a tag <code>\<img\></code> (que mostra a imagem) e a tag <code>\<aside\></code> que indica um conteúdo que está 'à parte' do conteúdo principal, ou seja, ele pode ser uma complementação do conteúdo, um comentário, uma observação... ou, como é o nosso caso, uma ilustração do conteúdo. 

Como essa imagem é um "acessório", não faz parte do conteúdo do artigo em si, não vamos colocá-la nem no <code>header</code> nem no <code>details</code>.

Para que a imagem apareca no início do <code>article</code> vamos colocá-la logo abaixo do elemento <code>\<article\></code>.

O código vai ficar assim:

``` html
<article>
    <aside>                        
        <img src="../img/icone-estrela.png" />                        
    </aside>                    
    <header>                        
        <h3>Primeiro post</h3>                        
        <time datetime="2023-03-14 19:00">
            14 de março de 2023
        </time>                        
        <details>
            <summary>veja um resumo...</summary>
            <p>
                Este é o super conteúdo do primeiro post
                do blog. 
            </p>
        </details>                        
    </header>
    <p>
        <a href="posts/20230314-primeiro-post.html">vá para o artigo</a>
    </p>
</article>
```

> Você pode baixar a imagem da estrela no link
>
> [ícone-estrela.png](/img/icone-estrela.png)

# Tarefa 8: Menu do site

O elemento <code>nav</code> do HTML 5 é usado para indicar que o conteúdo dele refere-se à navegação da página. Menus são uma forma de navegar pela página. Por isso vamos usar a tag <code>\<nav\></code> para fazer o menu do nosso site.

Para isso vamos voltar a trabalhar no elemento <code>header</code>, que está logo abaixo de <code>body</code> na página principal.

Essa tag <code>\<header\></code> está definindo o cabeçalho da página. Vamos dizer que nesse cabeçalho existe um menu. A forma de dizer isso é colocando a tag <code>\<nav\></code> dentro da tag <code>\<header\></code>. Observe o código abaixo:

``` html
<header>            
    <nav>      

    </nav>
</header>
```

Dentro da tag <code>\<nav\></code> vamos colocar os ítens de navegação. Por enquanto, eles serão uma simples *lista não ordenada* (<code>\<ul\></code>) contendo dois ítens: blog e sobre.

O código fica assim:

``` html
<header>            
    <nav>      
        <ul>
            <li>blog</li>
            <li>sobre</li>
        </ul>
    </nav>
</header>
```

Para que possamos clicar nesses ítens e eles nos levarem às páginas do blog e sobre, respectivamente, vamos transformar esses ítens em links (<code>\<a\></code>).

``` html
<header>            
    <nav>      
        <ul>
            <li><a href="index.html">blog</a></li>
            <li><a href="about.html">sobre</a></li>
        </ul>
    </nav>
</header>
```

É isso. Por enquanto o menu não tem uma aparência de menu, como costumamos ver. Isso faremos depois, com CSS. 

As próximas duas tarefas são curtas e com elas terminamos o conteúdo mínimo do site que precisamos ter para avançar para a estilagem do site com CSS.
