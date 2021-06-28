from flask import Blueprint
from .views import Home, Signup, Login, Logout


user_bp = Blueprint('user_bp', __name__, template_folder='templates') # 첫번쨰 인자

user_bp.add_url_rule('/', view_func = Home.as_view('home'))
user_bp.add_url_rule('/signup/', view_func = Signup.as_view('signup'))
user_bp.add_url_rule('/login/', view_func = Login.as_view('login'))
user_bp.add_url_rule('/logout/', view_func = Logout.as_view('logout'))

