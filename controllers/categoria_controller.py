from models import db
from models.categoria import Categoria

def listar_categorias():
    return Categoria.query.all()

def buscar_categoria(categoria_id):
    return Categoria.query.get(categoria_id)

def criar_categoria(data):
    categoria = Categoria(nome=data["nome"])
    db.session.add(categoria)
    db.session.commit()
    return categoria

def atualizar_categoria(categoria_id, data):
    categoria = Categoria.query.get(categoria_id)
    if categoria is None:
        return None

    categoria.nome = data.get("nome", categoria.nome)
    db.session.commit()
    return categoria

def deletar_categoria(categoria_id):
    categoria = Categoria.query.get(categoria_id)
    if categoria is None:
        return False

    db.session.delete(categoria)
    db.session.commit()
    return True