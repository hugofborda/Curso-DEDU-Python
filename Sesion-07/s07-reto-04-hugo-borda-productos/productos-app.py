from flask import Flask
from flask import render_template
from flask import request
import productos

app = Flask(__name__)

@app.route('/')
def index():
    titulo = "Productos Inicio"
    productos_lista = productos.lista_productos()
    return render_template("index.html", titulo=titulo, productos=productos_lista)
 
@app.route('/panel/')
def panel(msg=""):
    titulo = "Productos - Panel"
    return render_template("panel.html", titulo=titulo, msg=msg)

@app.route('/producto/alta/', methods=['GET', 'POST'])
def producto_alta():
    titulo = "Productos - Alta"
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        descripcion = request.form["descripcion"]
        productos.alta(nombre, precio, descripcion)
        # return para el método POST
        return panel(msg="El producto se dió de alta de forma correcta!")

    # return para el método GET
    return render_template("producto-alta.html", titulo=titulo)

@app.route('/productos/<string:accion>')
def productos_lista(accion):
    titulo = "Productos"
    productos_lista = productos.lista_productos()
    
    return render_template('productos.html',
                           titulo = titulo,
                           accion = accion,
                           productos = productos_lista
                          )

@app.route('/producto/modificar/<int:id_>/', methods=['GET', 'POST'])
def producto_modificar(id_):
    titulo = "Producto Modificar"
    productos_lista = productos.lista_productos()
    for producto in productos_lista:
        if producto["id"] == id_:
            break
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        descripcion = request.form["descripcion"]
        productos.modificar(id_, nombre, precio, descripcion)
        
        return panel("Producto modificado con éxito!")
    return render_template('producto-modificar.html',
                           titulo = titulo,
                           producto = producto
                          )

@app.route('/producto/eliminar/<int:id_>/', methods=['GET', 'POST'])
def producto_eliminar(id_):
    titulo = "Producto Eliminar"
    productos_lista = productos.lista_productos()
    for producto in productos_lista:
        if producto["id"] == id_:
            break
    if request.method == "POST":
        productos.baja(id_)
        
        return panel("Producto dado de baja con éxito!")
    return render_template('producto-baja.html',
                           titulo = titulo,
                           producto = producto
                          )    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

