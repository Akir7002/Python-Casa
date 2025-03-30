def imprimir_menu():
    print('✨✨ ------------------✨✨')
    print('--- Bienvenido a Cine ---')
    print('✨✨ ------------------✨✨')
    print('[1] Comprar boletas') 
    print('[2] Ver los asientos disponibles')
    print('[3] Salir')

def obtener_una_opcion():
    while True: 
        try:  #si pasa un error se atrapa y se muestra el mensaje
            opcion = int(input('Seleccione una opción: '))
            if opcion >= 1 and opcion <= 3:
                return opcion
            else:
                print('Por favor, ingrese una opción válida.')
        except:
            print('Error. Intente Nuevamente.')

def mostrar_asientos(asientos):
    letras = ['A', 'B', 'C', 'D', 'E']
    
    # Calcular el ancho exacto de un asiento para centrar las letras
    asiento_ancho = 10  # Ancho estimado de "  [💺]  "
    
    # Imprimir las letras centradas 
    print('    ', end='')  # Espacio para el número de fila
    for letra in letras:
        # Centrar cada letra en el espacio del asiento
        espacio_medio = (asiento_ancho - 1) // 2
        print(' ' * espacio_medio + letra + ' ' * espacio_medio, end='')
    print()

    # Imprimir línea separadora para mejor visualización
    print('    ' + '-' * (asiento_ancho * 5))
    
    # Imprimir las filas con sus números y los asientos
    for i, fila in enumerate(asientos):
        print(f" {i + 1}  |", end='')
        for columna in fila:
            print(f"  [{columna}]  ", end='')
        print()
def comprar_boleta(asientos):
    mostrar_asientos(asientos)
    
    while True:
        try:
            fila = int(input("Ingrese el número de fila (1-5): ")) - 1
            if fila < 0 or fila >= 5:
                print("Fila inválida. Debe ser entre 1 y 5.")
                continue
                
            columna_letra = input("Ingrese la letra de columna (A-E): ").upper()
            if columna_letra not in ['A', 'B', 'C', 'D', 'E']:
                print("Columna inválida. Debe ser entre A y E.")
                continue
                
            columna = ord(columna_letra) - ord('A')
            
            if asientos[fila][columna] == '🔒':
                print("Este asiento ya está ocupado. Elija otro.")
                continue
                
            asientos[fila][columna] = '🔒'
            print(f"¡Boleta comprada para el asiento {fila+1}{columna_letra}!")
            
            print("\n--- Asientos actualizados ---")
            mostrar_asientos(asientos)  # Mostrar los asientos después de comprar
            input("\nPresione Enter para continuar...")  # Pausa para ver la actualización
            return
        except Exception as e:
            print(f"Error. Intente nuevamente: {e}")

def main():
    # Crear la matriz de asientos
    asientos = []
    for fila in range(5):
        columnas = ['💺' for _ in range(5)]
        asientos.append(columnas)
    
    while True:
        print("\n")  # Añadir espacio para mejor visualización
        imprimir_menu()
        opcion = obtener_una_opcion()
        
        if opcion == 1:
            comprar_boleta(asientos)
        elif opcion == 2:
            mostrar_asientos(asientos)
            input("\nPresione Enter para continuar...")  # Pausa para ver los asientos
        elif opcion == 3:
            print("¡Gracias por usar nuestro sistema de cine!")
            break


if __name__ == "__main__":
    main()