#app.py
from sanic import Sanic
from sanic.response import json

app = Sanic("Welcome Home")

@app.route('/')
async def hello_world(request):
    return json({'message': 'Welcome Home'})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8900)
