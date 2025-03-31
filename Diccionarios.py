#ejemplo de que se mas o menos debo hacer con un diccionario en python
#estudiantes = {
#    "Maria": {
#       "apellido": "Gomez",
#      "edad": 18,
#       "materias": {
#          "Matemáticas": [7.5, 8.0],
#         "Física": [6.0]

Estudiantes = {} #diccionario vacio global para luego almacenar 

def mostrar_menu():
    print('✨✨ ------------------✨✨')
    print('--- Bienvenido al registro de notas ---')
    print('✨✨ ------------------✨✨')
    print('[1] ➕   Agregar estudiante') 
    print('[2] 📚   Agregar materia a estudiante')
    print('[3] 🖋️   Agregar nota de estudiante')
    print('[4] 🔎   Consultar promedio por estudiante')
    print('[5] 👣   Salir')

def obtener_opcion():
    while True: 
        try:
            opcion = int(input('Seleccione una opción: '))
            if 1 <= opcion <= 5:
                return opcion
            print('Por favor, ingrese una opción válida (1-5).')
        except ValueError:
            print('Error: Debe ingresar un número. Intente nuevamente.')

def pausar():
    input("\nPresione Enter para continuar...")

def agregar_estudiante():
    try:
        cedula = int(input('\nIngrese la cédula del estudiante: '))
        if cedula in Estudiantes:
            print('⚠️ El estudiante ya existe. Ingrese otra cédula.')
        else:
            nombre = input('Ingrese el nombre: ').title()
            apellido = input('Ingrese el apellido: ').title()
            Estudiantes[cedula] = {
                'nombre': nombre,
                'apellido': apellido,
                'materias': {}
            }
            print(f'✅ Estudiante {nombre} {apellido} agregado exitosamente!')
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def agregar_materia():
    try:
        cedula = int(input('\nIngrese la cédula del estudiante: '))
        if cedula not in Estudiantes:
            print('⚠️ Estudiante no encontrado. Regístrelo primero.')
        else:
            materia = input('Ingrese la materia: ').title()
            if materia in Estudiantes[cedula]['materias']:
                print(f'⚠️ La materia {materia} ya está registrada.')
            else:
                Estudiantes[cedula]['materias'][materia] = []
                print(f'✅ Materia {materia} agregada exitosamente!')
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def agregar_nota():
    try:
        cedula = int(input('\nIngrese la cédula del estudiante: '))
        if cedula not in Estudiantes:
            print('⚠️ Estudiante no encontrado. Regístrelo primero.')
            return
            
        if not Estudiantes[cedula]['materias']:
            print('⚠️ El estudiante no tiene materias registradas.')
            return
            
        print('\nMaterias disponibles:')
        for materia in Estudiantes[cedula]['materias']:
            print(f"- {materia}")
            
        materia = input('\nIngrese la materia: ').title()
        if materia not in Estudiantes[cedula]['materias']:
            print(f'⚠️ La materia {materia} no está registrada.')
            return
            
        try:
            nota = float(input('Ingrese la nota (1.0-5.0): '))
            if 1.0 <= nota <= 5.0:
                Estudiantes[cedula]['materias'][materia].append(nota)
                print(f'✅ Nota {nota} agregada a {materia}!')
            else:
                print('⚠️ La nota debe estar entre 1.0 y 5.0.')
        except ValueError:
            print('❌ Error: La nota debe ser un número.')
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def calcular_promedio():
    try:
        # 1. Pedir cédula
        cedula = int(input('\nIngrese la cédula del estudiante: '))
        if cedula not in Estudiantes:
            print('❌ Estudiante no encontrado.')
            pausar()
            return
            
        estudiante = Estudiantes[cedula]
        
        # 2. Verificar si tiene materias
        if not estudiante['materias']:
            print('⚠️ El estudiante no tiene materias registradas.')
            pausar()
            return
            
        # 3. Bucle para reintentar selección de materia
        while True:
            print('\nMaterias disponibles:')
            for materia in estudiante['materias']:
                print(f"- {materia}")
                
            materia = input('\nIngrese la materia (o "salir" para cancelar): ').title()
            
            if materia.lower() == 'salir':
                return
                
            if materia not in estudiante['materias']:
                print(f'⚠️ La materia "{materia}" no está registrada. Intente nuevamente.')
                continue
                
            # 4. Calcular promedio si hay notas
            notas = estudiante['materias'][materia]
            if not notas:
                print(f'⚠️ No hay notas registradas en {materia}.')
            else:
                promedio = sum(notas) / len(notas)
                print(f'\n🔍 Reporte de {estudiante["nombre"]} {estudiante["apellido"]}:')
                print(f'Materia: {materia}')
                print(f'Notas: {notas}')
                print(f'Promedio: {promedio:.2f}')
                print('-'*30)
            break
            
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 1:
            agregar_estudiante()
        elif opcion == 2:
            agregar_materia()
        elif opcion == 3:
            agregar_nota()
        elif opcion == 4:
            calcular_promedio()
        elif opcion == 5:
            print('\n👋 ¡Hasta luego! Gracias por usar el sistema.')
            break

if __name__ == "__main__":
    main()