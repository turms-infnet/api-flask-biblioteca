from flask import jsonify, request
from typing import List

from app import app
from controllers.perfil_autor_controller import buscar_perfil, criar_perfil, atualizar_perfil, deletar_perfil
from models.perfil_autor import PerfilAutor
from utils.validator import validate_fields

@app.route("/perfil/<int:perfil_id>", methods=["GET"])
def buscar_perfil_view(perfil_id):
    perfil: PerfilAutor = buscar_perfil(perfil_id)
    if perfil is None:
        return jsonify({"erro": "Perfil não encontrado"}), 404

@app.route("/perfil", methods=["POST"])
def criar_perfil_view():
    data = request.get_json(silent=True) or {}

    result = validate_fields(data, ["biografia", "site_pessoal", "autor_id"])

    if result[0]:
        return jsonify(result[1]), 400

    perfil, erro = criar_perfil(data)

    if erro:
        return jsonify({"erro": erro}), 400

    return jsonify(perfil.to_dict()), 201

@app.route("/perfil/<int:perfil_id>", methods=["PUT"])
def atualizar_perfil_view(perfil_id):
    data = request.get_json(silent=True) or {}
    perfil = atualizar_perfil(perfil_id, data)
    if perfil is None:
        return jsonify({"erro": "Perfil não encontrado"}), 404
    return jsonify(perfil.to_dict()), 200

@app.route("/perfil/<int:perfil_id>", methods=["DELETE"])
def deletar_perfil_view(perfil_id):
    sucesso = deletar_perfil(perfil_id)
    if not sucesso:
        return jsonify({"erro": "Perfil não encontrado"}), 404

    return "", 204