
BP_TOTAL_PRESTIGIO_100 = 150_000_000 
LIMITE_MAXIMO_DE_NIVEL = 50   
PRESTIGIO_MAXIMO = 100 
BP_PUNTOS_POR_PRESTIGIO = 1_500_000 

def calcular_puntos_faltantes(prestigio_deseado, bp):
    """Calcula los puntos BP faltantes para alcanzar el prestigio deseado."""
    total_requerido = prestigio_deseado * BP_PUNTOS_POR_PRESTIGIO
    bp_faltantes = total_requerido - bp
    return bp_faltantes

def calcular_puntos_gastados(prestigio_actual, nivel_actual):
    """Calcula los puntos BP gastados según el prestigio y nivel actual."""
    costo_por_nivel = BP_PUNTOS_POR_PRESTIGIO / LIMITE_MAXIMO_DE_NIVEL
    puntos_actuales_gastados = (nivel_actual - 1) * costo_por_nivel
    puntos_gastados_en_total = (prestigio_actual * BP_PUNTOS_POR_PRESTIGIO)\
    + puntos_actuales_gastados
    return puntos_actuales_gastados, puntos_gastados_en_total

def obtener_datos ():
    """Solicita al usuario los datos necesarios para el cálculo."""
    prestigio_deseado = -1
    while not (0 <= prestigio_deseado <= PRESTIGIO_MAXIMO):
        try:
            prestigio_deseado = float(input\
            ("Ingrese su prestigio deseado (0-100): "))
            if not (0 <= prestigio_deseado <= PRESTIGIO_MAXIMO):
                print("El prestigio deseado debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    prestigio_actual = -1
    while not (0 <= prestigio_actual <= prestigio_deseado):
        try:
            prestigio_actual = float(input\
            (f"Ingrese su prestigio actual (0-{prestigio_deseado}): "))
            if prestigio_actual < 0: 
                print("El prestigio actual no puede ser negativo.")
            elif prestigio_actual > prestigio_deseado:
                print(
                f"El prestigio actual no puede ser mayor({prestigio_deseado})"
                )
        except ValueError:
            print("Por favor, ingrese un número válido.")
    nivel_actual = 0 
    while not (1 <= nivel_actual <= LIMITE_MAXIMO_DE_NIVEL):
        try:
            nivel_actual = float(
                input(f"Ingrese su nivel actual(1-{LIMITE_MAXIMO_DE_NIVEL})")
                                 )
            if not (1 <= nivel_actual <= LIMITE_MAXIMO_DE_NIVEL):
                print(
                f"El nivel debe estar entre 1 y{LIMITE_MAXIMO_DE_NIVEL}.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    bp = -1
    while bp < 0:
        try:
            bp = float(input("Ingrese los BP que tiene actualmente: "))
            if bp < 0:
                print("Los BP disponibles no pueden ser negativos.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return {
       "prestigio_deseado": prestigio_deseado,
        "prestigio_actual": prestigio_actual,
        "nivel_actual": nivel_actual,
        "bp_disponibles": bp
    }
MATRIZ_DE_DATOS = [
    {"prestigio_deseado": 25,
      "prestigio_actual": 1,
      "nivel_actual": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 50,
      "prestigio_actual": 1,
      "nivel_actual": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 75,
      "prestigio_actual": 1,
      "nivel_actual": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 100,
      "prestigio_actual": 1,
      "nivel_actual": 1,
      "bp_disponibles": 250000000
      }
]
def main():
    """Función principal que controla el flujo del programa."""
    fuente_datos = ""
    while fuente_datos not in ["M", "A"]:
        print("\nSeleccione la fuente de datos:")
        fuente_datos = input(
        "Escriba 'M' (manual) o 'A' (automática):"
        ).upper()
        if fuente_datos not in ["M", "A"]:
            print("Entrada no válida, intente de nuevo.")
    resultados = []
    if fuente_datos == "A":
        print(
            f"\nUsando datos de la matriz predefinida\
            con {len(MATRIZ_DE_DATOS)} personajes."
        )
        datos_a_calcular = MATRIZ_DE_DATOS
    else:
        num_personajes = 0
        while num_personajes <= 0:
            try:
                num_personajes = int(
                    input("\n¿Cuántos personajes desea calcular?: ")
                )
                if num_personajes <= 0:
                    print("Ingrese un número positivo.")
            except ValueError:
                print("Entrada no válida.")
        datos_a_calcular =\
        [obtener_datos() for _ in range(num_personajes)]

    for indice, datos in enumerate(datos_a_calcular, start=1):
        bp_faltantes = calcular_puntos_faltantes(
            datos["prestigio_deseado"], datos["bp_disponibles"]
        )
        _, puntos_gastados_total = calcular_puntos_gastados(
            datos["prestigio_actual"], datos["nivel_actual"]
        )
        resultados.append(
            {
                "calculo": indice,
                "prestigio_deseado": datos["prestigio_deseado"],
                "prestigio_actual": datos["prestigio_actual"],
                "bp_faltantes": bp_faltantes,
                "bp_gastados_total": puntos_gastados_total,
            }
        )

    print("\n" + "=" * 50)
    print("Resultados:")
    print("=" * 50)

    for r in resultados:
        print(f"\nResultados personaje #{r['calculo']}:")
        print(
            f"  Prestigio deseado: P{r['prestigio_deseado']:.0f} "
            f"(desde P{r['prestigio_actual']:.0f})"
        )
        print(f"  Puntos faltantes: {r['bp_faltantes']:,.2f}")
        print(f"  Puntos gastados totales: {r['bp_gastados_total']:,.2f}")


if __name__ == "__main__":
    main()