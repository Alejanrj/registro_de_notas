def main():
    
    while True:
        print("\n--- SISTEMA DE REGISTRO DE NOTAS ---")
        print("1. Registrar ingreso")
        print("2. Registrar nota")
        print("3. Ver promedio")
        print("4. Salir")
        
        opcion = input("Por favor, selecciona una opción (1-4): ")
        
        if opcion == '1':
            print("\n[Has elegido: Registrar ingreso] ")
            
        elif opcion == '2':
            print("\n[Has elegido: Registrar nota] ")
            
        elif opcion == '3':
            print("\n[Has elegido: Ver promedio] ")
            
        elif opcion == '4':
            print("\nSaliendo del sistema... ¡Hasta luego!")
            break 
            
        else:
        
            print("\n❌ Opción no válida. Por favor intenta de nuevo.")

if __name__ == "__main__":
    main()