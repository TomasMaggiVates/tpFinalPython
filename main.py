from shr.cargar_info import parse_jsons, cargar_paises, print_info, guardar
from shr.tabular_datos import mayor_poblacion, idioma_mas_hablado, moneda_mas_usada


def main():
    # leemos el json y cargamos la info en un diccionario
    d = parse_jsons()

    # simple log para corroborar la informacion
    print_info(d)

    # convertimos la info en el dict en una lista que contenga obj del tipo continente que a su vez contienen
    # una lista con obj del tipo pais, cada unos con sus metodos de ayuda para ciertas operaciones
    c = cargar_paises(d)

    # obtenemos el continente con mayor poblacion
    r1 = mayor_poblacion(c)

    # obtenemos el idioma mas hablado del mundo y por continente
    r2 = idioma_mas_hablado(c)

    # obtenemos la moneda mas usada del mundo
    r3 = moneda_mas_usada(c)

    # colocamos los dict con las respuestas en una lista y la guardamos en el almacenamiento como un json
    guardar([r1, r2, r3])


if __name__ == "__main__":
    main()
