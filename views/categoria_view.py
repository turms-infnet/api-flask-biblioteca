from flask import jsonify, request

from app import app
from controllers.categoria_controller import listar_categorias, buscar_categoria, criar_categoria, atualizar_categoria, deletar_categoria

@app.route("/categorias", method=["GET"])
def listar_categorias():
    return jsonify({})

@app.route("/categorias/<int:categoria_id>", method=["GET"])
def buscar_categoria(categoria_id):
    return jsonify({})

@app.route("/categorias", method=["POST"])
def criar_categoria():
    data = request.get_json(silent=True) or {}

    return jsonify({})

@app.route("/categorias/<int:categoria_id>", method=["PUT"])
def atualizar_categoria(categoria_id):
    data = request.get_json(silent=True) or {}
    return jsonify({})

@app.route("/categorias/<int:categoria_id>", method=["DELETE"])
def deletar_categoria(categoria_id):
    return jsonify({})