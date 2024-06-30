from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

@app.route('/pagina_inicial')
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    erro_email = 0
    erro_usuario = 0

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]
        email_existe = db.session(db.select(User).filter_by(email=email))
        username_existe = db.session(db.select(User).filter_by(username=username))

        if email_existe:
            # email ja cadastrado, insira outro
            print("email ja cadastrado.")
            erro_email = 1

        elif username_existe:
            # username ja cadastrado, insira outro
            print("nome de usuario ja cadastrado.")
            erro_usuario = 1

        else:
            user = User(username=username, email=email, password=pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("pagina_inicial"))
        
    return render_template('registrar.html')

@app.route('/entrar', methods=["GET", "POST"])
def entrar():
    erro_login = 0

    if request.method == "POST":
        email = request.form["email"]
        pwd = request.form["password"]

        user = db.session.execute(db.select(User).filter_by(email=email).scalar_one())

        if not user or not user.verify_password(pwd):
            print("Usuário e/ou senha incorretos.")
            erro_login = 1

            return redirect(url_for("entrar"))

        login_user(user)

    return render_template('pagina_inicial.html')

@app.route('/sair')
def sair():
    logout_user()
    return redirect(url_for('pagina_inicial'))

if __name__ == "__main__":
    app.run(debug=True)