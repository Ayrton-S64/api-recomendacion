from flask import request, jsonify
from app.services.auth import verify_user

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

def login():
  try:
    email = request.json.get('email')
    password = request.json.get('password')
    user = verify_user(email, password)
    return jsonify({
      'status': True,
      'code': 200,
      'error': None,
      'data': user,
    }), 200
  except Exception as e:
    return jsonify({
      'status': False,
      'code': 400,
      'error': str(e),
      'data': None,
    }), 400