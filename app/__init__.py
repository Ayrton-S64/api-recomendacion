from flask import Flask
from flask_cors import CORS
from app.routes import auth, song, album

app = Flask(__name__)
CORS(app, origins='*')

app.register_blueprint(auth.auth_bp, url_prefix='/auth')
app.register_blueprint(song.song_bp, url_prefix='/songs')
app.register_blueprint(album.album_bp, url_prefix='/albums')
