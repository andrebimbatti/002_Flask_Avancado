import urllib.parse
import os

SECRET_KEY = 'alura'

try:
    with open('.\\extras\\pass.txt', 'r') as arquivo:
        password = str(arquivo.read().strip())
except Exception as e:
    print('Erro ao ler a senha')

pass_enc = urllib.parse.quote_plus(password)

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
        SGBD = 'mysql+pymysql',
        usuario = 'root',
        senha = pass_enc,
        servidor = '127.0.0.1',
        porta = '3306',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'