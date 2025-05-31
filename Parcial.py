def imprimir_menu():
    print('✨✨ ----------------------------------------------------------✨✨')
    print('--- 😉 Bienvenido a su sistema de calificaciones de confianza 😉 ---')
    print('✨✨ ----------------------------------------------------------✨✨')
    print('[1] Agregar calificación')
    print('[2] Ver calificaciones')
    print('[3] Calcular promedio')
    print('[4] Verificar Aprobados')
    print('[5] Modificar calificación')
    print('[6] Salir')


def agregar_calificacion(calificaciones):
    
    nombre = input("Ingrese el nombre del estudiante📝: ")
    
    # Verificar si el estudiante ya existe en el diccionario
    if nombre not in calificaciones:
        calificaciones[nombre] = []  # Crear una lista vacía para las calificaciones del estudiante
    
    try:

        cantidad_notas = int(input(f"¿Cuántas notas desea agregar para {nombre}? "))
        
        if cantidad_notas <= 0:
            print("Debe ingresar un número positivo de notas.")
            return
            
        # Agregar la cantidad especificada de notas
        for i in range(cantidad_notas):
            try:
                calificacion = float(input(f"Ingrese la calificación {i+1} para {nombre}📝: "))
                calificaciones[nombre].append(calificacion) # Agregar la calificación a la lista del estudiante
                print(f"Calificación {calificacion} agregada con éxito ✅")
            except ValueError:
                print("Error: Ingrese un número válido.")
                i -= 1  # Repetir 
        
        print(f"Finalizado. Calificaciones de {nombre}: {calificaciones[nombre]}")
    except ValueError:
        print("Error: Ingrese un número entero válido para la cantidad de notas.")


def ver_calificaciones(calificaciones):

    if not calificaciones:
        print("No hay calificaciones registradas. Por favor, ingrese una calificación al sistema.")
    else:
        print("Calificaciones de los estudiantes:")
        for nombre, notas in calificaciones.items():
            print(f"{nombre}: {notas}")


def calcular_promedio(calificaciones):
    if not calificaciones:
        print("No hay calificaciones para calcular el promedio")
    else:
        nombre = input("Ingrese el nombre del estudiante para calcular su promedio: ")
        if nombre in calificaciones:
            promedio = sum(calificaciones[nombre]) / len(calificaciones[nombre])
            print(f"El promedio de {nombre} es: {promedio:.2f}")
        else:
            print(f"No se encontraron calificaciones para {nombre}")


def verificar_aprobados(calificaciones): #para saber si el estudiante esta aprobado o no
    if not calificaciones:
        print("No hay calificaciones para verificar.")
    else:
        nombre = input("Ingrese el nombre del estudiante para verificar si está aprobado: ")
        if nombre in calificaciones:
            promedio = sum(calificaciones[nombre]) / len(calificaciones[nombre])
            if promedio >= 6:
                print(f"{nombre} está aprobado✅ con un promedio de {promedio:.2f}")
            else:
                print(f"{nombre} está suspendido❌ con un promedio de {promedio:.2f}")
        else:
            print(f"No se encontraron calificaciones para {nombre}")


def modificar_calificacion(calificaciones):

    #Permite modificar una calificación específica de un estudiante.
    
    if not calificaciones:
        print("No hay calificaciones para modificar")
    else:
        nombre = input("Ingrese el nombre del estudiante cuya calificación desea modificar: ")
        if nombre in calificaciones:
            print(f"Calificaciones de {nombre}: {calificaciones[nombre]}")
            indice = int(input("Ingrese el número de la calificación que desea modificar (1, 2, 3, ...): ")) - 1
            if 0 <= indice < len(calificaciones[nombre]):
                nueva_calificacion = float(input("Ingrese la nueva calificación: "))
                calificaciones[nombre][indice] = nueva_calificacion
                print("Calificación modificada con éxito✅.")
            else:
                print("Número de calificación no válido❌")
        else:
            print(f"No se encontraron calificaciones para {nombre}")


def main():
    
    #Función principal que maneja el menú y las opciones del sistema.
    
    calificaciones = {}  # Diccionario para almacenar las calificaciones de los estudiantes
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_calificacion(calificaciones)
        elif opcion == "2":
            ver_calificaciones(calificaciones)
        elif opcion == "3":
            calcular_promedio(calificaciones)
        elif opcion == "4":
            verificar_aprobados(calificaciones)
        elif opcion == "5":
            modificar_calificacion(calificaciones)
        elif opcion == "6":
            print("Gracias por usar nuestro sistema de calificaciones 😊")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Intente de nuevo")


if __name__ == "__main__":
    main()