from models import db

class PerfilAutor(db.Model):
    __tablename__ = "perfil_autor"

    id = db.Column(db.Integer, primary_key=True)
    biografia = db.Column(db.Text)
    site_pessoal = db.Column(db.String(150))
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "biografia": self.biografia,
            "site_pessoal": self.site_pessoal,
            "autor_id": self.autor_id
        }
