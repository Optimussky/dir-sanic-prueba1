#app.py
from sanic_ext import render
from sanic import Sanic

from sanic.response import json
from jinja2 import Environment, FileSystemLoader
from sanic import Sanic, response
import mysql.connector

app = Sanic(__name__)

# Configuración de la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'D354rr0ll0f4t1g4',
    'database': 'dbfatiga'
}

# Función para establecer la conexión con la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta para mostrar la lista de elementos (Read)
@app.route('/')
async def index(request):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT idUsuario,nombre,usuario FROM tbUsuario')
    items = cursor.fetchall()
    conn.close()
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")
    rendered_template = template.render(items=items)

    return response.html(rendered_template)
    #return response.html(render_template("index.html", items=items))

    


# Función para renderizar plantillas
def render_template(template_name, **context):
    with open(template_name, 'r') as template_file:
        
        template_content = template_file.read()
        for x in template_content:
            print(x)
    return template_content.format(**context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8900)
