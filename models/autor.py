from models import db

class Autor(db.Model):
    __tablename__ = "autor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50))

    livros = db.relationship("Livro", backref="autor", lazy=True)
    perfil = db.relationship("PerfilAutor", backref="autor", uselist=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nacionalidade": self.nacionalidade
        }
