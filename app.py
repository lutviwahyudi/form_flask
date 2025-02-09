from flask import Flask
from models.model import db
from blueprints.main_blueprint import main_views
from blueprints.auth_blueprint import auth_views

app = Flask(__name__)

# Tambahkan secret key
app.secret_key = "ini_secret_key_rahasia_ubah_ya"

# Konfigurasi database MySQL untuk XAMPP/Laragon
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/belajar_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi database
db.init_app(app)

app.register_blueprint(main_views)
app.register_blueprint(auth_views)