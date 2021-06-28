# Python 3.8 - Tutorial do Django 3.2 - Sistema de Enquete
Fonte: https://docs.djangoproject.com/en/3.2/intro/tutorial01/

Polls (enquetes)

1. Para configurar o projeto, clone este repositório 

>> git clone https://github.com/emersonccf/enquete-django

2. e faça a criação de um ambiente virtual, 

>> python -m venv ve
ou
>> pyton3 -m venv ve

3. ative-o 

>> ve\Scripts\activate 
ou 
>> source ve/bin/activate

4. e depois instale a relação de dependências que constam na pasta e arquivo -> requirements.txt com o comando: 

>> pip install -r requirements.txt

Assim todas as dependencias serão instaladas.

5. Realize as migrações (cria o banco de dados e suas tabelas):

>> python manage.py migrate

6. Crie o um super usuário para administra o sistema:

>> python manage.py createsuperuser

7. Caso preferir substitua os passos 2 a 4 pelos comandos do pipenv (Necessário
conhecimento pévio de Pyenv e Pipenv para seguir este item, caso não tenha opte antes
por estudar melhor ou seguir a primeira opção sugerida):

7.1 Crie o ambiente virtual sincronizado com as dependencias fixadas no arquivo
Pipfile.lock, você pode escolher em instalar com e sem as dependcias de desenvolvimento:
>> pipenv sync -d  (com todas as dependências)
ou
>>pipenv sync (sem as dependências de desenvovimento)

7.2 Ative o ambiente virtual:
>> pipenv shell

Pronto e a partir dai só é seguir os comandos dos itens 5 e 6
---