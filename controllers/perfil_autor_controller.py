from models import db
from models.autor import Autor
from models.perfil_autor import PerfilAutor

def buscar_perfil(perfil_id):
    return PerfilAutor.query.get(perfil_id)

def criar_perfil(data):
    autor = Autor.query.get(data.get("autor_id"))
    if autor is None:
        return None, "Autor não encontrado"

    if autor.perfil is not None:
        return None, "Este autor já possui um perfil (relação 1:1)"

    perfil = PerfilAutor(
        biografia=data.get("biografia"),
        site_pessoa=data.get("site_pessoa"),
        autor_id=autor.id
    )
    
    db.session.add(perfil)
    db.session.commit()
    return perfil, None

def atualizar_perfil(perfil_id, data):
    perfil = PerfilAutor.query.get(perfil_id)
    if perfil is None:
        return None

    perfil.biografia = data.get("biografia", perfil.biografia)
    perfil.site_pessoal = data.get("site_pessoal", perfil.site_pessoal)
    db.session.commit()
    return perfil

def deletar_perfil(perfil_id):
    perfil = PerfilAutor.query.get(perfil_id)
    if perfil is None:
        return False

    db.session.delete(perfil)
    db.session.commit()
    return True