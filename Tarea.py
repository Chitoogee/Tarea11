def crear_plan(faenas, dias):
    plan = []
    for i in range(faenas):
        fila = []
        for j in range(dias):
            fila.append(0)
        plan.append(fila)
    return plan


def mostrar_plan(plan):
    for fila in plan:
        for elemento in fila:
            print(elemento, end="\t")
        print()


def ingresar_produccion(plan):

    for i in range(len(plan)):
        for j in range(len(plan[0])):
            produccion = float(
                input(f"Ingrese la producción de la faena {i+1} en el día {j+1}: "))
            plan[i][j] = produccion


def produccion_faena(plan, faena):
    produccion_total = 0
    for i in range(len(plan[faena])):
        produccion_total += plan[faena][i]
    return produccion_total


def produccion_dia(plan, dia):

    produccion_total = 0
    for i in range(len(plan)):
        produccion_total += plan[i][dia]
    return produccion_total


def generar_plan():

    print("Plan de producción:")
    mostrar_plan(plan)


def ingresar_datos():

    ingresar_produccion(plan)


def calcular_produccion_faena():

    faena = int(input("Ingrese el número de la faena: "))
    produccion_total = produccion_faena(plan, faena-1)
    print(f"La producción total de la faena {faena} es: {produccion_total}")


def calcular_produccion_dia():

    dia = int(input("Ingrese el número del día: "))
    produccion_total = produccion_dia(plan, dia-1)
    print(f"La producción total del día {dia} es: {produccion_total}")


faenas = int(input("Ingrese el número de faenas: "))
dias = int(input("Ingrese el número de días: "))

plan = crear_plan(faenas, dias)

while True:
    print("1. Generar plan de producción")
    print("2. Ingresar datos de producción")
    print("3. Calcular producción total de una faena específica")
    print("4. Calcular producción total de todas las faenas en un día específico")
    print("5. Salir del programa")

    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        generar_plan()
    elif opcion == "2":
        ingresar_datos()
    elif opcion == "3":
        calcular_produccion_faena()
    elif opcion == "4":
        calcular_produccion_dia()
    elif opcion == "5":
        print("Saliendo del menú...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
