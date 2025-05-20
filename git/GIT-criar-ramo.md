# Criar um ramo de desenvolvimento (branching)

Com o GIT podemos controlar não apenas as versões dos arquivos do nosso projeto que estão no diretório de trabalho principal mas também criar versões alternativas para nosso projeto, que são novas linhas de desenvolvimento, muitas vezes usadas para experimentar ideias ou iniciar um novo projeto a partir do que já temos, sem para isso criar um novo diretório ou repositório. 

Um <code>ramo</code> é uma espécie de "diretório virtual" com arquivos de nosso projeto e é como chamamos uma "linha de desenvolvimento" do projeto. Os arquivos que estão em ramo fazem parte da linha de desenvolvimento desse ramo.

Existe sempre a linha principal (por padrão, chamada de "main", que significa "principal") e outras possíveis linhas, cada uma com o nome que quisermos dar a elas.

O processo de criar um novo ramo em um repositório GIT é chamado de <code>branching</code>, que significa <code>ramificação</code>.

No VSCodium, o ramo de desenvolvimento atual aparece no canto inferior esquerdo da janela. Agora, o nome dele é <code>main</code>.

Para criar um novo ramo (observe as imagens abaixo):

1. clique em <code>main</code> (canto inferior esquerdo da janela, onde está o mouse)
2. No menu que se abriu no topo da janela, ao centro, escolha a opção <code>Create new branch...</code> (Criar novo ramo).

<figure>
<img src="../img/vscodium/vscodium-create-branch.png" />
<figcaption style = "text-align: center">Criar um novo ramo</figcaption>
</figure>

<figure>
<img src="../img/vscodium/vscodium-create-new-branch-pages.png" />
<figcaption style = "text-align: center">Dar um nome ao novo ramo - este vai se chamar <code>pages</code></figcaption>
</figure>

3. Observe no canto inferior esquerdo da janela que o ramo de desenvolvimento atual agora é <code>pages</code> e que todos os arquivos que estavam em <code>main</code> estão também neste novo ramo.

Parece que não mudou muita coisa, só que sim. A partir de agora, podemos fazer mudanças nos arquivos que estiverem em <code>pages</code> sem afetar os arquivos que estão no ramo <code>main</code>! Inclusive, podemos ter arquivos em um ramo que não existem no outro. 


## Atualizar e publicar ramo

Agora precisamos atualizar o repositório no Codeberg, pois as mudanças que fizemos ainda estão apenas em nosso computador.

Siga as instruções para [Publicar ramo](GIT-publicar-ramo.md).