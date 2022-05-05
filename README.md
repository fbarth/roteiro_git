# Roteiro para uso do Git e GitHub

1. Criar uma conta no [GitHub](https://github.com/). O que é GitHub?

2. Instalar o git no seu computador seguindo os passos disponíveis nesta página: [https://git-scm.com/downloads](https://git-scm.com/downloads). O que é Git? 

3. Criar um repositório na sua conta no GitHub em [https://github.com/new](https://github.com/new). Você vai dar um nome para o seu projeto e clicar em *Create repository*. Depois disso uma tela irá aparecer te mostrando algumas opções para o setup do seu projeto. Você pode, por exemplo, criar um novo repositório a partir de arquivos existentes na sua máquina: 

````bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fbarth/roteiro_git.git
git push -u origin main
````

Neste momento, você vai ver que todos os seus arquivos que estão no diretório local agora então na URL informada acima. Basta dar um refresh na URL acima. 

4. Adicionar novos arquivos ao seu projeto na sua máquina local:

* ver o status dos arquivos modificados:

````bash
git status
````

* você pode adicionar estas modificações em uma *staging area*, dizendo para o git que no próximo *commit* ele deverá considerar tais mudanças:

````bash
git add .
````

5. Fazendo o *commit* e *push* para o repositório remoto: 

````bash
git commit -m "estrutura inicial"
git push 
````








