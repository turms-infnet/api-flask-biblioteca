from flask import jsonify, request
from typing import List

from app import app
from controllers.categoria_controller import listar_categorias, buscar_categoria, criar_categoria, atualizar_categoria, deletar_categoria
from models.categoria import Categoria
from utils.validator import validate_fields

@app.route("/categorias", methods=["GET"])
def listar_categorias_view():
    categorias: List[Categoria] = listar_categorias()
    return jsonify([categoria.to_dict() for categoria in categorias]), 200

@app.route("/categorias/<int:categoria_id>", methods=["GET"])
def buscar_categoria_view(categoria_id):
    categoria: Categoria = buscar_categoria(categoria_id)
    if categoria is None:
        return jsonify({"erro": "Categoria não encontrada"}), 404

    return jsonify(categoria.to_dict())

@app.route("/categorias", methods=["POST"])
def criar_categoria_view():
    data = request.get_json(silent=True) or {}

    result = validate_fields(data, ["nome"])

    if result[0]:
        return jsonify(result[1]), 400

    categoria: Categoria = criar_categoria(data)

    return jsonify(categoria.to_dict()), 201

@app.route("/categorias/<int:categoria_id>", methods=["PUT"])
def atualizar_categoria_view(categoria_id):
    data = request.get_json(silent=True) or {}
    categoria = atualizar_categoria(categoria_id, data)
    if categoria is None:
        return jsonify({"erro": "Categoria não encontrada"}), 404
    return jsonify(categoria.to_dict()), 200

@app.route("/categorias/<int:categoria_id>", methods=["DELETE"])
def deletar_categoria_view(categoria_id):
    sucesso = deletar_categoria(categoria_id)
    if not sucesso:
        return jsonify({"erro": "Categoria não encontrada"}), 404

    return "", 204