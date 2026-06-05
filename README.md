repositorio criado para auxiliar meus estudos de poo, sendo composto pelo arquivo conversor.py que gera um arquivo .puml a partir do codigo python

sobre o compartilhamento e sincronização de codigo, os seguintes comandos git foram utilizados:

git init
- inicia o novo projeto com git

git add <nome-arquivo> ou git add .
- add os arquivos que estao prontos para serem commitados

git commit -m "mensagem do commit"
- salva os arquivos no historico

git log
- mostra os ultimos commit (log de alteraçoes)

git status
- mostra o estado da nossa ramificaçao atual

git diff
- mostra o que foi alterado até o momento / alteraçoes na ramificaçao

git merge
- usado para mesclar diferentes ramificaçoes

git branch | git checkout branch -b <nome-da-branch>
- mostra a branch atual | cria uma nova branch versionada a partir da branch atual

git checkout <nome-branch>
- sai da branch atual e entra na branch informada

git remote add <nome> <url>
- add um novo repositorio remoto

git push <nome> <nome-da-branch>
- envia as alteraçoes locais para o repositorio remoto

git pull <nome> <nome-da-branch>
- busca as alteraçoes do repositorio remoto e os traz para a maquina local

git fetch
- sincroniza o historico de branch local de acordo com o historico de branch remoto