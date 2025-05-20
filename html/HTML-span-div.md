# Aula 1

## HTML5

## Tags span e div

<code> \<span\> </code> - marca um bloco de texto/dados. A apresentação desses dados pelo browser é **em linha** com outros elementos ao seu redor.

<code> \<div\> </code> - marca um bloco de texto/dados também. A diferença é que o browser apresenta esses dados formatados **em bloco** (com quebra de linha).

Exemplos:

``` html
Oi, oi, oi! Meu nome é <span>Gustavo</span>.
```

O resultado é:

> <code>Oi, oi, oi! Meu nome é <span>Gustavo</span>. Prazer!</code>

Nenhum efeito visível. A string 'Gustavo' foi destacada no código das demais e só.

``` html
Oi, oi, oi! Meu nome é <div>Gustavo</div>. Prazer!
```

O resultado é:

<code>Oi, oi, oi! Meu nome é <div>Gustavo<div>Prazer!.
</code>

A string 'Gustavo' foi exibida dentro de um 'bloco', separado do seu entorno por espaço em branco, resultando em uma quebra linha, acima e abaixo do seu conteúdo.

## Algumas tags que se comportam como \<div\>

- As tags <code> \<h1\>, \<h2\> ... \<h6\></code> - Marcam cabeçalho que vão de nível 1 a 6. O tamanho da fonte muda e o conteúdo é exibido em bloco.

Exemplo:

``` html
<h2>Apresentação!</h2>
Oi, oi, oi!!!
```

Resultado:

> <h2>Apresentação!</h2>
> Oi, oi, oi!!!
<br/>


- A tag <code>\<p\></code> - marca um parágrafo de texto. O tamanho da fonte permanece o mesmo e o conteúdo é exibido em bloco.

Exemplo:

``` html
<h2>Apresentação</h2>
<p>Oi, oi, oi!!</p>
<p>Meu nome é Gustavo. Prazer!</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
</p>
<p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>
```

Resultado:
> <h2>Apresentação</h2>
> <p>Oi, oi, oi!!</p>
> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
></p>
><p>Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</p>

Note os espaços entre os parágrafos.

## Algumas tags que se comportam como \<span\>

- <code>\<strong\></code> - Usada para negritar um trecho de texto.
- <code>\<em\></code> - Usada para italicizar um trecho de texto.
- <code>\<u\></code> - Usada para sublinhar um trecho de texto.

Exemplo:

``` html
<p>Texto, texto <strong>em negrito</strong></p>
<p>Texto, texto <em>em itálico</em></p>
<p>Texto, texto <u>sublinhado</u></p>
```

Resultado:

> <p>Texto, texto <strong>em negrito</strong></p>
> <p>Texto, texto <em>em itálico</em></p>
> <p>Texto, texto <u>sublinhado</u></p>


