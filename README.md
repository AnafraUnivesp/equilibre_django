## equilibre_django

### **Domínio**: [equilibreapp](https://equilibreapp.onrender.com/)

## Pré-Requisitos

- Instalar o **Django**
- Instalar o **Python**
- Instalar **Visual Studio** ou a IDE da sua preferência que execute Python
- Possuir uma conta no **Github**

> Lembrando que são comandos para Windows

## Getting Started 

Comando para **criar um env** (ambiente) dentro do meu diretório.

```
python -m venv venv

```

Neste trecho eu **ativo o ambiente virutual** no meu prompt (cmd)
```
.\venv\Scripts\activate

```
A aplicação entrará no modo ambiente local:

exemplo
> <font colo="green">(venv) PS C:\Users\Usuario\Documents\Univesp\pi02_v2\equilibre_django> </font>


Neste trecho houve a instalação do **django** mais a **biblioteca** <font color="red">**gunicor**</font>

> O gunicor é um **servidor de aplicação** que atende as requisições do nosso servidor.

```
pip install django gunicorn

```

Caso seja solicitado **atualize a versão do pip**  utilizando o seguinte comando:

```
python.exe -m pip install --upgrade pip

```

Para **iniciarmos um novo projeto** utilizamos o **django-admin**, mas caso eu queria investigar quais são os outros comando que compõem o admin-django utilize o comando abaixo:

```
admin-django --help

``` 

## Iniciando o Projeto

1. Retorne à pasta raiz do projeto 

Para iniciar um novo projeto utilize o comando abaixo:

```
admin-django startproject NOMEDOPROJETO .

``` 
Obs. o caractere de ponto significa que eu estou **indicando** a instalação no diretório raiz. 

2. Confira se a pasta projeto foi criada e seus principais arquivos:

Exemplo:

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        23/10/2024     08:46                equilibreapp
d-----        23/10/2024     08:18                venv
-a----        23/10/2024     07:49           3301 .gitignore
-a----        23/10/2024     07:49           1088 LICENSE
-a----        23/10/2024     08:46            690 manage.py
-a----        23/10/2024     08:31            576 README.md

```
Confira se o arquivo **manage.py** foi criado. E se dentro da pasta do projeto foram criados os arquivos padrões: 

**Exemplo:**

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----        23/10/2024     08:46            417 asgi.py
-a----        23/10/2024     08:46           3363 settings.py**
-a----        23/10/2024     08:46            790 urls.py**
-a----        23/10/2024     08:46            417 wsgi.py**
-a----        23/10/2024     08:46              0 __init__.py**

```

## Executando o Projeto Localmente

Rode o comando para executar o servidor localmente

```
python manage.py runserver

```

**Exemplo**
![Primeira Página de Execução](./static/img/000_log_execucao_local.png)

Clique no endereço apontado no prompt ou digite na barra de endereço do seu **localhost:8000**

![Primeira Página de Execução](./static/img/001_primeira_execucao.png)


## Escolhendo a nuvem para hospedagem da aplicação

