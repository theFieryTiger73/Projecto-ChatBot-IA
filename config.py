import os

from dotenv import load_dotenv

load_dotenv()

server = os.environ.get("MSSQL_SERVER")
database = os.environ.get("MSSQL_DB")
driver = os.environ.get("MSSQL_DRIVER")
URI = os.environ.get("DATABASE_URI")
SECRET_KEY = os.environ.get("SECRET_KEY")

# configurações de conexão
server = server
database = database
driver = driver

SQLALCHEMY_DATABASE_URI = URI

SQLALCHEMY_TRACK_MODIFICATION = True

SECRET_KEY = SECRET_KEY