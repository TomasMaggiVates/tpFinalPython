def mayor_poblacion(d: dict) -> dict:
    '''
        iteramos sobre el diccionario de continentes para localizar al que tenga
        mayor poblacion, la categoria [Desconocido] no se contabiliza en esta ocasion
    '''
    continente = ''
    poblacion = 0

    for nombre, objeto in d.items():

        # en caso de que no sepamos el contiente del pais este no se computa
        if nombre == 'Desconocido':
            continue

        if objeto.get_poblacion() > poblacion:
            continente = nombre
            poblacion = objeto.get_poblacion()

    return {
        'respuesta1': {
            'mayor_poblacion': continente,
            'numero': poblacion
        }
    }


def idioma_mas_hablado(d: dict) -> dict:
    '''
        iteramos sobre el idioma de cada pais para obtener el mas hablado en todo el mundo y 
        por continente, solo en el primer caso tambien tenemos en cuenta a [Desconocido]
    '''
    r = {}

    # guardamos todos los idiomas y la cantidad de hablantes en el diccionario para luego
    # consultar cual es el mas hablado de todo el mundo
    idiomas = {}

    for continente in d.values():
        for pais in continente.paises:
            for k, v in pais.get_proporcion_idiomas().items():
                try:
                    idiomas[k] += v
                except:
                    idiomas[k] = 0
                    idiomas[k] += v
    m_counter = 0
    m_idioma = ''

    # buscamos en el diccionario de idiomas el mas hablado
    for k, v in idiomas.items():
        if v > m_counter:
            m_counter = v
            m_idioma = k

    r = {
        'respuesta2': {
            'World': m_idioma
        }
    }

    for nombre_continente, continente in d.items():

        # el continente desconocido no se contabiliza
        if nombre_continente == 'Desconocido':
            continue

        cant = continente.get_idioma_mas_hablado()

        # si el numero de hablantes es 0 hay algun error con la informacion provista
        r['respuesta2'][nombre_continente] = list(cant.keys())[0] if list(
            cant.values())[0] != 0 else 'datos insuficientes'

    return r


def moneda_mas_usada(d: dict) -> dict:
    '''
        iteramos sobre cada pais y obtenemos la moneda mas usada en todo el mundo
    '''

    monedas = {}
    for continente in d.values():
        for pais in continente.paises:

            # no hay info sobre la moneda del pais, asique pasamos al siguiente
            if pais.currency_code == None:
                continue
            else:
                try:
                    monedas[pais.currency_code] += 1
                except:
                    monedas[pais.currency_code] = 1

    m_cantidad = 0
    m_moneda = ''

    for k, v in monedas.items():
        if v > m_cantidad:
            m_cantidad = v
            m_moneda = k

    return {
        'respuesta3': {
            'moneda mas usada': m_moneda,
            'cant_paises': m_cantidad
        }
    }
