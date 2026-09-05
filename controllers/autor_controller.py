from models import db
from models.autor import Autor

def listar_autores():
    return Autor.query.all()

def buscar_autor(autor_id):
    return Autor.query.get(autor_id)

def criar_autor(data):
    autor = Autor(nome=data["nome"], nacionalidade=data["nacionalidade"])
    db.session.add(autor)
    db.session.commit()
    return autor

def atualizar_autor(autor_id, data):
    autor = Autor.query.get(autor_id)
    if autor is None:
        return None

    autor.nome = data.get("nome", autor.nome)
    autor.nacionalidade = data.get("nacionalidade", autor.nacionalidade)
    db.session.commit()
    return autor

def deletar_autor(autor_id):
    autor = Autor.query.get(autor_id)
    if autor is None:
        return False

    db.session.delete(autor)
    db.session.commit()
    return True