# Monitorador de intercambio UFF

- ## Para que serve:
Esse projeto foi criado com a intenção de monitorar o lançamento de editais de mobilidade dda Universidade Federal Fuminense.

- ## Como funcina:
De tempo em tempo o programa lê a página web de editais da UFF e compara se ele já leu aquele último edital. Caso não tenha lido, ele envia para o email desejado o título do edital e a url para acessalo.

- ## Como rodar:
- Git clone no repositório 
- Instale as bibliotecas de requirements.txt (aconselho usar venv)
- Rode o programa uma vez e passe o email e uma senha de aplicativo desse email **NÂO PASSE A SENHA VERDADEIRA**
- Use um agendador de tarefas para rodar o programa na hora desejada, como o task scheduler no windows ou o contab no linux. Exemplo do meu comando no crontab:

'''
0 14 * * * cd /caminho_do_projeto && venv/bin/python3 main.py
'''