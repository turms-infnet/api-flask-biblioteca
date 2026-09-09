from flask import jsonify, request

from app import app
from controllers.autor_controller import listar_autores, buscar_autor, criar_autor, atualizar_autor, deletar_autor

@app.route("/autores", method=["GET"])
def listar_autores():
    return jsonify({})

@app.route("/autores/<int:autor_id>", method=["GET"])
def buscar_autor(autor_id):
    return jsonify({})

@app.route("/autores", method=["POST"])
def criar_autor():
    data = request.get_json(silent=True) or {}

    return jsonify({})

@app.route("/autores/<int:autor_id>", method=["PUT"])
def atualizar_autor(autor_id):
    data = request.get_json(silent=True) or {}
    return jsonify({})

@app.route("/autores/<int:autor_id>", method=["DELETE"])
def deletar_autor(autor_id):
    return jsonify({})