from flask import render_template, request, url_for, redirect
from flask_login import login_user, logout_user
from app import app, db
from app.models import User

@app.route('/pagina_inicial')
def pagina_inicial():
    #renderiza a pagina inicial
    return render_template('pagina_inicial.html')

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    #Guarda erros
    erro_email = 0
    erro_usuario = 0

    #Se receber um post
    if request.method == "POST":

        #Armazena dados do usuário
        username = request.form["username"]
        email = request.form["email"]
        pwd = request.form["password"]

        #Verifica se existe email ou usuario pois são campos únicos.
        email_existe = db.session(db.select(User).filter_by(email=email))
        username_existe = db.session(db.select(User).filter_by(username=username))

        #Retorna erro se existir email
        if email_existe:
            # email ja cadastrado, insira outro
            print("email ja cadastrado.")
            erro_email = 1

        #Retorna erro se existir usuario
        elif username_existe:
            # username ja cadastrado, insira outro
            print("nome de usuario ja cadastrado.")
            erro_usuario = 1

        #Se chegou aqui, usuário pode ser criado
        #no banco de dados e redirecionar o usuario
        #para a página de login
        else:
            user = User(username=username, email=email, password=pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("entrar"))
        
    return render_template('registrar.html')

@app.route('/entrar', methods=["GET", "POST"])
def entrar():
    #Guarda erro
    erro_login = 0

    #Se receber um post:
    if request.method == "POST":
        #Recebe email e senha
        email = request.form["email"]
        pwd = request.form["password"]

        #Verifica se o usuário está no banco
        user = db.session.execute(db.select(User).filter_by(email=email).scalar_one())

        #Se não estiver ou a senha estiver incorreta, 
        #retorna um erro
        if not user or not user.verify_password(pwd):
            print("Usuário e/ou senha incorretos.")
            erro_login = 1

            return redirect(url_for("entrar"))

        #Se chegou aqui não houve erros
        login_user(user)

    #Renderiza a pagina inicial
    return render_template('pagina_inicial.html')

#Desloga e redireciona o usuário
#para a página inicial
@app.route('/sair')
def sair():
    logout_user()
    return redirect(url_for('pagina_inicial'))

if __name__ == "__main__":
    app.run(debug=True)