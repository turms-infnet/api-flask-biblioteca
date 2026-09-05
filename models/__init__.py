from flask_sqlalchemy import SQLAlchemy

# Esta é A instância do ORM (Object-Relational Mapper) usada por toda a aplicação.
#
# Repare que ela é criada aqui, "solta", sem estar ligada a nenhuma aplicação Flask
# ainda. Isso é proposital: todos os arquivos de model (autor.py, livro.py, etc.)
# importam esse mesmo objeto `db` para poder declarar suas classes/tabelas.

db = SQLAlchemy()