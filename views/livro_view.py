from flask import jsonify, request

from app import app
from controllers.livro_controller import listar_livros, buscar_livro, criar_livro, atualizar_livro, deletar_livro

@app.route("/livros", method=["GET"])
def listar_livros():
    return jsonify({})

@app.route("/livros/<int:livro_id>", method=["GET"])
def buscar_livro(livro_id):
    return jsonify({})

@app.route("/livros", method=["POST"])
def criar_livro():
    data = request.get_json(silent=True) or {}

    return jsonify({})

@app.route("/livros/<int:livro_id>", method=["PUT"])
def atualizar_livro(livro_id):
    data = request.get_json(silent=True) or {}
    return jsonify({})

@app.route("/livros/<int:livro_id>", method=["DELETE"])
def deletar_livro(livro_id):
    return jsonify({})