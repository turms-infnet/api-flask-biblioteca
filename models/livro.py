from models import db

livro_categoria = db.Table(
    "livro_categoria",
    db.Column("xid_livro", db.Integer, db.ForeignKey('livro.id'), primary_key=True),
    db.Column("xid_categoria", db.Integer, db.ForeignKey('categoria.id'), primary_key=True),
)

class Livro(db.Model):
    __tablename__ = "livro"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ano_publicacao = db.Column(db.Integer)

    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"), nullable=False)

    categorias = db.relationship("Categoria", secondary=livro_categoria, backref="livros")

    def to_dict(self):
            return {
                "id": self.id,
                "titulo": self.titulo,
                "ano_publicacao": self.ano_publicacao,
                "autor_id": self.autor_id,
                "categorias": [categoria.to_dict() for categoria in self.categorias],
            }
    