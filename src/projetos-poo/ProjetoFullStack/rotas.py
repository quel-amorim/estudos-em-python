from flask import Flask , url_for , render_template
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('\principal.html')

app.run(debug=True)