# Roteiro para uso do Git e GitHub

## Setup inicial

1. Criar uma conta no [GitHub](https://github.com/). O que é GitHub?

2. Instalar o git no seu computador seguindo os passos disponíveis nesta página: [https://git-scm.com/downloads](https://git-scm.com/downloads). O que é Git? 

## Criando o primeiro projeto

1. Criar um repositório na sua conta no GitHub em [https://github.com/new](https://github.com/new). Você vai dar um nome para o seu projeto e clicar em *Create repository*. Depois disso uma tela irá aparecer te mostrando algumas opções para o setup do seu projeto. Você pode, por exemplo, criar um novo repositório a partir de arquivos existentes na sua máquina: 

````bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fbarth/roteiro_git.git
git push -u origin main
````

Neste momento, você vai ver que todos os seus arquivos que estão no diretório local agora então na URL informada acima. Basta dar um refresh na URL acima. 

2. Você também pode adicionar novos arquivos ao seu projeto na sua máquina local e ver o status dos arquivos modificados:

````bash
git status
````

3. Você pode adicionar estas modificações em uma *staging area*, dizendo para o git que no próximo *commit* ele deverá considerar tais mudanças:

````bash
git add .
````

4. Você pode fazer o *commit* e *push* para o repositório remoto: 

````bash
git commit -m "estrutura inicial"
git push 
````

Podemos fazer estas etapas de *add*, *commit* e *push* inúmeras vezes. O GitHub irá manter todas as versões dos arquivos. 

6. Além disso, se for necessário, podemos baixar todo o projeto em uma outra máquina fazendo o *clone* do mesmo: 

````bash
git clone https://github.com/fbarth/roteiro_git.git
````

Percebam que a URL informada acima é a mesma informada no item 3. Quando você for fazer isto com o seu projeto você terá que informar a URL do seu projeto. 

## Compartilhando o projeto com outros desenvolvedores

Ok! Agora está na hora de compartilhar o projeto com outros desenvolvedores. Para isto, basta ir na aba *Settings*, item *Collaborators*. Se você fizer isto, você vai chegar em uma página similar a esta: 

<img src="./assets/add_people.png" alt="Adicionando colaborador" style="width:800px;"/>

O novo desenvolvedor foi adicionado como colaborador e agora poderá fazer commits neste repositório remoto! Quando os repositórios são públicos, qualquer pessoa pode clonar ou fazer um fork do seu repositório remoto. Porém, somente os colaboradores podem fazer commits neste repositório. Em outras palavras, todos podem ler o código, mas apenas os colaboradores podem escrever.

## Criando conflitos para aprendermos a usar o merge

* O desenvolvedor 2 altera o método `mensagem()` na classe Gato, faz `commit` e `push`. O desenvolvedor 1 faz o mesmo. Mas quando ele executa o `push` então ele é obrigado a fazer um `pull`, `merge` e então enviar para o repositório remoto. 

* O mesmo acontece quando os desenvolvedores resolvem ao mesmo tempo adicionar o método `gosta_futebol()` na classe Pessoa.

Tudo isto acontecendo no branch `main`. 

## Usando branches diferentes







