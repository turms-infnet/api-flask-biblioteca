from flask import jsonify, request
from typing import List

from app import app
from controllers.livro_controller import listar_livros, buscar_livro, criar_livro, atualizar_livro, deletar_livro
from models.livro import Livro
from utils.validator import validate_fields

@app.route("/livros", methods=["GET"])
def listar_livros_view():
    livros: List[Livro] = listar_livros()
    return jsonify([livro.to_dict() for livro in livros]), 200

@app.route("/livros/<int:livro_id>", methods=["GET"])
def buscar_livro_view(livro_id):
    livro: Livro = buscar_livro(livro_id)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    
@app.route("/livros", methods=["POST"])
def criar_livro_view():
    data = request.get_json(silent=True) or {}

    result = validate_fields(data, ["titulo", "ano_publicacao", "autor_id", "categorias"])

    if result[0]:
        return jsonify(result[1]), 400

    livro: Livro = criar_livro(data)

    return jsonify(livro.to_dict()), 201

@app.route("/livros/<int:livro_id>", methods=["PUT"])
def atualizar_livro_view(livro_id):
    data = request.get_json(silent=True) or {}
    livro = atualizar_livro(livro_id, data)
    if livro is None:
        return jsonify({"erro": "Livro não encontrado"}), 404
    return jsonify(livro.to_dict()), 200

@app.route("/livros/<int:livro_id>", methods=["DELETE"])
def deletar_livro_view(livro_id):
    sucesso = deletar_livro(livro_id)
    if not sucesso:
        return jsonify({"erro": "Livro não encontrado"}), 404

    return "", 204