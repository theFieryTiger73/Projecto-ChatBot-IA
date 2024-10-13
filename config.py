DEBUG = True

# configurações de conexão
server = 'localhost\SQLEXPRESS'
database = 'chatbot'
driver = 'ODBC Driver 17 for SQL Server'

SQLALCHEMY_DATABASE_URI = f'mssql+pyodbc://{server}/{database}?driver={driver}'

SQLALCHEMY_TRACK_MODIFICATION = True

SECRET_KEY = 'um-nome-bem-seguro'