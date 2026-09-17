from flask import Flask
app = Flask(__name__)

#Rotas
@app.route("/")
def ola_mundo():
    return "Salve dev !"

#Execução
app.run(debug=True)