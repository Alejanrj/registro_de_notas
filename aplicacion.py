
base_datos = []

def registrar_estudiante():
    nombre = input("Nombre del estudiante: ")
    # diccionario sencillo
    estudiante = {"nombre": nombre, "nota": 0.0}
    base_datos.append(estudiante)
    print("Estudiante guardado con éxito.")


def poner_nota():
    busqueda = input("¿Nota que deseas registrar?: ")
    for persona in base_datos:
        if persona["nombre"].lower() == busqueda.lower():
            nueva_nota = float(input("Ingresa la nota: "))
            persona["nota"] = nueva_nota
            print("Nota registrada.")
            return
    print("No encontré a ese estudiante.")

def calcular_promedio():
    if not base_datos: 
        print("No hay nadie en la lista.")
    else:
        suma = 0
        cantidad = 0
        for persona in base_datos:
            suma = suma + persona["nota"]
            cantidad = cantidad + 1
        
        promedio = suma / cantidad
        
        if cantidad == 1:
            nombre_unico = base_datos[0]['nombre']
            print(f"La nota de {nombre_unico} es: {promedio}")
        else:
            print(f"El promedio de los {cantidad} estudiantes es: {promedio}")

while True:
    print("\n--- MENÚ DE NOTAS ---")
    print("1. Registrar Estudiante")
    print("2. Registrar Nota")
    print("3. Ver Promedio")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        registrar_estudiante() 
    elif opcion == "2":
        poner_nota()          
    elif opcion == "3":
        calcular_promedio()    
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    # Esta es una línea de prueba en la rama feature/prueba