# @autor : David Esteban Echeverri Cardenas
# @fecha : 17 octubre 2023
# @ficha : 2740559 
# @Description : calculadora


# Función para sumar dos números
def suma(suma1, suma2):
    return suma1 + suma2

# Función para restar dos números
def resta(resta1, resta2):
    return resta1 - resta2

# Función para multiplicar dos números
def multiplicacion(mult1, mult2):
    return mult1 * mult2

# Función para dividir dos números
def division(divi1, divi2):
    if divi2 != 0:
        return  divi1/divi2
    else:
        return "Error: división por cero"

# Función para obtener el residuo de la división
def residuo(resi1, resi2):
    if resi2 != 0:
        return resi1 % resi2
    else:
        return "Error: división por cero"

# Función para calcular la potencia
def potencia(pote1, pote2):
    return pote1 ** pote2
