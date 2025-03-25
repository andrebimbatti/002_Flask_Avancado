# Jogoteca - Sistema de Gerenciamento de Jogos

**Jogoteca** é um sistema CRUD (Create, Read, Update, Delete) desenvolvido em Python com o framework Flask. Este projeto permite gerenciar uma coleção de jogos de forma prática e segura, oferecendo funcionalidades como adição, visualização, edição e exclusão de jogos, além de um sistema de autenticação de usuários.

## Funcionalidades

- **Autenticação de Usuários**: Login seguro com senhas criptografadas.
- **Gerenciamento de Jogos**:
  - Adicionar novos jogos com informações como nome, categoria, console e capa.
  - Visualizar a lista completa de jogos cadastrados.
  - Editar detalhes de jogos existentes.
  - Excluir jogos da coleção.
- **Upload de Imagens**: Suporte para upload de capas personalizadas, com uma imagem padrão como fallback.
- **Interface Intuitiva**: Páginas renderizadas com templates HTML para uma experiência de usuário amigável.

## Tecnologias Utilizadas

- **Backend**: Python, Flask
- **Banco de Dados**: MySQL com SQLAlchemy como ORM
- **Frontend**: HTML, CSS, Jinja2
- **Segurança**: Flask-WTF (proteção CSRF), Flask-Bcrypt (criptografia de senhas)
- **Outras Bibliotecas**: Flask-SQLAlchemy, WTForms

## Como Instalar e Usar

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/jogoteca.git
   cd jogoteca
  
2. **Crie e ative um ambiente virtual**:
    ```bash
      
    python -m venv venv

- 2.1 Ativando no Linux/Mac:
    ```bash
    source venv/bin/activate  
    ```
    
- 2.3 **Ativando no windows**:
  ```bash
  venv\Scripts\activate     # Windows
  ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Rode o arquivo para configurar o banco de dados**:
    ```bash
   python prepara_banco.py
    ```
    
5. **Execute o app principal**:
   ```bash
   python jogoteca.py
   ```
## Time

| [<img src="https://avatars.githubusercontent.com/u/37429520?v=4" width="115"><br><sub>André Bimbatti</sub>](https://github.com/andrebimbatti) |
| :---: |

## Licença

Este projeto está licenciado sob a licença MIT. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).

---
