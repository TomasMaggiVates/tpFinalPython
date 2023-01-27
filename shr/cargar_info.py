# para manejar los jsons a leer
import json

# objetos donde meter toda la info de los jsons
from classes.class_continente import Continente
from classes.class_pais import Pais

DEFAULT_IN = 'in/'
DEFAULT_OUT = 'out/'


def find_pais(p_pais: str, d: dict) -> dict:
    '''
        buscamos el continente al que pertenece el pais dado
    '''
    for c, p in d.items():
        for k, v in p.items():
            if k == p_pais:
                return c, k
    return 'Desconocido', p_pais


def print_info(d: dict) -> None:
    '''
        imprimimos de forma amigable al usuario el diccionario con la info obtenida de los
        jsons
    '''
    for continente in d.keys():
        print(continente)
        for k, v in d[continente].items():
            print(f"* {k}{v}")

        print('-----------------------------')


def parse_jsons() -> dict:
    '''
        leemos cada json y devolvemos un diccionario con toda la info necesaria para crear los objetos
    '''

    # categoria desconocido se usa para guardar paises de los cuales no se conoce continente
    # solo se contabilizan con las categorias que posean
    d = {'Desconocido': {}}

    with open(DEFAULT_IN + 'country-by-continent.json', 'r') as f:
        l = json.load(f)

        for i in l:
            # intentamos meter el nombre del pais como key de diccionario para luego meter el resto de infomacion
            # en el value
            try:
                d[i['continent']][i['country']] = {}
            # deberia saltar una excepcion si es la primera vez que agregamos un dict pais al continente asique
            # aqui asignamos primero el dict al v continente y despues el pais
            except:
                d[i['continent']] = {}
                d[i['continent']][i['country']] = {}

    archivos = ['country-by-currency-code.json',
                'country-by-languages.json',
                'country-by-population.json']

    keys = ['currency_code',
            'languages',
            'population']

    for archivo, key in zip(archivos, keys):
        with open(DEFAULT_IN + archivo, 'r') as f:
            l = json.load(f)
            for i in l:
                continente, pais = find_pais(i['country'], d)
                try:
                    d[continente][pais][key] = i[key]
                except:
                    d[continente][pais] = {}
                    d[continente][pais][key] = i[key]
    return d


def cargar_paises(d: dict) -> list[Continente]:
    '''
        utilizamos los datos en el diccionario para crear los paises con su respectiva informacion y los
        asignamos a un objeto continente
    '''
    continentes = {}

    for continente, paises in d.items():
        l = []
        for pais, info in paises.items():
            p = Pais(pais)
            try:
                p.currency_code = info['currency_code']
            except:
                p.currency_code = None
            try:
                p.languages = info['languages']
            except:
                p.languages = None
            try:
                p.population = info['population']
            except:
                p.population = None
            l.append(p)
        c = Continente(l)
        # print(c)
        continentes[continente] = c

    return continentes


def guardar(l: list) -> None:
    '''
        guardamos las respuestas en un json
    '''
    with open(DEFAULT_OUT + 'respuestas.json', 'w') as f:
        json.dump(l, f)
