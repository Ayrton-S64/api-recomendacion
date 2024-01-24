from flask import Blueprint
from app.controllers.auth import login,test

auth_bp = Blueprint('auth',__name__)

auth_bp.route('/login',methods=['POST'])(login)
auth_bp.route('/test',methods=['GET'])(test)