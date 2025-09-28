#Definicion de terminos 

P100BP = 150000000  #cantidad de puntos requeridos para max
LVM = 50  #cantidad de niveles por prestigio 
PMAX = 100 #cantidad de prestigios 
BPPP = 1500000 #cantidad de puntos para 1 prestigio 


#reducir nombres para facilidad de acceso 

def calcular_puntos_faltantes(prestigio_deseado, bp_disponibles):
    total_requerido = prestigio_deseado * BPPP
    bp_faltantes = total_requerido - bp_disponibles
    return bp_faltantes

def calcular_puntos_gastados(prestigio_actual,  su_nivel):
    costo_por_nivel = BPPP / LVM
    puntos_actuales_gastados = (su_nivel - 1) * costo_por_nivel 
    puntos_gastados_en_total = (prestigio_actual * BPPP) + puntos_actuales_gastados 
    return puntos_actuales_gastados, puntos_gastados_en_total 

prestigio_deseado = -1
while not (0 <= prestigio_deseado <= PMAX):
    try:
        prestigio_deseado = float(input("Ingrese su prestigio deseado (0-100): "))
        if not (0 <= prestigio_deseado <= PMAX):
            print("El prestigio deseado debe estar entre 0 y 100.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

prestigio_actual = -1
while not (0 <= prestigio_actual <= prestigio_deseado):
    try:
        prestigio_actual = float(input(f"Ingrese su prestigio actual (0-{prestigio_deseado}): "))
        if prestigio_actual < 0: 
            print("El prestigio actual no puede ser negativo.")
        elif prestigio_actual > prestigio_deseado:
            print(f"El prestigio actual no puede ser mayor que el prestigio deseado ({prestigio_deseado}).")
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

bp_disponibles = -1
while bp_disponibles < 0:
    try:
        bp_disponibles = float(input("Ingrese los BP que tiene actualmente: "))
        if bp_disponibles < 0:
            print("Los BP disponibles no pueden ser negativos.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

bp_faltantes = calcular_puntos_faltantes(prestigio_deseado, bp_disponibles)

puntos_actuales_gastados, puntos_gastados_en_total = calcular_puntos_gastados(prestigio_actual, su_nivel)

print ("\n" + "="*50 )
print ("Resultados:")
print("="*50)

print(f"La cantidad de puntos faltantes para su prestigio: {bp_faltantes:,.2f}")
print(f"La cantidad de puntos gastados actualmente es: {puntos_actuales_gastados:,.2f}")
print(f"La cantidad de puntos gastados en total es: {puntos_gastados_en_total:,.2f}")   