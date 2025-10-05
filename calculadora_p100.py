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

lista_resultados = []
personajes = 0
while personajes <= 0:
    try:
        personajes = int(input("\n con cuantos personajes va a realizar el calculo?"))
        if personajes <= 0 :
            print ("ingresa un numero positivo.")
    except ValueError:
        print ("entrada no valida")
    
for indice in range(personajes):
    print (f"\n personaje {indice + 1}")

    datos = obtener_datos_deseados()

    bp_faltantes = calcular_puntos_faltantes(datos["prestigio_deseado"], datos["bp_disponibles"])
    puntos_actuales_gastados, puntos_gastados_en_total = calcular_puntos_gastados(datos["prestigio_actual"], datos["su_nivel"])
    
    resultado = {
        "cálculo": indice  + 1, 
        "p_deseado": datos["prestigio_deseado"],
        "p_actual": datos["prestigio_actual"],
        "bp_faltantes": bp_faltantes,
        "bp_gastados_total": puntos_gastados_en_total
    }
    lista_resultados.append(resultado)


print ("\n" + "="*50 )
print ("Resultados:")
print("="*50)

for resultado in lista_resultados:
    print(f"\nResultados pesonaje #{resultado['cálculo']}:")
    print(f"  Prestigio deseado: P{resultado['p_deseado']:.0f} (Desde P{resultado['p_actual']:.0f})")
    print(f"  Puntos Faltantes: {resultado['bp_faltantes']:,.2f}")
    print(f"  Puntos Gastados Totales: {resultado['bp_gastados_total']:,.2f}")
