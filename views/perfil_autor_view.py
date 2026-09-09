from flask import jsonify, request

from app import app
from controllers.perfil_autor_controller import buscar_perfil, criar_perfil, atualizar_perfil, deletar_perfil

@app.route("/perfil/<int:perfil_id>", method=["GET"])
def buscar_categoria(perfil_id):
    return jsonify({})

@app.route("/perfil", method=["POST"])
def criar_perfil():
    data = request.get_json(silent=True) or {}

    return jsonify({})

@app.route("/perfil/<int:perfil_id>", method=["PUT"])
def atualizar_perfil(perfil_id):
    data = request.get_json(silent=True) or {}
    return jsonify({})

@app.route("/perfil/<int:perfil_id>", method=["DELETE"])
def deletar_perfil(perfil_id):
    return jsonify({})