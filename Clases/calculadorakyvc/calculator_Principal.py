# Importar el módulo de operaciones matemáticas
import modulo_calculos

# Definimos la opción de la operación a realizar.
def menu_calculos():
    print("Operaciones matemáticas:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Residuo")
    print("6. Potencia")
    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    # Realiza el cálculo llamando al módulo.
    if opcion == '1':
        suma1 = float(input("Ingrese el primer número: "))
        suma2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado de la suma:", modulo_calculos.suma(suma1, suma2))
    elif opcion == '2':
        res1 = float(input("Ingrese el primer número: "))
        res2 = float(input("Ingrese el segundo número: "))
        print("Resultado de la resta:", modulo_calculos.resta(res1, res2))
    elif opcion == '3':
        mult1 = float(input("Ingrese el primer número: "))
        mult2 = float(input("Ingrese el segundo número: "))
        print("Resultado de la multiplicación:", modulo_calculos.multiplicacion(mult1, mult2))
    elif opcion == '4':
        div1 = float(input("Ingrese el primer número: "))
        div2 = float(input("Ingrese el segundo número: "))
        print("Resultado de la división:", modulo_calculos.division(div1, div2))
    elif opcion == '5':
        res1 = float(input("Ingrese el primer número: "))
        res2 = float(input("Ingrese el segundo número: "))
        print("Resultado del residuo:", modulo_calculos.residuo(res1, res2))
    elif opcion == '6':
        pot1 = float(input("Ingrese la base: "))
        pot2 = float(input("Ingrese el exponente: "))
        print("Resultado de la potencia:", modulo_calculos.potencia(pot1, pot2))
    else:
        print("Opción no válida")

# Llamar a la función del menú de cálculos
menu_calculos()