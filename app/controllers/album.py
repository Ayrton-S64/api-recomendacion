from flask import request, jsonify
from app.services.album import get_all

def test():
  try:
    return jsonify({
      'status': True,
      'code': 200,
      'error': None,
      'data': "Hola mundo",
    }), 200
  except Exception as e:
    return jsonify({
      'status': False,
      'code': 400,
      'error': str(e),
      'data': None,
    }), 400

def list_albums():
  try:
    data = get_all()
    return jsonify({
      'status': True,
      'code': 200,
      'error': None,
      'data': data,
    }), 200
  except Exception as e:
    return jsonify({
      'status': False,
      'code': 400,
      'error': str(e),
      'data': None,
    }), 400