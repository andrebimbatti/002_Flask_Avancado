import pymysql

print("Conectando...")

senha = input('Digite a senha do Banco de Dados \n')

try:
      conn = pymysql.connect(
      host='127.0.0.1',
      user='root',
      password=senha,
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor
      )
      
      cursor = conn.cursor()
      
      cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
      cursor.execute("CREATE DATABASE `jogoteca`;")
      cursor.execute("USE `jogoteca`;")
      
      # Criando tabelas
      TABLES = {
      'Jogos': '''
            CREATE TABLE `jogos` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `nome` varchar(50) NOT NULL,
            `categoria` varchar(40) NOT NULL,
            `console` varchar(20) NOT NULL,
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;''',
      
      'Usuarios': '''
            CREATE TABLE `usuarios` (
            `nome` varchar(20) NOT NULL,
            `nickname` varchar(8) NOT NULL,
            `senha` varchar(100) NOT NULL,
            PRIMARY KEY (`nickname`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;'''
      }
      
      for tabela_nome, tabela_sql in TABLES.items():
            try:
                  print(f'Criando tabela {tabela_nome}:', end=' ')
                  cursor.execute(tabela_sql)
                  print('OK')
            except pymysql.MySQLError as err:
                  print(f'Erro ao criar {tabela_nome}: {err}')
      
      # Inserindo usuários
      usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
      usuarios = [
      ("Andre Bimbatti", "Kaito", "animes"),
      ("Camila Ferreira", "Mila", "paozinho"),
      ("Guilherme Louro", "Cake", "python_eh_vida")
      ]
      cursor.executemany(usuario_sql, usuarios)
      
      cursor.execute('SELECT * FROM usuarios')
      print(' -------------  Usuários:  -------------')
      for user in cursor.fetchall():
            print(user['nickname'])
            
            # Inserindo jogos
            jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
            jogos = [
            ('Tetris', 'Puzzle', 'Atari'),
            ('God of War', 'Hack n Slash', 'PS2'),
            ('Mortal Kombat', 'Luta', 'PS2'),
            ('Valorant', 'FPS', 'PC'),
            ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
            ('Need for Speed', 'Corrida', 'PS2')
            ]
            cursor.executemany(jogos_sql, jogos)
            
      cursor.execute('SELECT * FROM jogos')
      print(' -------------  Jogos:  -------------')
            
      for jogo in cursor.fetchall():
            print(jogo['nome'])
            
            # Commitando as alterações
            conn.commit()
        
except pymysql.MySQLError as err:
    print(f'Erro de conexão: {err}')

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
