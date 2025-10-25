from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def home():
   return '<center><h1>Aula Criação de API</h1></center>'

@app.route('/api')
def teste():
    return jsonify(mensagem="esta mensagem indica que a sua API funcionou")

@app.route('/api/<cliente>', methods= ['GET'])
def nome(cliente):
    return jsonify(mensagem2=f'Oi {cliente}')
    
@app.route('/saudacao/<idioma>/<nome>', methods=['get'])
def saudacao(idioma, nome):
    mensagens = {
        'pt':'bom dia',
        'en':'good morning',
        'fr':'bonjour',
        'it':'buongiorno',
        'es':'buenos dias',
        'de':'guten morgen',
    }
    mensagens = mensagens.get(idioma)
    return jsonify(mensagens=f'{mensagens}, {nome}')

pedidos = [
    
    {'id':1,'cliente':'Gabriel','prato':'Hamburguer','status':'aguardando'},
    {'id':1,'cliente':'Fernando','prato':'Pizza','status':'aguardando'},
]


proximo_id= 3

@app.route('/pedidos', methods=['POST'])
def novospedidos():
    global proximo_id
    novo_pedido = request.json
    novo_pedido_molde = {
        'id': proximo_id,
        'cliente': novo_pedido['cliente'],
        'prato': novo_pedido['prato'],
        'status': 'aguardando'
    }

    pedidos.append(novo_pedido_molde)
    proximo_id += 1 
    
    return jsonify(novo_pedido_molde)

@app.route('/pedidos', methods=['GET'])
def verpedidos():
    return jsonify(pedidos)

if __name__ == '__main__':
    app.run (debug=True)
    
