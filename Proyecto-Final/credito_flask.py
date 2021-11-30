from flask import Flask, render_template, request
import controlador_credito as controlador

app = Flask(__name__)


@app.route('/')
def index():
    titulo = "Usuarios Inicio"
    usuarios = controlador.get_usuarios()
    return render_template("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/panel/')
def panel(msg=""):
    titulo = "Usuarios - Panel"
    return render_template("panel.html", titulo=titulo, msg=msg)

@app.route('/usuarios/<string:accion>')
def productos_lista(accion):
    titulo = "Usuarios"
    usuarios = controlador.get_usuarios()
    
    return render_template('usuarios.html',
                           titulo = titulo,
                           accion = accion,
                           usuarios = usuarios
                          )

@app.route('/usuarios/<string:accion>')
def usuarios_lista(accion):
    titulo = "Productos"
    usuarios = controlador.get_usuarios()
    
    return render_template('usuarios.html',
                           titulo = titulo,
                           accion = accion,
                           usuarios = usuarios
                          )

@app.route('/usuario/adicionar/', methods=['GET', 'POST'])
def usuario_adicionar():
    titulo = "Usuarios - Adicionar"
    if request.method == "POST":
        nombre = request.form["nombre"]
        if controlador.add_usuario(nombre) :
        # return para el método POST
            return panel(msg="El usuario se adicionó de forma correcta!")
        else :
            return panel(msg=f"El usuario: {nombre}, ya existe!")
    # return para el método GET
    return render_template("usuario-adicionar.html", titulo=titulo)

@app.route('/usuario/eliminar/<string:nombre_>/', methods=['GET', 'POST'])
def usuario_eliminar(nombre_):
    titulo = "Usuarios - Eliminar"
    usuario = controlador.get_usuario(nombre_)
    if request.method == "POST":
        controlador.del_usuario(nombre_)
        return panel(msg=f"El usuario: {nombre_}, fue eliminado!")
    # return para el método GET
    return render_template("usuario-eliminar.html", titulo=titulo, usuario = usuario)

@app.route('/usuario/reporte/<string:nombre_>/')
def usuario_reporte(nombre_):
    titulo = "Usuarios - Reporte"
    usuario = controlador.get_usuario(nombre_)
    # return para el método GET
    return render_template("usuario-reporte.html", titulo=titulo, usuario=usuario)

@app.route('/usuario/tarjetas/<string:nombre_>/')
def usuario_tarjetas(nombre_):
    titulo = "Usuarios - Tarjetas"
    usuario = controlador.get_usuario(nombre_)
    # return para el método GET
    return render_template("usuario-tarjetas.html", titulo=titulo, usuario=usuario)

@app.route('/usuario/tarjeta-adicionar/<string:nombre_>/', methods=['GET', 'POST'])
def tarjeta_adicionar(nombre_):
    titulo = "Tarjetas - Adicionar"
    usuario = controlador.get_usuario(nombre_)
    if request.method == "POST":
        nombre_usuario = request.form["nombre-usuario"]
        nombre = request.form["nombre"]
        interes_anual = float(request.form["interes-anual"])
        deuda = float(request.form["deuda"])
        pago = float(request.form["pago"])
        cargo = float(request.form["cargo"])
        controlador.add_tarjeta_usuario(nombre_usuario,nombre,deuda,interes_anual,pago,cargo)
        return panel(msg=f"La tarjeta: {nombre}, fue adicionada al usuario: {nombre_usuario}!")
    # return para el método GET
    return render_template("tarjeta-adicionar.html", titulo=titulo, usuario=usuario)

@app.route('/usuario/tarjeta-eliminar/<string:usuario_>/<string:tarjeta_>/', methods=['GET', 'POST'])
def tarjeta_eliminar(usuario_, tarjeta_):
    titulo = "Tarjetas - Eliminar"
    tarjeta = controlador.get_tarjeta(usuario_,tarjeta_)
    if request.method == "POST":
        controlador.del_tarjeta_usuario(usuario_, tarjeta_)
        return panel(msg=f"La tarjeta: {tarjeta_}, fue eliminada al usuario: {usuario_}!")
    # return para el método GET
    return render_template("tarjeta-eliminar.html", titulo=titulo, usuario=usuario_, tarjeta = tarjeta)


if __name__ == "__main__":
    controlador.inicializa_bd()
    app.run(debug=True, host="0.0.0.0")    