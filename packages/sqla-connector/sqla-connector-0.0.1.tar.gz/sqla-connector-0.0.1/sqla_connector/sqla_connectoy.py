"""Configs from database conncetions"""

from sqlalchemy import create_engine, Connection
from sqlalchemy.orm import sessionmaker


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import Config

class SQLAConnector:
    """Manipulador de Conexão com Banco de Dados usando SQLAlchemy.
    
    Esta classe gerencia conexões com o banco de dados utilizando o SQLAlchemy,
    oferecendo um mecanismo para criar sessões e realizar operações no banco de dados
    de forma segura e eficiente.
    """

    def __init__(self) -> Connection:
        """Inicializa a instância do manipulador de conexão com a string de conexão do banco de dados.

        Args:
            connection_string (str): A string de conexão usada para conectar ao banco de dados.
        """
        self.__connection_string = Config.CONNECTION_STRING
        self.__engine = create_engine(self.__connection_string)
        self.session = None

    def get_engine(self):
        """Retorna o engine de conexão com o banco de dados.

        Retorna:
            engine: Uma instância de Engine do SQLAlchemy configurada com a string de conexão.
        """
        return self.__engine

    def __enter__(self):
        """Entra no contexto de gerenciamento de recursos, configurando e retornando uma sessão.

        Retorna:
            self: Uma instância de DBConnectionHandler com uma sessão ativa.
        """
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Sai do contexto de gerenciamento de recursos, fechando a sessão atual, se houver.

        Args:
            exc_type: Tipo da exceção, se alguma exceção foi levantada dentro do bloco 'with'.
            exc_val: Valor da exceção, se alguma exceção foi levantada.
            exc_tb: Rastreamento da exceção, se alguma exceção foi levantada.
        """
        if self.session:
            self.session.close()

def db_connector(func):
    """Decorador para fornecer uma conexão de banco de dados a uma função.
    
    Args:
        func: A função que será decorada.

    Returns:
        A função decorada com uma conexão de banco de dados injetada.
    """
    def with_connection_(*args, **kwargs):
        with SQLAConnector() as connection:
            session = connection.session
            try:
                return func(*args, session=session, **kwargs)
            except Exception as e:
                session.rollback()
                raise
            finally:
                session.close()

    return with_connection_


