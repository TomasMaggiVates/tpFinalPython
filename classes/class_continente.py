from classes.class_pais import Pais


class Continente:
    def __init__(self, paises: list[Pais] = []):
        self.paises = paises

    # esto nos permite ver de forma mas amigable para el usuario la info dentro del objeto cuando
    # queremos imprimirla en la consola
    def __str__(self) -> str:
        s = ''
        for pais in self.paises:
            s += str(pais)
        return s

    def get_poblacion(self) -> int:
        counter = 0
        for pais in self.paises:
            try:
                counter += pais.population
            except:
                continue
        return counter

    def get_idioma_mas_hablado(self):
        '''
            devuelve el idioma mas hablado del continente
        '''
        idiomas = {}

        for pais in self.paises:
            try:
                d = pais.get_proporcion_idiomas()
                for idioma, cantidad in d.items():
                    try:
                        idiomas[idioma] += cantidad
                    except:
                        idiomas[idioma] = 0
                        idiomas[idioma] += cantidad
            except:
                continue

        m_counter = 0
        m_idioma = ''

        for k, v in idiomas.items():
            if v > m_counter:
                m_counter = v
                m_idioma = k

        return {m_idioma: m_counter}
