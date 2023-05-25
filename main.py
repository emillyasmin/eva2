from flask import Flask, g, render_template, \
    request, redirect, url_for, flash, session

from models.emprestimo_has_item import Emprestimo_has_item
from models.suapapi import Suap
from datetime import date

import mysql.connector

from models.usuario import Usuario
from models.usuarioDAO import UsuarioDAO
from models.material import Material
from models.materialDAO import MaterialDAO
from models.emprestimo import Emprestimo
from models.emprestimoDAO import EmprestimoDAO
from models.item import Item
from models.itemDAO import ItemDAO

app = Flask(__name__)
app.secret_key = "senha123"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = ""
DB_NAME = "bdlab"

app.auth = {
    'painel': {0:1, 1:1},
    'logout': {0:1, 1:1},
    'cadastrar_material': {0:1, 1:1},
    'cadastrar_item': {0:1, 1:1},
    'cadastrar_emprestimo': {0:1, 1:1},
    'listar_material': {0:1, 1:1},
    'listar_usuario': {0:1, 1:1},
    'listar_item': {0:1, 1:1},
    'listar_emprestimos': {0:1, 1:1},
    'excluir_usuario': {0:1, 1:1},
    'excluir_material': {0:1, 1:1},
    'excluir_item': {0:1, 1:1},
    'excluir_emprestimo': {0:1, 1:1},
    'atualizar_material': {0:1, 1:1},
    'atualizar_item': {0:1, 1:1},
    'adicionar_item': {0:1, 1:1}


}

@app.before_request
def autorizacao():
    acao = request.path[1:]
    acao = acao.split('/')
    if len(acao) >= 1:
        acao = acao[0]

    acoes = app.auth.keys()
    if acao in list(acoes):
        if session.get('logado') is None:
            return redirect(url_for('login'))
        else:
            tipo = session['logado']['tipo']
            if app.auth[acao][tipo] == 0:
                return redirect(url_for('painel'))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template("index.html")


# Usuarios

@app.route('/listar_usuario', methods=['GET', 'POST'])
def listar_usuario():
    dao = UsuarioDAO(get_db())
    usuarios_db = None
    usuario_db = None
    try:
        codigo = request.form['codigo']
        if codigo is not None:
            codigo = request.form['codigo']
            usuario_db = dao.listar(codigo)

    except:
        usuarios_db = dao.listar()

    return render_template("listar_usuario.html", usuarios=usuarios_db, usuario=usuario_db)


@app.route('/excluir_usuario/ <matricula>', methods=['GET', ])
def excluir_usuario(matricula):
    dao = UsuarioDAO(get_db())
    ret = dao.excluir(matricula)
    if ret == 1:
        flash(f"Usuario {matricula} excluído com sucesso!", "success")
    else:
        flash(f"Erro ao excluir usuario {matricula}", "danger")
    return redirect(url_for('listar_usuario'))



# Materiais

