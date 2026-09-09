from flask import Flask, jsonify
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from models.autor import Autor
from models.perfil_autor import PerfilAutor
from models.livro import Livro
from models.categoria import Categoria

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return jsonify({
        'status': 'API Rodando...'
    })

from views import autor_view
from views import categoria_view
from views import livro_view
from views import perfil_autor_view
# from views import docs_view
