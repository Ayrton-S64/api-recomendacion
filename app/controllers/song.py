from flask import request, jsonify
from app.services.song import get_all, get_by_code
# from app.services.artista import 

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

def find_song(code:str):
  try:
    data = get_by_code(code);
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

def list_songs():
  try:
    print('printing list songs')
    print('printing args',request.args)
    print('printing code',request.args.get('code',None))

    song_code = request.args.get('code',None)
    data = None 
    if(song_code):

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