Nesta ocasião foi escolhida a nuvem [Render.com](https://render.com/) 
Neste serviço é possível deployar:

- Sites Estáticos;
- Aplicações Web
- Bancos de Dados (Postgres)


![Render](./static/img/002_render_cloud.png)


1. Realize Login e Senha na página do Render./
2. Escolha o tipo do microserviço a ser utilizado
3. Preenchar as informações referentes á aplicação.
4. Integre o Render ao seu github ( O render irá buscar informações de sua aplicação no repositório da sua aplicação)

Neste caso fizemos a seguinte configuração:

**Parte 01**

![Render](./static/img/003_configurando_o_render_part01.png)

**Parte 02**

![Render](./static/img/004_configurando_o_render_part02.png)

- Na sessão de language é possível escolher : Node,Angular, Python3, Ruby e etc. Nesta ocasião definimos inicialmente o Python3;
- A region, foi escolhida automaticamente, não realizamos alterações;
- A branch main será a nossa branch referência;
- A sessão de Root, utilizamos o caractere .(ponto), para que ele busque a aplicação na árvore principal do repositório. 
- A sessões de **build command** e **Start command** são geradas automaticamente quando a linguagem é definida, mas pode ser alterada manualmente. 

**Parte 03**

![Render](./static/img/005_configurando_o_render_part03.png)

- Estamos utilizando um recurso gratuito 


1. Após realizar o cadastro, definir o tipo do microserviço e preencher os campos na nuvem, retorne para o prompt 
2. Instale a **biblioteca requiriments.txt**


Rode o comando:

```
pip install -r requirements.txt

``` 

Caso apresente **erros** rode o comando abaixo:

```
pip freeze > requirements.txt

``` 

***fonte:** [Stackoverflow](https://stackoverflow.com/questions/46854451/pip-install-r-requirements-txt-errno-2-no-such-file-or-directory-requiremen)


3. **IMPORTANTE:** 

Ainda no Render, na sessão **START COMMAND**, preencha o **nome da pasta** que se encontra a sua aplicação.
Como no nosso caso escolhemos a biblioteca **gunicorn** e **python3** como linguagem o seguinte campo ficou da seguinte forma:


> ./$ gunicorn equilibreapp.wsgi

**Obs:** Este nome, é o nome definido no Render, o mesmo poderá ser alterado futuramente, acesse o **Settings Render** para editar e configurar novas informações.

4. Após execução, o Render gerará uma página de logs de deploy. Portanto é necessário atualizar as informações locais, subi-las para a **branch main**, já que o Render buscará a aplicação na mesma. 


5. **IMPORTANTE:** 

Localize no Render o endereço de domínio da sua aplicação:

![Localizado meu dominio](./static/img/006_endereco_dominio_logs.png)

O deploy apresentará um **erro de deploy** já previsto ao acessarmos o endereço de domínio gerado pelo Render.


![Erro de acesso domínio](./static/img/008_erro_de_acess-_domínio.png)


6. Retorne ao repositório do projeto, acesse o arquivo **Settings.py**

7. Adicione o endereço no campo **ALLOWED_HOSTS**

```
ALLOWED_HOSTS = ['https://equilibreapp.onrender.com', '*']

```
Obs: Foi inserido um **wildcard** no código para permitir também outros hosts(qualquer).


8. Realize o commit e o merge novamente e subi as alterações na branch main.

9. O próprio Render irá sincronizar os deploys junto ao Github. 

10. Ao acessar novamente o domínio, notamos que nossa página principal rodou com sucesso:


![Acessando minha aplicação no via Domínio](./static/img/007_sucesso_dominio.png)

## Testes

## TDD - Desenvolvimento Orientado a Testes ( em conjunto com a integração contínua)

Para facilitar o processo de testes, crie uma **nova Issue** no Github, chamada: [Implementar Integração Contínua](https://github.com/AnafraUnivesp/equilibre_django/issues/4)

Estes testes servirão para entender se a nossa aplicação funcionára conforme o esperado. 

1. Baixe o programa **pytest-edjango**,acese a documentação do mesmo clicando [aqui](https://pytest-django.readthedocs.io/en/latest/)
O programa, trarás as funcionalidade do Django para a nossa área de testes. 


![Pytest-Django](./static/img/009_pystest_django.png)


2. Para instalar a dependência pyteste,insira os comando do pip conforme a documentação. Porém os testes serão apenas realizados em um **ambinte de desenvolvimento**. 

```
$ pip install pytest-django

```
3. Após realizar a instalar, verifique no Settings da sua IDE, se o Pytest está habilitado para testes. Como estu utilizando o VS Code, realizei o seguinte caminho:

![Settings VS Code](./static/img/010_config_pytest_vscode.png)

**Obs:** Durante o desenvolvimento do projeto, foi mais interessante instalar a **IDE Pycharm**. Na imagem abaixo é possível
identificar, como realizar a mesma configuração do pytest, no settings do Pycharm.


![Settings VS Code](./static/img/011_config_pytest_pycharm.png)


4. Para realizarmos o teste, foi necessário criar um novo arquivo dentro da pasta do meu projeto equilibreapp padrão chamado
**test_home.py**

5. No corpo do arquivo teste inserir o seguinte comando abaixo:

```
def test_home_status_code(client:Client)

```
6. Caso o Pychard não identifique o Client, será necessário instalar a bibliteca/ dependências **django.test**

```
 pip install django.test

```

### **Teste de CRUD**

No arquivo **test_home.py** inserimos os comando para realizar os primeiros teste **(Solicitação x Reposta)**:

![Settings VS Code](./static/img/012_teste_de_get_200.png)

1. O django irá disponibilizar o objetivo Client para que possamos realizar o testes;
2. O objeto do tipo Client, irá emular requisições https;
3. Para isso realize o import da classe e crie um get, o qual a resposta será obtida através da raiz do projeto,onde inserimos ('/').
4. Ao rodar o teste, o log do terminal, informará que falta configurar o Settings do emulador de teste, o qual está 
disponível na documentação do [Pyteste-Django](https://pytest-django.readthedocs.io/en/latest/#example-using-pytest-ini-or-tox-ini)

Para configurar o settings do pytest, será necessário criar um novo arquivo na **raiz do projeto**, vamos chamá-la de 
**setup.cfg**. *cfg* se refere a *Configuração*


![Settings VS Code](./static/img/013_arquivo_setup_log.png)

1. Na imagem acima, podemos identificar que na dependência foi inserida o nome da pasta da aplicação e o foi adicionado o tool junto ao nome da condiguração.
2. O python também disponibiliza como padrão os modelos dos arquivos para testes
3. Na imagem também destacamos o arquivo setup.cf salvo na árvore do projeto
4. No log também identificamos uma falha acusando o código 404 (Página não encontrada)
5. Como não implantamos uma página de fato no django o código 404 chama uma página válida para ser exibida.


### **Teste de CRUD** - Criando uma view

Para que a página seja exibida, criamos um novo arquivo, chamado **home_view** dentro da nossa pasta de projeto. 

1. Na view(home) inicialmente precisamos sempre inciá-la com um parâmetro chamado request;
2. A seguir devemos definir o **path** que esta view irá responder.
3. No arquivo **url.py** temos algumas informações padrõnizadas do Django. 
4. Crie um novo path e indique a função que foi criada(home);
5. Lembre-se de informar no import a localização da view( neste caso a pasta do projeto) e o nome da função home


![Teste 01 - url.py ](./static/img/014_url_log_erro.png)

6. **Como esperado** será apresentado um novo **erro** no log do terminal
7. O path vazio, faz uma busca na raiz do nosso projeto, o qual será atendido pela view home. 
8. Como na imagem acima, o erro indica que a **requisição http, retornou uma informação vazia**
9. Para corrigir o erro, precisamos indicar na nossa view o retorno de um requisição simples. 

### **Teste de CRUD** - Nosso Primeiro Hello Univesp

1. Como na imagem abaixo, retornamos no arquivo **home_view.py** e informamos a função **HttpResponse**
2. Também indicamos o retorno aguardado pela nossa requisição e a mensagem a ser apresentada na tela.
3. Ao executar, a requisição foi executada com sucesso

![Teste 01 - url.py ](./static/img/015_home_view_teste_passed.png)

4. Para executar de fato, rode localmente a aplicação para verificar se as requisições realizadas ao servidor retornarão o nosso primeir Hello Univesp
5. No terminal rode:

```
python manage.py runserver

```
6. Verifique o localhost gerado pelo servidor:

![Teste 01 - url.py ](./static/img/016_hello_univesp.png)


## **Servidor de Integração Contínua - Utilizando o Github Actions**

Para executarmos os testes automaticamente, podemos realizar uma configuração, construindo um ambiente que rode nossos testes em um ambiente virtual.

1. No terminal informe o comando abaixo, onde foi terminado um código de sucesso.
```
pytest

```
2. Para criar essa configuração de teste no Github Actions, criamos manualmente Na pasta raiz a pasta **.github/workflows**
3. Crie um arquivo **django.yml**, nele faremos algumas configurações básicas..
4. Consulte o arquivo para verificar os detalhes. 
5. Também foi configurada a **instalação do pipenv**

```
 pip install pipenv

```








Parei Aqui [Imersão Django (EP. 2)](https://www.youtube.com/watch?v=wj4Qj73Mz7I) 


# Referências:

- [Imersão Django](https://www.youtube.com/watch?v=zLIeu9cPYrY&t=553s)
- [Tutorial de Configuração do Render](https://www.youtube.com/watch?v=bnCOyGaSe84)