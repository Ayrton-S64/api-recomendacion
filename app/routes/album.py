from flask import Blueprint
from app.controllers.album import list_albums,test

album_bp = Blueprint('album',__name__)

album_bp.route('/',methods=['GET'])(list_albums)
album_bp.route('/test',methods=['GET'])(test)