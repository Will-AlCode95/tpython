# Clonar o repositório no seu computador de trabalho

Clonar é fazer uma cópia idêntica de um repositório salvando todos os arquivos em um outro local - normalmente em outro computador. No nosso caso, vamos copiar o repositório que acabamos de criar todinho para dentro do nosso computador de trabalho.

Clonar serve para que possamos fazer modificações nos arquivos (criar novos, alterar conteúdo de arquivos existente, apagar arquivos...) sem modificar diretamente o repositório principal, que é o que está publicado no codeberg.

Isso ajuda a organizar o trabalho (no nosso computador ficam os testes, os trabalhos pela metade, e também os trabalhos já prontos para publicar) e no servidor (o codeberg) ficam apenas os arquivos e partes do programa (ou site, ou documento...) que estão bons para serem usados.


## Clonar o repositório usando a linha de comando

Para clonar o repositório que você acabou de criar você pode usar o GIT em linha de comando (`CMD`, no Windows, `terminal` no Mac ou Linux) ou pode fazer tudo de dentro do `VisualStudio Code`.

Para clonar o repositório usando a linha de comando, começe abrindo o terminal que dá acesso à linha de comando. 

Quando clonarmos o repositório, será criado um novo diretório em nosso computador que terá o mesmo nome do repositório.

> Por isso é importante cuidar para que não exista um diretório com o mesmo nome do repositório no diretório atual quando você executar o comando de clonagem.

Suponha que estamos usando o Windows e que o diretório atual seja `C:\Users\gustavo`. O prompt de comando vai aparecer assim:comando, digite:

```
C:\Users\gustavo>
```

Para evitar que haja um diretório com o mesmo nome do nosso repositório, nós vamos: 

- criar um novo diretório
- mudar para esse diretório (entrar no diretório)
- clonar o repositório nesse diretório

> O prompt de comando nos exemplos a seguir está abreviado. Não estou usando o caminho completo nem outros sinais, apenas o sinal `$`, que é uma forma genérica de indicar que o computador está pronto para receber um comando. Você deve digitar o que vem após o sinal de prompt.


1. Crie um novo diretório chamado `repos` (abreviatura de "repositórios")


``` bash
$ mkdir repos
```

2. Entre no diretório `repos`

``` bash
$ cd repos
```

O prompt vai indicar que agora o diretório `repos` é o diretório de trabalho. Por exemplo:

``` 
repos$
```

3. Clone o repositório usando GIT. Para isso você precisa da URL de clonagem do seu repositório. Você encontra ela na página do seu repositório no Codeberg. Essa página é a página que se abriu logo após a criação do repositório.

> Caso você tenha mudado de página ou tenha fechado a janela sem querer, a URL que você precisa para o comando de clonagem é formada segundo a seguinte sintaxe:

```
https://codeberg.org/usuario/nome_repositorio.git

Onde:

usuario   - nome de seu usuário no codeberg
nome_repositorio - nome do seu repositorio

* Observe a extensão .git após o nome do repositório *
```

Por exemplo. **Este é o comando para clonar o repositório** <kbd>iprog23</kbd> do usuário <kbd>grz</kbd>.

``` bash
repos$ git clone https://codeberg.org/grz/iprog23.git
```

Após esse comando, você vai ver algumas mensagens do GIT e, por fim, o prompt de comando novamente. Como no exemplo abaixo:

``` bash
Cloning into 'iprog23'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (4/4), 862 bytes | 862.00 KiB/s, done.
repos$ _
```

Confira se a clonagem deu certo listando o diretório

No Linux/MacOS
``` bash
repos$ ls -l
```

No Windows

``` cmd
repos$ dir
```

Deve aparecer uma listagem contendo um diretório que tem o nome do seu repositório.

Esse diretório é uma cópia do repositório. Confira se os arquivos estão lá digitando

``` bash
repos$ ls -l iprog23
```

> Substitua <kbd>ls -l</kbd> por <kbd>dir</kbd> se você estiver no Windows e substitua o nome do diretório pelo nome do seu repositório.

Tudo deve estar lá e tudo deve ter dado certo. Se algo não funcionou, volte e confira os passos.

