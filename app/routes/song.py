from flask import Blueprint
from app.controllers.song import list_songs,test

song_bp = Blueprint('song',__name__)

song_bp.route('/',methods=['GET'])(list_songs)
song_bp.route('/test',methods=['GET'])(test)