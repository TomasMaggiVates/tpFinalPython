class Pais:
    def __init__(self, nombre) -> None:
        self.name = nombre
        self.currency_code = ''
        self.languages = []
        self.population = 0

    # esto nos permite ver de forma mas amigable para el usuario la info dentro del objeto cuando
    # queremos imprimirla en la consola
    def __str__(self) -> str:
        return f"nombre: {self.name}\n\
moneda: {self.currency_code}\n\
idiomas: {self.languages}\n\
poblacion: {self.population}\n"

    def get_proporcion_idiomas(self):
        '''
            devuelve un diccionario con cada idioma hablado y su numero proporcional de hablantes
        '''
        d = {}

        # dividimos el total de la poblacion por la cantidad de lenguas porque suponemos que
        # todas las lenguas se hablan en la misma proporcion
        try:
            proporcion = self.population / len(self.languages)
            for lengua in self.languages:
                d[lengua] = proporcion
        # en caso de que no haya poblacion o idiomas cargados el pais no se contabiliza
        except:
            d = {'': 0}
        return d
