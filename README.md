# Roteiro para uso do Git e GitHub

1. Criar uma conta no [GitHub](https://github.com/). O que é GitHub?

2. Instalar o git no seu computador seguindo os passos disponíveis nesta página: [https://git-scm.com/downloads](https://git-scm.com/downloads). O que é Git? 

3. Criar um repositório na sua conta no GitHub em [https://github.com/new](https://github.com/new). Você vai dar um nome para o seu projeto e clicar em *Create repository*. Depois disso uma tela irá aparecer te mostrando algumas opções para o setup do seu projeto: 

* criando um novo repositório a partir de arquivos existentes na sua máquina: 

````bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/fbarth/roteiro_git.git
git push -u origin main
````

* fazendo o *push* de um repositório remoto: 

````bash
git remote add origin https://github.com/fbarth/roteiro_git.git
git branch -M main
git push -u origin main
````


