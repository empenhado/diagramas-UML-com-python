repositorio criado para auxiliar os estudos de poo do grupo de colaboradores (Ester Martins, Rafael Carvalho, Bruno Vital, Sérgio Guthyerres). este repositório é composto pelo arquivo conversor.py que gera um arquivo .puml a partir do codigo python

# fluxo de uso do conversor.py:
- para cada diagrama deve-se colar o codigo python dentro da variavel meu_codigo_python usando """ """
- mudar o nome do arquivo/diagrama na funçao gerar_arquivo_puml("nome_diagrama", meu_codigo_python)
- rodar o script no terminal

# dicas extras de configuraçao de ambiente:
- a extensao do PlantUML deve ser instalada para renderizar os diagramas
- o atalho alt + D abre uma aba com o diagrama gerado
- se o diagrama nao aparecer: abra as configuracoes do VS code (ctrl + ,) > digite plantuml render > mude a config de local para plantUMLServer > copie e cole a url do servidor oficial do PlantUML Server

# sobre o compartilhamento e sincronização de codigo, os seguintes comandos git foram utilizados:

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