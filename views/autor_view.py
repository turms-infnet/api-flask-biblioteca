from flask import jsonify, request
from typing import List

from app import app
from controllers.autor_controller import listar_autores, buscar_autor, criar_autor, atualizar_autor, deletar_autor
from models.autor import Autor
from utils.validator import validate_fields

@app.route("/autores", methods=["GET"])
def listar_autores_view():
    autores: List[Autor] = listar_autores()
    return jsonify([autor.to_dict() for autor in autores]), 200

@app.route("/autores/<int:autor_id>", methods=["GET"])
def buscar_autor_view(autor_id):
    autor: Autor = buscar_autor(autor_id)
    if autor is None:
        return jsonify({"erro": "Autor não encontrado"}), 404

@app.route("/autores", methods=["POST"])
def criar_autor_view():
    data = request.get_json(silent=True) or {}

    result = validate_fields(data, ["nome", "nacionalidade"])

    if result[0]:
        return jsonify(result[1]), 400

    autor: Autor = criar_autor(data)

    return jsonify(autor.to_dict()), 201

@app.route("/autores/<int:autor_id>", methods=["PUT"])
def atualizar_autor_view(autor_id):
    data = request.get_json(silent=True) or {}
    autor = atualizar_autor(autor_id, data)
    if autor is None:
        return jsonify({"erro": "Autor não encontrado"}), 404
    return jsonify(autor.to_dict()), 200

@app.route("/autores/<int:autor_id>", methods=["DELETE"])
def deletar_autor_view(autor_id):
    sucesso = deletar_autor(autor_id)
    if not sucesso:
        return jsonify({"erro": "Autor não encontrado"}), 404

    return "", 204