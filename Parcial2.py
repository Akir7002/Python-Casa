import json
import os
Estudiantes_JSON_PATH = "Estudiantes.json"
Estudiantes = {}


def manejar_json(archivo=Estudiantes_JSON_PATH, datos=None):
    """
    Maneja operaciones de lectura/escritura de archivos JSON con manejo robusto de errores.
    
    Args:
        archivo (str): Ruta del archivo JSON
        datos (dict, optional): Datos a guardar. Si es None, se lee el archivo.
    
    Returns:
        dict: Datos leídos o None si hubo error al guardar
    """
    if datos is None:  # Modo lectura
        try:
            if not os.path.exists(archivo):
                print(f"⚠️ Advertencia: El archivo {archivo} no existe. Se creará uno nuevo al guardar.")
                return {}
                
            with open(archivo, 'r', encoding='utf-8') as f:
                contenido = f.read()
                if not contenido.strip():
                    print(f"⚠️ Advertencia: El archivo {archivo} está vacío.")
                    return {}
                    
                return json.loads(contenido)
                
        except json.JSONDecodeError as e:
            print(f"❌ Error: El archivo {archivo} contiene JSON inválido. Detalle: {e}")
            return {}
            
        except Exception as e:
            print(f"❌ Error inesperado al leer {archivo}: {str(e)}")
            return {}
            
    else:  # Modo escritura
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
                f.flush()  # Forzar escritura inmediata
                os.fsync(f.fileno())  # Asegurar escritura en disco
                
            print(f"✅ Datos guardados exitosamente en {archivo}")
            return True
            
        except (IOError, PermissionError) as e:
            print(f"❌ Error al guardar en {archivo}: {str(e)}")
            return False
            
        except Exception as e:
            print(f"❌ Error inesperado al guardar: {str(e)}")
            return False

def mostrar_menu():
    print('✨✨ ----------------------------------------------✨✨')
    print('--- Bienvenido al sistema de calificaciones escolares ---')
    print('✨✨ ----------------------------------------------✨✨')
    print('[1] ➕   Agregar estudiante') 
    print('[2] 📚   Agregar materia a estudiante')
    print('[3] 🖋️   Agregar nota de estudiante')
    print('[4] 🔎   Consultar promedio por estudiante')
    print('[5] 👀   Ver lista de aprobados')
    print('[6] 💀   Ver lista de reprobados')
    print('[7] 📑   Ver estadísticas generales del grupo')
    print('[8] 👣   Salir')

def obtener_opcion():
    while True: 
        try:
            opcion = int(input('Seleccione una opción: '))
            if 1 <= opcion <= 8:
                return opcion
            print('Por favor, ingrese una opción válida (1-8).')
        except ValueError:
            print('Error: Debe ingresar un número. Intente nuevamente.')

def pausar():
    input("\nPresione Enter para continuar...")

# IMPORTANTE: Cargamos los datos del archivo al iniciar el programa
Estudiantes = manejar_json()
print(f"Estudiantes cargados: {list(Estudiantes.keys())}")

def agregar_estudiante():
    global Estudiantes
    try:
        nombre = input('Ingrese el nombre: ').title()
        apellido = input('Ingrese el apellido: ').title()
        edad = int(input('Ingrese la edad: '))
        
        if nombre in Estudiantes:
            print('⚠️ El estudiante ya existe. Ingrese otro nombre.')
            pausar()
            return
        
        Estudiantes[nombre] = {
            "apellido": apellido,
            "edad": edad,
            "materias": {}
        }
        
        print(f'✅ Estudiante {nombre} {apellido} agregado exitosamente!')
        pausar()
    except ValueError:
        print('❌ Error: La edad debe ser un número entero.')
        pausar()
    except Exception as e:
        print(f'❌ Error inesperado al agregar estudiante: {e}')
        pausar()

def agregar_materia():
    global Estudiantes
    try:
        nombre = input('\nIngrese el nombre del estudiante: ').title()
        
        if nombre not in Estudiantes:
            print(f'⚠️ Estudiante "{nombre}" no encontrado. Estudiantes registrados:')
            for estudiante in Estudiantes.keys():
                print(f"- {estudiante}")
            pausar()
            return
        
        materia = input('Ingrese la materia: ').title()
        
        if materia in Estudiantes[nombre]['materias']:
            print(f'⚠️ La materia {materia} ya está registrada para {nombre}.')
        else:
            Estudiantes[nombre]['materias'][materia] = []
            print(f'✅ Materia "{materia}" agregada exitosamente a {nombre}!')
        pausar()
    except Exception as e: #Expection as e es para capturar cualquier error inesperado
        # Esto es útil para depurar errores inesperados
        print(f'❌ Error inesperado al agregar materia: {e}')
        pausar()

