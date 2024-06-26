from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

@app.route('/pagina_inicial')
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]
        user = User(username=username, email=email, password=pwd)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("pagina_inicial"))
    return render_template('registrar.html')

@app.route('/entrar', methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        email = request.form["email"]
        pwd = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(pwd):
            return redirect(url_for("entrar"))

        login_user(user)
    return render_template('pagina_inicial.html')

@app.route('/sair')
def sair():
    logout_user()
    return redirect(url_for('pagina_inicial'))
if __name__ == "__main__":
    app.run(debug=True)