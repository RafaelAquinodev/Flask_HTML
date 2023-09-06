from flask import Flask, render_template, request #importar a biblioteca flask e o modulo dentro dela.


app = Flask(__name__) #Definir o nome do aplicativo, chama o Flask e passa um parametro

times = []
registros = []

@app.route('/') #criando uma rota, através do método route.
def index(): #definindo uma função
    nome = "Rafael"
    idade = 23
    return render_template("index.html", nome=nome, idade=idade) #passando as variaveis como parametro.

@app.route('/futebol', methods=["GET", "POST"])
def futebol():
    #times = ["Vasco", "Flamengo", "Botafogo", "Fluminense", "Palmeiras", "Santos","Sao Paulo", "Cruzeiro"]
    
    if request.method == "POST":
        if request.form.get("time"):
            times.append(request.form.get("time"))
    return render_template("sobre.html", times=times)

@app.route('/alunos', methods=["GET","POST"])
def nota():
    # alunos = {"Rafael": 5.0, "Thiago": 8.0, "Joao":9.0}
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("notas"):
            registros.append({"aluno":request.form.get("aluno"),"notas":request.form.get("notas")})

    return render_template("notas.html", registros=registros)


if __name__ == '__main__':
    app.run(debug=True)






