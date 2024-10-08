Este projeto é uma aplicação web de gerenciamento de biblioteca desenvolvida com Django e Django REST Framework.  Foi desenvolvido para uma ativdade de residência da CEPEDI pelos residentes Pablo Cezar Moreira Carvalho e Klaus Almeida Souza Santos


Instalação:

1. Clone o repositório:
git clone https://github.com/KlausAlmeida1/biblioteca-django-v2.git

2. Entre na pasta:
cd biblioteca-django-v2

3. Crie e ative o ambiente virtual Python:
python -m venv venv
venv\Scripts\activate

4. Instale as depedências:
pip install -r requirements.txt

5. Faça as migrações e popule o banco de dados:
python manage.py migrate
python manage.py populate_db

6. Inicie a aplicação:
python manage.py runserver



