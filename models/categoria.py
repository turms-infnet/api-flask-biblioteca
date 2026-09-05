from models.livro import livro_categoria
from models import db

class Categoria(db.Model):
    __tablename__ = "categoria"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)

    livros = db.relationship("Livro", secondary=livro_categoria, backref="categorias")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "livros": [livro.to_dict() for livro in self.livros]
        }