def agregar_nota():
    global Estudiantes
    try:
        nombre = input('Ingrese el nombre del estudiante: ').title()
        
        if nombre not in Estudiantes:
            print(f'⚠️ Estudiante "{nombre}" no encontrado. Estudiantes registrados:')
            for estudiante in Estudiantes.keys():
                print(f"- {estudiante}")
            pausar()
            return
            
        if not Estudiantes[nombre]['materias']:
            print(f'⚠️ {nombre} no tiene materias registradas.')
            pausar()
            return
            
        print('\nMaterias disponibles:')
        materias = Estudiantes[nombre]['materias']
        for i, materia in enumerate(materias.keys()):
            print(f"[{i+1}] {materia} (Notas: {materias[materia]})")
            
        while True:
            try:
                opcion = int(input(f"Seleccione la materia (1-{len(materias)}): ")) - 1
                if 0 <= opcion < len(materias):
                    materia = list(materias.keys())[opcion]
                    break
                print("Número fuera de rango.")
            except ValueError:
                print("Error: Ingrese un número válido.")
                
        while True:
            try:
                nota = float(input(f'Ingrese la nota para {materia} (1.0-10.0): '))
                if 1.0 <= nota <= 10.0:
                    Estudiantes[nombre]['materias'][materia].append(nota)
                    print(f'✅ Nota {nota} agregada a {materia} de {nombre}!')
                    break
                print('La nota debe estar entre 1.0 y 10.0')
            except ValueError:
                print('Error: Ingrese un número válido.')
                
        pausar()
    except Exception as e:
        print(f'❌ Error inesperado: {e}')
        pausar()

def mostrar_promedios_por_materia_estudiante():
    global Estudiantes
    nombre = input('\nIngrese el NOMBRE del estudiante para ver sus promedios por materia: ').strip().title()

    # Normalizar nombres para evitar problemas de espacios y mayúsculas/minúsculas
    estudiantes_normalizados = {k.strip().title(): k for k in Estudiantes.keys()}
    nombre_real = estudiantes_normalizados.get(nombre)

    if not nombre_real:
        print(f'❌ Estudiante "{nombre}" no encontrado. Estudiantes disponibles:')
        for estudiante in Estudiantes.keys():
            print(f"- {estudiante}")
        pausar()
        return

    estudiante_data = Estudiantes[nombre_real]
    materias = estudiante_data.get('materias', {})

    if not materias:
        print(f'⚠️ El estudiante "{nombre}" no tiene materias registradas.')
        pausar()
        return

    print(f"\n📊 Reporte de Promedios por Materia para {nombre} {estudiante_data.get('apellido', '')}:")
    print('-'*45)

    alguna_materia_con_notas = False
    for materia, lista_notas in materias.items():
        if lista_notas:
            promedio_materia = sum(lista_notas) / len(lista_notas)
            print(f"  ✅ {materia:<15}: Promedio = {promedio_materia:.2f} (Notas: {lista_notas})")
            alguna_materia_con_notas = True
        else:
            print(f"  ⚪️ {materia:<15}: (Sin notas registradas)")

    if not alguna_materia_con_notas and materias:
        print("\n  (El estudiante aún no tiene notas registradas en ninguna materia para calcular promedios).")
    pausar()

def listar_aprobados(nota_minima=6.0):
    global Estudiantes
    print(f'\n--- Lista de Estudiantes Aprobados (Promedio General >= {nota_minima}) ---')
    print('-'*60)

    if not Estudiantes:
        print('No hay estudiantes registrados en el sistema.')
        pausar()
        return

    aprobados = []
    
    for nombre, datos in Estudiantes.items():
        materias = datos.get('materias', {})
        todas_notas = [nota for notas in materias.values() for nota in notas]
        
        if not todas_notas:
            continue
            
        promedio_general = sum(todas_notas) / len(todas_notas)
        
        if promedio_general >= nota_minima:
            # Filtrar materias aprobadas
            materias_aprobadas = {
                materia: notas for materia, notas in materias.items()
                if notas and (sum(notas) / len(notas)) >= nota_minima
            }
            aprobados.append({
                'nombre': nombre,
                'apellido': datos.get('apellido', ''),
                'promedio': promedio_general,
                'materias_aprobadas': materias_aprobadas
            })

    if aprobados:
        print(f"\nTotal de aprobados: {len(aprobados)}\n")
        for estudiante in sorted(aprobados, key=lambda x: x['nombre']):
            print(f"Estudiante: {estudiante['nombre']} {estudiante['apellido']}")
            print(f"Promedio general: {estudiante['promedio']:.2f}")
            print("Materias aprobadas:")
            
            for materia, notas in estudiante['materias_aprobadas'].items():
                promedio_materia = sum(notas) / len(notas)
                print(f"  - {materia:<15}: {promedio_materia:.2f} (Notas: {notas})")
            print("-"*40)
    else:
        print("\nNo se encontraron estudiantes aprobados con el criterio actual.")
    pausar()

