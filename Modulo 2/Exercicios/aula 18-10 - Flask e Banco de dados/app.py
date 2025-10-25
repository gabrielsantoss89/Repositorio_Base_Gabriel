from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conta')
def conta():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    n3 = int(request.args.get('valor3',0))

    conta = n1 + n2 + n3
    
    return{
        
        'Numero 1': n1,
        'Numero 2': n2,
        'Numero 3': n3,
        'Soma de 3 numeros': conta
    }
    
@app.route('/desconto')
def desconto():
    return render_template('desconto.html')
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)


