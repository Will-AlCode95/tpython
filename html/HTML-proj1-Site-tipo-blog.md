# Um site tipo blog

Este é um roteiro para fazermos um site do tipo blog. Isso vai nos ajudar a trabalhar as tags HTML que já vimos e a conhecer novas.

Vamos começar pela estrutura do site, que envolve HTML, e deixar o design e a apresentação, que envolvem CSS, para depois.

Usaremos o [codeberg](https://codeberg.org) para armazenar, controlar e publicar este projeto.

O projeto vai ter seu próprio repositório GIT e será publicado como uma <code>codeberg page</code>.

# Estrutura e padrões do site

1. Todas as páginas contém
- cabeçalho com título
- menu de navegação
- rodapé com link para licença de uso do conteúdo publicado

2. Página principal

- listagem dos artigos/posts, sendo que cada ítem contém:
    - título
    - data
    - imagem de capa ou ícone que ilustre o conteúdo do artigo
    - resumo do artigo    
    - link para página com o texto completo do artigo

3. Cada página contendo o texto completo do artigo
- título do artigo
- data de publicação do artigo
- imagem de capa que ilustra o conteúdo do artigo
- texto completo do artigo
- link para retornar à página principal do site

4. Página "sobre"
- texto explicando quais assuntos são tratados no site/blog e quem está escrevendo os artigos


## Nomes dos arquivos e diretórios

Vamos padronizar o nomes dos arquivos e diretórios que usaremos. Isso tem o objetivo de facilitar o armazenamento e a consulta dos dados.

Por exemplo, com isso vamos evitar duplicatas e caracteres não permitidos em nomes de arquivos. Também evitaremos o problema de ter aquivos de um mesmo tipo sendo gravados hora em um diretório, hora em outro... que é um anti-padrão que dificulta a consulta a esses arquivos, porque não temos um lugar certo, bem definido, onde ir para encontrá-los quando precisamos.

Usar um padrão para nomear os arquivos e diretórios é bom também para facilitar o desenvolvimento de programas que criam e usam esses arquivos. Não vamos fazer isso agora, mas é bom pensar nesses problemas antes mesmo de escrever um programa porque assim teremos mais chances de reaproveitar o trabalho de agora em projetos futuros, que envolvam programação.

## Estrutura de diretórios

```
/               - Diretório raíz do site
|               
+--- posts      - páginas com texto completo dos artigos
|
+--- img        - imagens usadas no site
```

## Página principal 

> Este arquivo deve ser salvo no diretório <KBD>raíz</KBD> do site.

O nome do arquivo que contém a página principal deve ser <code>index.html</code> por padrão. Não é uma escolha nossa mas de quem configurou o servidor web que usamos.

É possível usar outros nomes, alterando as configurações do servidor web, mas <code>index.html</code> é o nome mais comumente usado e por isso vamos adotá-lo neste projeto.

## Página de artigo

> Estes arquivos devem ser salvos no diretório <KBD>posts</KBD> do site.

Cada artigo deve ter uma página só para si, salva em um arquivo HTML também só seu. O nome de cada um desses arquivos HTML deve seguir a seginte sintaxe:

```
Sintaxe

<aaaammdd>-<titulo-do-artigo>.html

    onde:

    aaaa    - ano
    mm      - mês
    dd      - dia

    titulo-do-artigo    Título em minúsculas e
                        sem caracteres especiais,
                        como espaços e acentos

Exemplos

    Um artigo publicado dia 15/03/2023 chamado "Projeto do blog" deve ser salvo no diretório posts no arquivo:

    20230315-projeto-do-blog.html

    Um artigo publicado no mesmo dia, mas chamado "Começando o blog" deve ser salvo no diretório posts no arquivo:

    20230315-comecando-o-blog.html

```

## Página sobre

> Este arquivo deve ser salvo no diretório <code>raíz</code> do site.


O arquivo da página sobre deve se chamar <code>about.html</code>. "About" significa "sobre", em inglês.

## Tarefa: Criar a estrutura de diretórios do site

Vamos para a linha de comando para criar a estrutura de diretórios do site.

 
```
/    <---- raíz do site
|
+--- posts    <---- diretório dos artigos
|
+--- img      <---- diretório das imagens
```

A estrutura de diretórios começa pelo <code>diretório raíz</code> do site. É lá que vamos colocar os arquivos <code>index.htmn</code> e <code>about.html</code>. 

O diretório do repositório será o diretório raíz do nosso site. Portanto, o diretório raíz já está pronto após clonarmos ele do repositório remoto.

A tarefa é, então, criar mais dois diretórios dentro do diretório raíz.

- posts
- img

## Passos para criar os diretórios

1. Mude para o diretório raíz do site (o diretório do seu repositório **local**). Supondo que você esteja no diretório <code>repos</code> que criamos [anteriormente](GIT-clonar-repositorio.md), o comando para mudar para o seu repositório é:

``` bash
repos$ cd blog23

Onde: "blog23" é o nome seu repositório
```

2. Agora que você está na raíz do seu repositório, crie os dois diretórios que faltam.

``` bash
blog23$ mkdir posts

blog23$ mkdir img
```

3. Confira a listagem do diretório para ver os novos diretórios lá

``` bash
blog23$ ls -l
```

Tudo lá? Vamos adiante. Se algo estiver faltando, volte e revise os passos.