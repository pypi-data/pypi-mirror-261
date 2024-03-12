# SQLAConnector

Simplifique sua conexão com bancos de dados em Python usando SQLAlchemy com o SQLAConnector, uma biblioteca que gerencia sessões e transações automaticamente.

## Instalação

bashCopy code

`pip install sqlaconnector`

## Configuração

Defina a string de conexão no `config.py`.

## Uso

**Gerenciando Sessões:**

pythonCopy code

`from sqlaconnector import SQLAConnector  with SQLAConnector() as connector:     # Operações de banco de dados`

**Decorador para Conexões:**

pythonCopy code

`from sqlaconnector import db_connector  @db_connector def sua_funcao(session):     # Operações de banco de dados`