@app.route('/cadastrar_material', methods=['GET', 'POST'])
def cadastrar_material():
    if request.method == "POST":
        nome = request.form['nome']
        tipo = request.form['tipo']

        material = Material(nome, tipo)

        dao = MaterialDAO(get_db())
        codigo = dao.inserir(material)
        print(codigo)
        if codigo > 0:
            flash("Cadastrado com sucesso!", "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    vartitulo = "Cadastro de Material"
    return render_template("cadastrar_material.html", titulo=vartitulo)


@app.route('/listar_material', methods=['GET', 'POST'])
def listar_material():
    dao = MaterialDAO(get_db())
    try:
        nome = request.form['nome']
        if nome is not None:
            materiais_db = dao.listar(nome)
    except:
        materiais_db = dao.listar()

    return render_template("listar_material.html", materiais=materiais_db)



@app.route('/atualizar_material/<int:codigo>', methods=['GET', 'POST'])
def atualizar_material(codigo):
    dao = MaterialDAO(get_db())

    if request.method == "POST":
        nome = request.form['nome']
        tipo = request.form['tipo']

        material = Material(nome, tipo)
        material.setCodigo(codigo)
        ret = dao.atualizar(material)

        if codigo > 0:
            flash("Atualizado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao atualizar!", "danger")

    material_db = dao.listar(codigo)
    return render_template("atualizar_material.html", material=material_db)


@app.route('/excluir_material/ <codigo>', methods=['GET', ])
def excluir_material(codigo):
    dao = MaterialDAO(get_db())
    daoItem = ItemDAO(get_db())
    item = None
    daoItem.excluir(item, codigo)
    ret = dao.excluir(codigo)
    if ret == 1:
        flash(f"Material {codigo} excluído com sucesso!", "success")
    else:
        flash(f"Erro ao excluir material {codigo}", "danger")
    return redirect(url_for('listar_material'))




# Itens

@app.route('/listar_item', methods=['GET', 'POST'])
def listar_item():
    dao = ItemDAO(get_db())
    try:
        nome = request.form['nome']
        if nome is not None:
            nome = request.form['nome']
            itens_db = dao.listar(nome)
    except:
        itens_db = dao.listar()

    return render_template("listar_item.html", itens=itens_db)

@app.route('/cadastrar_item', methods=['GET', 'POST'])
def cadastrar_item():
    daoMaterial = MaterialDAO(get_db())

    if request.method == "POST":
        disponibilidade = request.form['disponibilidade']
        observacao = request.form['observacao']
        material = request.form['material']
        localizacao = request.form['localizacao']

        item = Item(disponibilidade, material, observacao, localizacao)

        dao = ItemDAO(get_db())
        codigo = dao.inserir(item)

        if codigo > 0:
            flash("Cadastrado com sucesso!", "success")
        else:
            flash("Erro ao cadastrar!", "danger")

    materiais_db = daoMaterial.listar()
    return render_template("cadastrar_item.html", materiais=materiais_db)

@app.route('/excluir_item/<codigo>', methods=['GET', ])
def excluir_item(codigo):
    dao = ItemDAO(get_db())
    ret = dao.excluir(codigo)
    if ret == 1:
        flash(f"Item {codigo} excluído com sucesso!", "success")
    else:
        flash(f"Erro ao excluir item {codigo}", "danger")
    return redirect(url_for('listar_item'))

@app.route('/atualizar_item/<int:codigo>', methods=['GET', 'POST'])
def atualizar_item(codigo):
    dao = ItemDAO(get_db())
    daoMaterial = MaterialDAO(get_db())
    materiais_db = daoMaterial.listar()

    if request.method == "POST":
        disponibilidade = request.form['disponibilidade']
        observacao = request.form['observacao']
        material = request.form['material']
        localizacao = request.form['localizacao']
        emprestimo = " "

        item = Item(disponibilidade, material, emprestimo, observacao, localizacao)

        dao = ItemDAO(get_db())

        item.setCodigo(codigo)
        ret = dao.atualizar(item)
        print(ret)

        if ret > 0:
            flash("Atualizado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao atualizar!", "danger")

    item_db = dao.listar(codigo)
    return render_template("atualizar_item.html", item=item_db, materiais=materiais_db)



# Empréstimos

@app.route('/listar_emprestimos', methods=['GET','POST'])
def listar_emprestimos():
    dao = EmprestimoDAO(get_db())
    try:
        data = request.form['data']
        if data is not None:
            emprestimos_db = dao.listar(data)
    except:
        emprestimos_db = dao.listar()
    return render_template("listar_emprestimos.html", emprestimos=emprestimos_db)


@app.route('/cadastrar_emprestimo', methods=['GET', 'POST'])
def cadastrar_emprestimo():
    daoUsuario = UsuarioDAO(get_db())
    daoMaterial = MaterialDAO(get_db())

    if request.method == "POST":
        tipo = request.form['tipo']
        dt_emp = request.form['dt_emp']
        usuario = request.form['usuario']
        dt_devolucao = request.form['dt_devolucao']

        emprestimo = Emprestimo(tipo, dt_emp, usuario, dt_devolucao)

        print(Emprestimo(tipo, dt_emp, usuario))

        daoEmprestimo = EmprestimoDAO(get_db())
        codigo = daoEmprestimo.inserir(emprestimo)
        print(codigo)
        if codigo > 0:
            flash("Emprestimo cadastrado com sucesso! Código %d" % codigo, "success")
        else:
            flash("Erro ao registrar emprestimo!", "danger")

    usuarios_db = daoUsuario.listar()
    materiais_db = daoMaterial.listar()
    return render_template("cadastrar_emprestimo.html",
                           usuarios=usuarios_db, materiais=materiais_db)

@app.route('/excluir_emprestimo/<codigo>', methods=['GET', ])
def excluir_emprestimo(codigo):
    dao = EmprestimoDAO(get_db())
    daoItem = ItemDAO(get_db())
    ret = dao.excluir(codigo)
    daoItem.devolver(codigo)
    item = dao.excluirItens(codigo)
    if ret == 0 and item == 0:
        flash(f"Erro ao excluir emprestimo {codigo}", "danger")
    else:
        flash(f"Emprestimo {codigo} excluído com sucesso!", "success")
    return redirect(url_for('listar_emprestimos'))


@app.route('/adicionar_item/<int:codigo>', methods=['GET', 'POST'])
def adicionar_item(codigo):

    if request.method == "POST":
        item = request.form['item']
        emprestimo = codigo

        dao = ItemDAO(get_db())
        item = Emprestimo_has_item(emprestimo, item)

        ret = dao.verificar_item(item.item)
        print(ret)

        if ret is not None:
            flash("Erro ao adicionar item!", "danger")
        else:
            dao.adicionar_item(item)
            flash("Item adicionado com sucesso!", "success")

    daoItem = ItemDAO(get_db())
    itens_db = daoItem.listar()
    return render_template('adicionar_item.html', itens=itens_db, emprestimo=codigo)


@app.route('/devolver_itens/<int:codigo>', methods=['GET', 'POST'])
def devolver_itens(codigo):
    daoItem = ItemDAO(get_db())
    daoItem.devolver(codigo)
    dao = EmprestimoDAO(get_db())
    data = date.today()
    print(data)
    ret = dao.devolver(codigo, data)
    if ret > 0:
        flash("Itens devolvidos! Código %d" % codigo, "success")
    else:
        flash("Erro!", "danger")
    return redirect(url_for('listar_emprestimos'))

@app.route('/renovar_emprestimo/<int:codigo>', methods=['GET', 'POST'])
def renovar_emprestimo(codigo):
    dao = EmprestimoDAO(get_db())
    if request.method == "POST":
        data = request.form['data']
        print(data)
        ret = dao.devolver(codigo, data)
        if ret > 0:
            flash("Itens devolvidos! Código %d" % codigo, "success")
        else:
            flash("Erro!", "danger")
        emprestimo_db = dao.devolver(codigo, data)

    return render_template("renovar_emprestimo.html", emprestimo=emprestimo_db)



@app.route('/visualizar_emprestimo/<int:codigo>', methods=['GET', 'POST'])
def visualizar_emprestimo(codigo):
    dao = EmprestimoDAO(get_db())
    emprestimo_db = dao.listar(codigo)
    print(emprestimo_db)
    daoItem = ItemDAO(get_db())
    itens_db = daoItem.listar_itens(codigo)
    print(itens_db)
    return render_template("visualizar_emprestimo.html", emprestimo=emprestimo_db, itens=itens_db)




# Login/logout

@app.route('/login', methods=['GET', 'POST'])
def login():
    output = ""
    if request.method == "POST":
        matricula = request.form['matricula']
        senha = request.form['senha']
        api = Suap()
        usuario = api.autentica(matricula, senha)

        if usuario is not None:
            user = api.getMeusDados(usuario)
            tipo = 1
            if user['tipo_vinculo'] == 'Aluno':
                tipo = 0


            dao = UsuarioDAO(get_db())
            usuario = dao.autenticar(matricula, senha)
            print(user)

            if usuario is None:
                matricula = matricula
                nome = user['nome_usual']
                email = user['email']
                senha = 'senha'

                usuario = Usuario(matricula, senha, nome, email, tipo)
                codigo = dao.inserir(usuario)


            session['logado'] = {
                'matricula': user['matricula'],
                'nome': user['nome_usual'],
                'email': user['email'],
                'tipo': tipo
            }
            output = "<pre>" + str(user) + "</pre>"

            return redirect(url_for('painel'))
        else:
            output = "Erro"
            flash("Erro ao efetuar login!", "danger")


    print(output)
    return render_template("login.html", titulo="Login")


@app.route('/logout')
def logout():
    session['logado'] = None
    session.clear()
    return redirect(url_for('index'))


@app.route('/painel')
def painel():
    return render_template("painel.html", titulo="Painel")


if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)