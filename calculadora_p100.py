#Definicion de terminos 

P100BP = 150000000  #cantidad de puntos requeridos para max
LVM = 50  #cantidad de niveles por prestigio 
PMAX = 100 #cantidad de prestigios 
BPPP = 1500000 #cantidad de puntos para 1 prestigio 


#reducir nombres para facilidad de acceso 

def calcular_puntos_faltantes(prestigo, bp):
    total_requerido = prestigo * BPPP
    bp_faltantes = total_requerido - bp
    return bp_faltantes

def calcular_puntos_gastados(prestigio_a,  su_nivel):
    costo_por_nivel = BPPP / LVM
    puntos_actuales_gastados = (su_nivel - 1) * costo_por_nivel 
    puntos_gastados_en_total = (prestigio_a * BPPP) + puntos_actuales_gastados 
    return puntos_actuales_gastados, puntos_gastados_en_total 

def obtener_datos_deseados ():

    prestigo = -1
    while not (0 <= prestigo <= PMAX):
        try:
            prestigo = float(input("Ingrese su prestigio deseado (0-100): "))
            if not (0 <= prestigo <= PMAX):
                print("El prestigio deseado debe estar entre 0 y 100.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    prestigio_a = -1
    while not (0 <= prestigio_a <= prestigo):
        try:
            prestigio_a = float(input(f"Ingrese su prestigio actual (0-{prestigo}): "))
            if prestigio_a < 0: 
                print("El prestigio actual no puede ser negativo.")
            elif prestigio_a > prestigo:
                print(f"El prestigio actual no puede ser mayor que el prestigio deseado ({prestigo}).")
        except ValueError:
            print("Por favor, ingrese un número válido.")
            
    su_nivel = 0 
    while not (1 <= su_nivel <= LVM):
        try:
            su_nivel = float(input(f"Ingrese su nivel actual (1-{LVM}): "))
            if not (1 <= su_nivel <= LVM):
                print(f"El nivel debe estar entre 1 y {LVM}.")
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
       "prestigio_deseado": prestigo,
        "prestigio_actual": prestigio_a,
        "su_nivel": su_nivel,
        "bp_disponibles": bp
    }

MATRIZ = [
    {"prestigio_deseado": 25,
      "prestigio_actual": 1,
      "su_nivel": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 50,
      "prestigio_actual": 1,
      "su_nivel": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 75,
      "prestigio_actual": 1,
      "su_nivel": 1,
      "bp_disponibles": 250000000
      },
     {"prestigio_deseado": 100,
      "prestigio_actual": 1,
      "su_nivel": 1,
      "bp_disponibles": 250000000
      }
]


fuente_datos = None 
while fuente_datos not in ["M", "A"]:
    print("\n Seleccione la fuente de datos:")
    fuente_datos = input ("Esriba 'M' o 'A':").upper()
    if fuente_datos not in ["M", "A"]:
        print ("entrada no valida intente de nuevo.")

lista_resultados = []
datos_a_calcular = []

if fuente_datos == "A":
    print (f"\n Usando datos de la matriz predifinada con {len(MATRIZ)} personajes.")
    datos_a_calcular = MATRIZ
    num_calculos = len(MATRIZ)
else:
    num_calculos = 0
    while num_calculos <= 0:
        try: 
            num_calculos = int(input("\n ¿Con cuantos personajes va a realizar el calculo? "))
            if num_calculos <= 0:
                print ("ingresa un numero positivo.")
        except ValueError:
            print ("entrada no valida")

    print ("\n preparado para la entrada manual ")

for indice in range(num_calculos):
    print(f"\n personaje {indice + 1}")

    if fuente_datos == "M":
        datos = obtener_datos_deseados()
    else:
        datos = datos_a_calcular[indice]
    bp_faltantes = calcular_puntos_faltantes(datos["prestigio_deseado"], datos["bp_disponibles"])
    puntos_actuales_gastados, puntos_gastados_en_total = calcular_puntos_gastados(datos["prestigio_actual"], datos["su_nivel"])

    resultado = {
        "cálculo": indice + 1,
        "p_deseado": datos["prestigio_deseado"],
        "p_actual": datos["prestigio_actual"],
        "bp_faltantes": bp_faltantes,
        "bp_gastados_total": puntos_gastados_en_total
    }
    lista_resultados.append(resultado)

print("\n" + "="*50)
print("Resultados:")
print("="*50)

for resultado in lista_resultados:
    print(f"\nResultados pesonaje #{resultado['cálculo']}:")
    print(f"  Prestigio deseado: P{resultado['p_deseado']:.0f} (Desde P{resultado['p_actual']:.0f})")
    print(f"  Puntos Faltantes: {resultado['bp_faltantes']:,.2f}")
    print(f"  Puntos Gastados Totales: {resultado['bp_gastados_total']:,.2f}")
