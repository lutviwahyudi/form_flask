from flask import Blueprint, request, render_template, url_for, flash
from flask import redirect
from models.model import db, User
from werkzeug.security import generate_password_hash

auth_views = Blueprint("auth", __name__)

@auth_views.route("/register", strict_slashes=False, methods=["GET", "POST"])
def register():
    # Define application logic for homepage
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        # simpan kedatabase
        new_user = User(email=email, password=hashed_password)
        try: 
            db.session.add(new_user)
            db.session.commit()
            flash('akun berhasil didaftarkan', 'success')
        except:
            db.session.rollback()
            flash('akun gagal didaftarkan periksa inputan', 'danger')

        return redirect(url_for('main.index'))

    # Render template for GET requests
    return render_template("register.html")