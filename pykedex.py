import requests
from flask import Flask, render_template, request, redirect, session, flash, url_for


app = Flask(__name__)
app.secret_key = 'flask'



class Star:
    def __init__(self, films, name, url):
        self.url = url
        self.name = name
        self.films = films


class Filme:
    def __init__(self, title, characters, starships):
        self.title = title
        self.characters = characters
        self.starships = starships




class Treinadora:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


retorno = []



@app.route('/')
def index():
    retorno = session['objeto']
    categoriaObjeto = session['categoria']
    
    if categoriaObjeto == 'films':
        retorno2 = Filme(retorno['title'], listarNomeCharacters(retorno['characters']), listarNomeStarships(retorno['starships']))
    
    else:
        retorno2 = Star(listarNomeFilmes(retorno['films']), retorno['name'], retorno['url'])
    

    return render_template('lista.html', titulo='Faça sua Consulta', informacao=retorno2)
    



@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:

        return render_template('login.html', titulo='Nova Consulta')


def listarNomeFilmes(listaUrl):
    lista_filmes = []
    for url in listaUrl:
        requestFilme = requests.get(url)
        filme = requestFilme.json()
        lista_filmes.append(filme['title'])
    return lista_filmes

def listarNomeCharacters(listaUrl):
    lista_characters = []
    for url in listaUrl:
        requestCharacter = requests.get(url)
        personagens = requestCharacter.json()
        lista_characters.append(personagens['name'])
    return lista_characters

def listarNomeStarships(listaUrl):
    lista_starships = []
    for url in listaUrl:
        requestStarships = requests.get(url)
        naves = requestStarships.json()
        lista_starships.append(naves['name'])
    return lista_starships


@app.route('/autenticar', methods=['POST', ])
def autenticar():

    request1 = requests.get('https://swapi.dev/api/{0}/{1}/'.format(request.form['categoria'], request.form['id']))
    
    session['objeto'] = request1.json()
    session['categoria'] = request.form['categoria']
    return redirect(url_for('index'))
    '''option = int(input('Deseja realizar uma nova consulta?\n1. Sim.\n2. Sair.\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')'''


app.run(debug=True)
