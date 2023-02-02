from shr.cargar_info import parse_jsons, cargar_paises, print_info, guardar
from shr.tabular_datos import mayor_poblacion, idioma_mas_hablado, moneda_mas_usada


def main() -> None:
    # leemos el json y cargamos la info en un diccionario
    info = parse_jsons()

    # simple log para corroborar la informacion
    print_info(info)

    # convertimos la info en el dict en una lista que contenga obj del tipo continente que a su vez contienen
    # una lista con obj del tipo pais, cada unos con sus metodos de ayuda para ciertas operaciones
    containerDeContinente = cargar_paises(info)

    # obtenemos el continente con mayor poblacion
    r1 = mayor_poblacion(containerDeContinente)

    # obtenemos el idioma mas hablado del mundo y por continente
    r2 = idioma_mas_hablado(containerDeContinente)

    # obtenemos la moneda mas usada del mundo
    r3 = moneda_mas_usada(containerDeContinente)

    # colocamos los dict con las respuestas en una lista y la guardamos en el almacenamiento como un json
    guardar([r1, r2, r3])


# chekqueamos que estemos en el punto de entrada del programa
if __name__ == "__main__":
    main()
