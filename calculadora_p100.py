#Definicion de terminos 

P100BP = 150000000  #cantidad de puntos requeridos para max
LVM = 50  #cantidad de niveles por prestigio 
PMAX = 100 #cantidad de prestigios 
BPPP = 1500000 #cantidad de puntos para 1 prestigio 


#reducir nombres para facilidad de acceso 

#funciones aplicacion 
def calcular_puntos_faltantes (prestigio_deseado, bp_disponibles):
    if prestigio_deseado > PMAX or prestigio_deseado < 0:
        print ("el prestigio deseado no es valido y debe de ser entre 0 y 100")
    total_requerido = (prestigio_deseado) * (BPPP)
    bp_faltantes = (total_requerido) - (bp_disponibles)
    return bp_faltantes

def calcular_puntos_gastados (prestigio_actual, su_nivel):
    puntos_de_prestigio = (prestigio_actual) * (BPPP)
    puntos_de_nivel = (puntos_de_prestigio) / (LVM)
    puntos_actuales_gastados = (su_nivel - 1) * (puntos_de_nivel) 
    puntos_gastados_en_total = (puntos_de_prestigio) + (puntos_de_nivel) 
    return puntos_actuales_gastados, puntos_gastados_en_total


prestigio_deseado = float(input("ingrese su prestigio deseado: "))
prestigio_actual = float(input("ingrese su prestigio actual: "))
su_nivel = float(input("ingrese su nivel actual: "))
bp_disponibles = float(input("ingrese los bp que tiene actualmente: "))


if prestigio_deseado < 0 or prestigio_actual < 0 or su_nivel < 1 or su_nivel > LVM or bp_disponibles < 0:
    print("los valores ingresados no son validos, por favor ingrese valores positivos y un nivel entre 1 y 50")
elif prestigio_deseado < prestigio_actual:
    print("el prestigio deseado no puede ser menor que el prestigio actual")
else: bp_faltantes = calcular_puntos_faltantes \
    (prestigio_deseado, bp_disponibles)

puntos_actuales_gastados, puntos_gastados_en_total = \
      calcular_puntos_gastados(prestigio_actual, su_nivel)

print(f"la cantidad de puntos faltantes para su prestigo:{bp_faltantes:,.2f}")
print(f"la cantidad de puntos gastados actualmente es:{puntos_actuales_gastados:,.2f}")
print(f"la cantidad de puntos gastados en total es:{puntos_gastados_en_total:,.2f}")

#redccion de lineas de texto debe de ser 75 si no mal recuerdo 