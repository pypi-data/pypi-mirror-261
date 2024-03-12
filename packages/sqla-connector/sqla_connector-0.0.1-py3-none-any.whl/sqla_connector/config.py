import os
from dotenv import load_dotenv

class Config:
    """Configuração base."""
    
    load_dotenv()
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    
class TestingConfig(Config):
    """Configuração de teste."""
    TESTING = True