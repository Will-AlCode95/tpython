# Configurar nome e email do usuário local do repositório

Para usarmos em nosso computador um repositório que acabamos de clonar, precisamos configurar um nome de usuário e um email que serão usados a cada *commit* e a cada vez que enviarmos ao Codeberg (computador remoto) atualizações dos arquivos modificados por nós (computador local).

1. Mude para o diretório do repositório. Supondo que você ainda esteja no diretório `repos` que criamos, digite:

``` bash
repos$ cd iprog23
```
Agora o prompt deve indicar que o diretório atual é `iprog23` (ou, o nome que você deu ao seu repositório).

2. Configure o nome do seu usuário local, usando o nome de seu usuário do Codeberg ao invés de <kbd>grz</kbd>, como está no exemplo.

``` bash
iprog23$ git config --local user.name grz
```

3. Configure o endereço de email do usuário local, substituindo o endereço de email pelo endereço de email que você usou para criar a sua conta de usuário no Codeberg.

``` bash
iprog23$ git config --local user.email grzzr@duck.com
```

Pronto. Agora já podemos começar a trabalhar.