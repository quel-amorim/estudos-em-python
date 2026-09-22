import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for
load_dotenv()

app = Flask(__name__)

# Pega a chave definida no arquivo .env
app.secret_key = os.getenv("FLASK_SECRET_KEY")

class Calculadora:
    @staticmethod
    def somar(n1, n2):
        return n1 + n2

    @staticmethod
    def diminuir(n1, n2):
        return n1 - n2

    @staticmethod
    def multiplicar(n1, n2):
        return n1 * n2

    @staticmethod
    def dividir(n1, n2):
        if n2 == 0:
            return "Erro: Divisão por zero!"
        return n1 / n2


@app.route("/", methods=["GET", "POST"])
def index():
    # Inicializa o histórico na sessão se não existir
    if "historico" not in session:
        session["historico"] = []

    resultado = None
    erro = None
    n1 = ""
    n2 = ""

    if request.method == "POST":
        # Ação do formulário (Calcular, Limpar Histórico, etc.)
        acao = request.form.get("operacao")

        if acao == "limpar_historico":
            session["historico"] = []
            return redirect(url_for("index"))

        try:
            n1 = float(request.form.get("n1", 0))
            n2 = float(request.form.get("n2", 0))

            historico_atual = session["historico"]

            if acao == "somar":
                res = Calculadora.somar(n1, n2)
                resultado = f"{n1} + {n2} = {res}"
                historico_atual.append(resultado)

            elif acao == "diminuir":
                res = Calculadora.diminuir(n1, n2)
                resultado = f"{n1} - {n2} = {res}"
                historico_atual.append(resultado)

            elif acao == "multiplicar":
                res = Calculadora.multiplicar(n1, n2)
                resultado = f"{n1} * {n2} = {res}"
                historico_atual.append(resultado)

            elif acao == "dividir":
                res = Calculadora.dividir(n1, n2)
                if isinstance(res, str):  # Se for mensagem de erro
                    erro = res
                else:
                    resultado = f"{n1} / {n2} = {res}"
                    historico_atual.append(resultado)

            elif acao == "todas":
                operacoes = [
                    (n1 + n2, "+"),
                    (n1 - n2, "-"),
                    (n1 * n2, "*"),
                    (Calculadora.dividir(n1, n2), "/"),
                ]
                resultados_todas = []
                for res, op in operacoes:
                    if isinstance(res, str):
                        item = f"{n1} {op} {n2} = {res}"
                    else:
                        item = f"{n1} {op} {n2} = {res}"
                    resultados_todas.append(item)
                    historico_atual.append(item)
                resultado = " | ".join(resultados_todas)

            # Atualiza a sessão
            session["historico"] = historico_atual

        except ValueError:
            erro = "Valor incorreto! Digite apenas números."

    return render_template(
        "calculadora.html",
        resultado=resultado,
        erro=erro,
        n1=n1,
        n2=n2,
        historico=session.get("historico", [])
    )


if __name__ == "__main__":
    app.run(debug=True)