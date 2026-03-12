# 🔐 django-authentication-with-github-oauth2

## 📌 Descrição do projeto

Este projeto é um sistema de autenticação desenvolvido com Django que utiliza OAuth2 para permitir login seguro através do GitHub.

A aplicação demonstra a integração com provedores externos de autenticação utilizando django-allauth, permitindo que o usuário faça login com sua conta do GitHub. Após a autenticação, os dados básicos do usuário são armazenados no banco de dados padrão do Django e o usuário é redirecionado para uma área restrita de membros.

O foco principal deste projeto foi praticar a implementação de autenticação com OAuth2, integração com API externa, uso de variáveis de ambiente para segurança e organização de um projeto backend com Django.

Este projeto possui interface simples, pois o foco principal foi a funcionalidade de login.

---

## ⚙️ Funcionalidades

* Login com conta do GitHub usando OAuth2
* Integração com django-allauth
* Armazenamento automático de usuários no banco do Django
* Redirecionamento para página de membros após login
* Uso de variáveis de ambiente (.env) para proteger credenciais
* Templates básicos com HTML e CSS
* Estrutura organizada de projeto Django

---

## 👤 Como os usuários podem utilizar

### 1. Clonar o repositório

git clone [https://github.com/seu-usuario/django-authentication-with-github-oauth2.git]

### 2. Criar ambiente virtual

python -m venv venv

Ativar no Windows:

venv\Scripts\activate

Ativar no Linux/Mac:

source venv/bin/activate

### 3. Instalar dependências

pip install -r requirements.txt

### 4. Criar arquivo .env

Crie um arquivo chamado `.env` na raiz do projeto e adicione:

GITHUB_CLIENT_ID=seu_client_id
GITHUB_SECRET=seu_secret

### 5. Aplicar migrações

python manage.py migrate

### 6. Rodar o servidor

python manage.py runserver

### 7. Acessar no navegador

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Clique no botão de login com GitHub, faça a autenticação e você será redirecionado para a página de membros.

---

## ❓ Onde encontrar ajuda

Se tiver dúvidas sobre o projeto, você pode buscar ajuda através de:

* Issues deste repositório no GitHub
* Fórum da Alura
* LinkedIn do autor
* Email do autor

LinkedIn: https://www.linkedin.com/in/rafael-dias-fontes-2a947b3a7/
Email: rafael071007@gmail.com

Este projeto foi desenvolvido como parte de estudos com apoio de cursos da Alura.

---

## 👨‍💻 Autores

Rafael Dias

Projeto desenvolvido para fins de estudo e prática em Django, autenticação OAuth2 e integração com APIs externas.
Baseado em conteúdos educacionais da Alura.

