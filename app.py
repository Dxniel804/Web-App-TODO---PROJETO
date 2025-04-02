import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []
file_path = 'tarefas.csv'

def ler_csv(file_path):
    tarefas.clear()
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Pular cabeçalho 
            for row in reader:
                if row:
                    tarefas.append({"Titulo": row[0], "Descrição": row[1]})
    except FileNotFoundError:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Titulo", "Descrição"])

def escrever_csv(file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titulo", "Descrição"])
        for tarefa in tarefas:
            writer.writerow([tarefa["Titulo"], tarefa["Descrição"]])

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/tarefas')
def listar_tarefas():
    ler_csv(file_path)  # Recarrega os dados do CSV
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/add_tarefa', methods=['POST'])
def add_tarefa():
    titulo = request.form.get('titulo')
    descricao = request.form.get('descricao')
    
    if titulo and descricao:
        new_tarefa = {"Titulo": titulo, "Descrição": descricao}
        tarefas.append(new_tarefa)
        escrever_csv(file_path)  # Atualiza o CSV
    
    return redirect(url_for('listar_tarefas'))

@app.route('/add_tarefa_form')
def add_tarefa_form():
    return render_template('addTarefa.html')

@app.route('/del_tarefa')
def del_tarefa():
    ler_csv(file_path)  # Recarrega os dados antes de exibir a página
    return render_template('del_tarefa.html', tarefas=tarefas)

@app.route('/excluir_tarefa', methods=['POST'])
def excluir_tarefa():
    titulo = request.form.get('titulo')
    
    if titulo:
        global tarefas
        tarefas = [tarefa for tarefa in tarefas if tarefa["Titulo"] != titulo]
        escrever_csv(file_path)  # Atualiza o CSV
    
    return redirect(url_for('listar_tarefas'))

@app.route('/editar_tarefa', methods=['POST'])
def editar_tarefa():
    titulo = request.form.get('titulo')
    new_desc = request.form.get('nova_descricao')
    
    if titulo and new_desc:
        for tarefa in tarefas:
            if tarefa["Titulo"] == titulo:
                tarefa["Descrição"] = new_desc
                escrever_csv(file_path)
    
    return redirect(url_for('listar_tarefas'))

if __name__ == "__main__":
    ler_csv(file_path)  # Garante que o CSV seja lido ao iniciar o servidor
    app.run(debug=True, host="0.0.0.0")
