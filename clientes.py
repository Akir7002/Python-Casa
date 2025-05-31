import json
import os

CLIENTES_JSON_PATH = "clientes.json"
clientes = {}

# Cargar datos desde el archivo JSON
def cargar_clientes():
    global clientes
    if os.path.exists(CLIENTES_JSON_PATH):
        print("Archivo encontrado, cargando datos...")
        with open(CLIENTES_JSON_PATH, "r", encoding="utf-8") as file:
            clientes = json.load(file)
        print(f"✅ Clientes cargados: {clientes}")  # Depuración
    else:
        print("⚠️ Archivo no encontrado, inicializando diccionario vacío.")
        clientes = {}

# Guardar datos en el archivo JSON
def guardar_clientes():
    with open(CLIENTES_JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(clientes, file, indent=4, ensure_ascii=False)

def obtener_opcion():
    while True: 
        try:
            opcion = input('Seleccione una opción: ').strip()
            if opcion == '':  # Si está vacío
                continue
            opcion = int(opcion)
            if 1 <= opcion <= 6:
                return opcion
            print('Por favor, ingrese una opción válida (1-6).')
        except ValueError:
            print('Error: Debe ingresar un número. Intente nuevamente.')

def mostrar_menu():
    print('✨✨ ------------------------------✨✨')
    print('------- Bienvenido al registro -------')
    print('✨✨ ------------------------------✨✨')
    print('[1] ➕   Registrar un cliente') 
    print('[2] 🗑️   Eliminar un cliente')
    print('[3] 🖋️   Buscar un cliente')
    print('[4] 🔎   Lista de clientes')
    print('[5] 🔎   Lista de clientes preferenciales')
    print('[6] 👣   Salir')
    print('✨✨ ------------------------------✨✨')
def pausar():
    input("\nPresione Enter para continuar...")

def registrar_clientes():
    try:
        cedula = input('\nIngrese la cédula del cliente: ').strip()
        if cedula in clientes:
            print('⚠️ El cliente ya existe. Ingrese otra cédula.')
        else:
            nombre = input('Ingrese el nombre: ').title()
            apellido = input('Ingrese el apellido: ').title()
            correo = input('Ingrese el correo: ').lower()
            telefono = input('Ingrese el teléfono: ').strip()
            direccion = input('Ingrese la dirección: ').title()
            preferencial = input('¿Es cliente preferencial? (s/n): ').lower() == 's'
            
            # Agregar el cliente al diccionario
            clientes[cedula] = {
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo,
                'telefono': telefono,
                'direccion': direccion,
                'preferencial': preferencial
            }
            print(f'✅ Cliente {nombre} {apellido} agregado exitosamente!')
            guardar_clientes()  # Guardar cambios en el archivo JSON
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def eliminar_cliente():
    try:
        cedula = input('\nIngrese la cédula del cliente: ').strip()
        if cedula not in clientes:
            print('⚠️ El cliente no existe. Por favor registre el cliente primero.')
            return
        del clientes[cedula]  # Eliminar cliente del diccionario
        print(f'✅ Cliente con cédula {cedula} eliminado exitosamente!')
        guardar_clientes()  # Guardar cambios en el archivo JSON
    except ValueError:
        print('❌ Error: La cédula debe ser un número entero.')
    pausar()

def buscar_cliente():
    try:
        cedula = input('\nIngrese la cédula del cliente: ').strip()
        print(f"\n🔍 Buscando cédula: {cedula}")
        print(f"🔍 Clientes disponibles: {list(clientes.keys())}\n")

        if cedula not in clientes:
            print('⚠️ El cliente no existe. Por favor registre el cliente primero.')
            return
        
        cliente = clientes[cedula]
        print('✨✨ ------------------------------✨✨')
        print('------- Cliente Encontrado -------')
        print('✨✨ ------------------------------✨✨')
        print(f"Nombre: {cliente['nombre']}")
        print(f"Apellido: {cliente['apellido']}")
        print(f"Correo: {cliente['correo']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Dirección: {cliente['direccion']}")
        print(f"Preferencial: {'Sí' if cliente['preferencial'] else 'No'}")
        print('-------------------------------------')
    except ValueError:
        print('❌ Error: La cédula debe ser un número válido.')
    pausar()

def listar_clientes(): 
    no_preferenciales = [cliente for cliente in clientes.values() if not cliente['preferencial']]  # Filtra los clientes no preferenciales

    if not no_preferenciales:
        print('⚠️ No hay clientes no preferenciales registrados.')
    else:
        print('✨✨ ------------------------------✨✨')
        print('------- Lista de clientes no preferenciales -------')
        print('✨✨ ------------------------------✨✨')
        for cliente in no_preferenciales:
            print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Dirección: {cliente['direccion']}")
            print('-----------------------------------')
    pausar()

def listar_clientes_preferenciales():
    preferenciales = [cliente for cliente in clientes.values() if cliente['preferencial']] #Filtra los clientes que tienen el valor True en la clave 'preferencial'.
#Solo los clientes preferenciales serán incluidos en la nueva lista.

    if not preferenciales:
        print('⚠️ No hay clientes preferenciales registrados.')
    else:
        print('✨✨ ------------------------------✨✨')
        print('------- Lista de clientes -------')
        print('✨✨ ------------------------------✨✨')
        for cliente in preferenciales:
            print(f"Cliente: {cliente['nombre']} {cliente['apellido']}")
            print(f"Correo: {cliente['correo']}")
            print(f"Teléfono: {cliente['telefono']}")
            print(f"Dirección: {cliente['direccion']}")
            print('-----------------------------------')
    pausar()

def main():
    cargar_clientes()  # Cargar clientes al iniciar el programa
    while True:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 1:
            registrar_clientes()
        elif opcion == 2:
            eliminar_cliente()
        elif opcion == 3:
            buscar_cliente()
        elif opcion == 4:
            listar_clientes()
        elif opcion == 5:
            listar_clientes_preferenciales()
        elif opcion == 6:
            print('\n👋 ¡Hasta luego! Gracias por usar el sistema.')
            break

if __name__ == "__main__":
    main()
