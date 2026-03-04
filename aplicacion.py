def main():

    base_datos = []

    while True:
        print("\n--- SISTEMA DE REGISTRO DE NOTAS ---")
        print("1. Registrar ingreso (Nombre)")
        print("2. Registrar nota")
        print("3. Ver promedio")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            nombre = input("Ingresa el nombre del estudiante: ")
            estudiante = {
                "nombre": nombre,
                "nota": 0.0
            }
        
            base_datos.append(estudiante)
            print(f" Estudiante '{nombre}' registrado con éxito.")
            
        elif opcion == '2':
            print("\n[Opción 2 ]")
            
        elif opcion == '3':
            print("\n[Opción 3 ]")
            
        elif opcion == '4':
            print("Saliendo... ")
            break
        else:
            print(" Opción no válida.")

if __name__ == "__main__":
    main()