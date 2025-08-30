#Definicion de terminos 

P100BP = 150000000  #cantidad de puntos requeridos para max
LVM = 50  #cantidad de niveles por prestigio 
PMAX = 100 #cantidad de prestigios 
BPPP = 1500000 #cantidad de puntos para 1 prestigio 


#reducir nombres para facilidad de acceso 
prestigio_deseado = float(input("ingrese su prestigio deseado: "))
prestigio_actual = float(input("ingrese su prestigio actual: "))
su_nivel = float(input("ingrese su nivel actual: "))
bp_disponibles = float(input("ingrese los bp que tiene actualmente: "))

total_requerido = (prestigio_deseado) * (BPPP)
bp_faltantes = (total_requerido) - (bp_disponibles)

puntos_de_prestigio = (prestigio_actual) * (BPPP)
puntos_de_nivel = (puntos_de_prestigio) / (LVM)
puntos_actuales_gastados = (su_nivel - 1) * (puntos_de_nivel) 
puntos_gastados_en_total = (puntos_de_prestigio) + (puntos_de_nivel) 

#hay que ponerle comas a los numeros para facilidad de lectura 

print(f"la cantidad de puntos faltantes para su prestigo: {bp_faltantes:.2f} ")
print(f"la cantidad de puntos gastados actualmente es:{puntos_actuales_gastados:.2f}")
print(f"la cantidad de puntos gastados en total es: {puntos_gastados_en_total:.2f}")

#redccion de lineas de texto debe de ser 75 su no mal recuerdo 