# Api Beers

Essa API foi desenvolvida utilizando Django e Django-Rest-Framework. Com essa API é possível o usuário realizar um cadastro, logar com seus dados, e utilizar o token gerado pelo Login para realizar operações CRUD salvando dados de cervejas.

---

## Instalação

- Clone esse repositório no seu computador utilizando `https://github.com/meiraDaniel/apiBeers` ou faça o download e a extração dos arquivos.

---

### Setup

- Dentro da pasta principal rode os comandos.

> Instale as dependências

```shell
$ pip install -r requirements.txt
```

> Rode o comando migrate, para criar o banco de dados. O arquivo com as migrations necessárias do modelo ToDo já estão criados.

```shell
$ python manage.py migrate
```

> Rode a API

```shell
$ python manage.py runserver
```

## Usabilidade

- Após inicialiazar o servidor, é possível realizar o cadastro de um novo usuário na url api/register/, passando no body da requisição os dados do novo usuário, como no exemplo abaixo. Esse endpoint só permite metodos post, não sendo possível recuperar a lista de usuários.

![alt text](https://github.com/meiraDaniel/apiBeers/blob/master/imgs/Register.png?raw=true)

- Com o novo usuário em mãos faça o login na url api/login, utilizando no body da requisição os dados cadastrados, como no exemplo abaixo:

![alt text](https://github.com/meiraDaniel/apiBeers/blob/master/imgs/Login.png?raw=true)

- Se a requisição for feita com sucesso, será retornado como resposta um token de acesso JWT, com tempo de vida de 1 hora.
- Com esse token em mãos é possível realizar as operações CRUD, disponíveis na url api/beers passando o token no header da requisição, como no exemplo abaixo.

![alt text](https://github.com/meiraDaniel/apiBeers/blob/master/imgs/HeaderToken.png?raw=true)

> Obs: testes de requisição da API feitas utilizando o Postman.
