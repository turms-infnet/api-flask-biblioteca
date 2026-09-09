from models import db
from models.livro import Livro
from models.categoria import Categoria

def _resolve_categorias(categoria_ids):
    if not categoria_ids:
        return []
    return Categoria.query.filter(Categoria.id.in_(categoria_ids)).all()

def listar_livros():
    return Livro.query.all()

def buscar_livro(livrvo_id):
    return Livro.query.get(livrvo_id)

def criar_livro(data):
    livro = Livro(
        titulo=data["titulo"],
        ano_publicacao=data["ano_publicacao"],
        autor_id=data["autor_id"],
    )

    livro.categorias = _resolve_categorias(data.get("categoria_ids", None))

    db.session.add(livro)
    db.session.commit()
    return livro

def atualizar_livro(livro_id, data):
    livro = Livro.query.get(livro_id)
    if livro is None:
        return None

    livro.titulo = data.get("titulo", livro.titulo)
    livro.ano_publicacao = data.get("ano_publicacao", livro.ano_publicacao)

    if "autor_id" in data:
        livro.autor_id = data["autor_id"]

    if "categoria_ids" in data:
        livro.categorias = _resolve_categorias(data.get("categoria_ids", None))

    db.session.commit()
    return livro

def deletar_livro(livro_id):
    livro = Livro.query.get(livro_id)
    if livro is None:
        return False

    db.session.delete(livro)
    db.session.commit()
    return True