def listar_reprobados(nota_minima=6.0):
    global Estudiantes
    print(f'\n--- Lista de Estudiantes con Materias Reprobadas (Promedio < {nota_minima}) ---')
    print('-'*65)

    if not Estudiantes:
        print('⚠️ No hay estudiantes registrados en el sistema.')
        pausar()
        return

    reprobados = []
    
    for nombre, datos in Estudiantes.items():
        materias = datos.get('materias', {})
        # Depuración: Verificar las materias y notas del estudiante
        print(f"Procesando estudiante: {nombre}, Materias: {materias}")
        
        # Filtrar materias reprobadas
        materias_reprobadas = {
            materia: notas for materia, notas in materias.items()
            if notas and (sum(notas) / len(notas)) < nota_minima
        }
        
        # Depuración: Verificar las materias reprobadas
        print(f"Materias reprobadas de {nombre}: {materias_reprobadas}")
        
        if materias_reprobadas:
            reprobados.append({
                'nombre': nombre,
                'apellido': datos.get('apellido', ''),
                'materias_reprobadas': materias_reprobadas
            })

    if reprobados:
        print(f"\nTotal de estudiantes con materias reprobadas: {len(reprobados)}\n")
        for estudiante in sorted(reprobados, key=lambda x: x['nombre']):
            print(f"Estudiante: {estudiante['nombre']} {estudiante['apellido']}")
            print("Materias reprobadas:")
            
            for materia, notas in estudiante['materias_reprobadas'].items():
                promedio_materia = sum(notas) / len(notas)
                print(f"  - {materia:<15}: {promedio_materia:.2f} (Notas: {notas})")
            print("-"*40)
    else:
        print("\nℹ️ No se encontraron estudiantes con materias reprobadas con el criterio actual.")
    pausar()

def ver_estadisticas():
    global Estudiantes
    print('\n--- Estadísticas Generales del Grupo ---')

    if not Estudiantes:
        print('⚠️ No hay estudiantes registrados para calcular estadísticas.')
        pausar()
        return

    num_estudiantes = len(Estudiantes)
    print(f"📊 Número total de estudiantes: {num_estudiantes}")

    promedios_generales = []
    estudiantes_sin_notas = 0
    num_materias_totales = 0
    num_notas_totales_count = 0

    for nombre, datos_estudiante in Estudiantes.items():
        materias = datos_estudiante.get('materias', {})
        notas_estudiante = [nota for notas_materia in materias.values() for nota in notas_materia]
        num_materias_totales += len(materias)
        num_notas_totales_count += len(notas_estudiante)

        if notas_estudiante:
            promedio = sum(notas_estudiante) / len(notas_estudiante)
            promedios_generales.append(promedio)
        else:
            estudiantes_sin_notas += 1

    if promedios_generales:
        promedio_grupo = sum(promedios_generales) / len(promedios_generales)
        print(f"📈 Promedio general del grupo: {promedio_grupo:.2f}")
        print(f"🥇 Promedio más alto: {max(promedios_generales):.2f}")
        print(f"🥉 Promedio más bajo: {min(promedios_generales):.2f}")
    else:
        print("ℹ️ No hay notas registradas para calcular promedios.")

    if estudiantes_sin_notas > 0:
        print(f"ℹ️ {estudiantes_sin_notas} estudiante(s) no tienen notas registradas.")

    if num_estudiantes > 0:
        print(f"📚 Promedio de materias por estudiante: {num_materias_totales / num_estudiantes:.2f}")
        if num_materias_totales > 0:
            print(f"🖋️ Promedio de notas por materia: {num_notas_totales_count / num_materias_totales:.2f}")
    pausar()

def main():
    global Estudiantes
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
            mostrar_promedios_por_materia_estudiante()
        elif opcion == 5:
            listar_aprobados()
        elif opcion == 6:
            listar_reprobados()
        elif opcion == 7:
            ver_estadisticas()
        elif opcion == 8:
            print("\n💾 Guardando cambios...")
            manejar_json(datos=Estudiantes)
            pausar()
            print('\n👋 ¡Hasta luego! Gracias por usar el sistema.')
            break

if __name__ == "__main__":
    main()