# Título do site

Já temos uma parte da nossa página principal dedicada ao cabeçalho. É parte onde acabamos de colocar o menu do site. O título do site pode ir junto, no mesmo cabeçalho. 

``` html
<header>            
    <nav>      
        <ul>
            <li><a href="index.html">blog</a></li>
            <li><a href="about.html">sobre</a></li>
        </ul>
    </nav>

    <h1>Blog23</h1>

</header>
```

Note que assim o que estamos dizendo é que o título do site faz parte, conceitualmente, do cabeçalho da página. Poderíamos pensar de outra forma e criar, por exemplo, uma seção só para o título. Não estaria errado. É tudo uma questão de como entendemos o título: ele é uma propriedade do cabeçalho ou ele é um elemento à parte? 

Quando fizermos o CSS para o site, vamos explorar ainda a possibilidade de usar imagens no lugar do título, como um logotipo do site ou imagem de capa.

# Rodapé do site

Para fazer o rodapé vamos retrabalhar o elemento <code>\<footer\></code> que até agora ficou vazio. 

Localize o <code>footer</code> no HTML da página principal. Ele ficou logo abaixo de <code>\<\main\></code>.

Modifique o código para:

``` html
<footer>
    blog23 - <a href="LICENSE">licença</a>
</footer>

```
