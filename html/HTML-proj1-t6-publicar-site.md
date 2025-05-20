# Pulicar o site na internet

Para que o site possa ser acessado de qualquer lugar na internet, ele precisa estar em um servidor web que esteja na internet e que (diferente de nosso computador) também esteja acessível por qualquer outro computador.

O processo de colocar um site em um servidor web de acesso público na internet é chamado de **publicação**.

A forma mais prática que temos de publicar nosso site é usando um recurso do próprio Codeberg para a publicação de sites, chamado <code>Codeberg Pages</code>.

## Codeberg pages

Qualquer repositório do Codeberg pode ter um website só seu. Para isso, precisamos:

1. criar um novo ramo chamado <code>pages</code> em nosso repositório
1. colocar nesse ramo os arquivos do nosso site
1. publicar o ramo pages

Quando terminarmos de publicar nosso site no Codeberg Pages, ele fica acessível através do URL que tem o seguinte formato:

[https://seu_usuario.codeberg.page/nome_repositorio](https://seu_usuario.codeberg.page/nome_repositorio)

Por exemplo, se seu usuário é **aluno23** e o repositório é **blog23**, o URL fica:

[https://aluno23.codeberg.page/blog23](https://aluno23.codeberg.page/blog23)

> O Codeberg Pages hospeda apenas sites estáticos. Isso significa que nenhum código executável (como Python, PHP, etc...) vai funcionar se você colocar ele no seu <code>pages</code>. Esses arquivos serão tratados como simples arquivos de texto.

Existem varias formas de publicar um site na internet. Futuramente vamos aprender mais algumas delas. 

## Passo 1: Criar um ramo <code>pages</code>

O ramo <code>pages</code> tem um significado especial para o Codeberg, que é o de ser a <code>raíz do site publicado</code> por ele.

> Para criar um novo ramo siga as instruções [neste link](GIT-criar-ramo.md).


Essa funcionalidade do <code>pages</code> que estamos usando é mais uma exceção do que uma regra. Na maioria das vezes criamos ramos para auxiliar o controle de versões dos nossos projetos.

## Passo 2: Publicar o site

Para publicar o site basta publicar o ramo <code>pages</code>.

> Siga os [passos neste link](GIT-publicar-ramo.md) para publicar um ramo.

## Passo 3: Acessar o site

Quando terminarmos de publicar nosso site no Codeberg Pages, ele fica acessível através do URL que tem o seguinte formato:

[https://seu_usuario.codeberg.page/nome_repositorio](https://seu_usuario.codeberg.page/nome_repositorio)

Por exemplo, se seu usuário é **aluno23** e o repositório é **blog23**, o URL fica:

[https://aluno23.codeberg.page/blog23](https://aluno23.codeberg.page/blog23)