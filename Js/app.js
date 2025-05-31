// Importa el módulo 'fs' para manejar archivos
const fs = require('fs'); 
// Importa el módulo 'path' para manejar rutas de archivos
const path = require('path'); 
// Importa el módulo 'readline-sync' para entrada de datos por consola
const readline = require('readline-sync'); 

// Define la ruta del archivo donde se guardarán las tareas
const DB_FILE = path.join(__dirname, 'tareas.json');
// Define los estados válidos para las tareas
const VALID_STATUSES = ['pendiente', 'en progreso', 'completada'];

// --- Funciones de utilidad ---

// Lee las tareas desde el archivo JSON
function readTasksFromFile() {
    try {
        // Si el archivo no existe, lo crea vacío
        if (!fs.existsSync(DB_FILE)) {
            fs.writeFileSync(DB_FILE, '{}');
            return {};
        }
        // Lee el contenido del archivo y lo convierte a objeto
        const data = fs.readFileSync(DB_FILE, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        // Maneja errores de lectura o parseo
        console.error(' ❌ Error al leer el archivo de tareas:', error.message);
        return {};
    }
}

// Escribe las tareas en el archivo JSON
function writeTasksToFile(tasks) {
    try {
        fs.writeFileSync(DB_FILE, JSON.stringify(tasks, null, 2));
        return true;
    } catch (error) {
        // Maneja errores de escritura
        console.error('❌  Error al guardar tareas:', error.message);
        return false;
    }
}

// Valida que la cédula solo contenga números
function validateCedula(cedula) {
    return /^\d+$/.test(cedula); 
}

// Valida que el estado de la tarea sea uno de los permitidos
function validateStatus(status) {
    return VALID_STATUSES.includes(status.toLowerCase());
}

// --- Funcionalidades principales ---

// Registra un nuevo usuario en el sistema
function registrarUsuario() {
    console.log('\n--- Registrar Nuevo Usuario ---');
    
    // Solicita el nombre del usuario
    const nombre = readline.question('Ingrese el nombre del usuario: ').trim();
    if (!nombre) {
        console.log(' ⚠️  El nombre no puede estar vacío.');
        return;
    }

    // Solicita la cédula y la valida
    let cedula;
    while (true) {
        cedula = readline.question('Ingrese la cédula del usuario (solo números): ').trim();
        if (validateCedula(cedula)) break;
        console.log('⚠️  Cédula inválida. Solo se permiten números.');
    }

    // Lee las tareas actuales
    const tasks = readTasksFromFile();
    
    // Verifica si la cédula ya está registrada
    if (tasks[cedula]) {
        console.log(` ❌  La cédula ${cedula} ya está registrada para el usuario: ${tasks[cedula].Usuario}`);
        return;
    }

    // Crea un nuevo usuario con datos vacíos de tarea
    tasks[cedula] = {
        Usuario: nombre,
        titulo: '',
        descripcion: '',
        estado: '',
        fechaCreacion: new Date().toISOString()
    };

    // Guarda los cambios en el archivo
    if (writeTasksToFile(tasks)) {
        console.log(`Usuario ${nombre} con cédula ${cedula} registrado exitosamente ✅ .`);
    }
}

// Registra una nueva tarea para un usuario existente
function registrarTarea() {
    console.log('\n--- Registrar Nueva Tarea ---');
    
    // Solicita la cédula y la valida
    const cedula = readline.question('Ingrese la cédula del usuario: ').trim();
    if (!validateCedula(cedula)) {
        console.log('❌  Cédula inválida.');
        return;
    }

    // Lee las tareas actuales
    const tasks = readTasksFromFile();
    // Verifica si el usuario existe
    if (!tasks[cedula]) {
        console.log('⚠️  No existe un usuario con esa cédula. Registre el usuario primero.');
        return;
    }

    // Solicita el título de la tarea
    const titulo = readline.question('Ingrese el título de la tarea: ').trim();
    if (!titulo) {
        console.log('⚠️ El título no puede estar vacío.');
        return;
    }

    // Solicita la descripción de la tarea
    const descripcion = readline.question('Ingrese la descripción: ').trim();
    
    // Solicita y valida el estado de la tarea
    let estado;
    while (true) {
        estado = readline.question(`Ingrese el estado (${VALID_STATUSES.join('/')}): `).trim().toLowerCase();
        if (validateStatus(estado)) break;
        console.log(`Estado inválido. Use uno de: ${VALID_STATUSES.join(', ')}`); // Valid_status es una constante que contiene los estados válidos
    }

    // Actualiza la tarea del usuario
    tasks[cedula] = {
        ...tasks[cedula],
        titulo,
        descripcion,
        estado,
        fechaActualizacion: new Date().toISOString()
    };

    // Guarda los cambios en el archivo
    if (writeTasksToFile(tasks)) {
        console.log(`Tarea "${titulo}" registrada para ${tasks[cedula].Usuario} (${cedula}) exitosamente ✅ .`);
    }
}

// Lista todas las tareas de un usuario por su cédula
function listarTareasPorUsuario() {
    console.log('\n--- Lista de Tareas por Usuario ---');
    
    // Solicita la cédula y la valida
    const cedula = readline.question('Ingrese la cédula del usuario: ').trim();
    if (!validateCedula(cedula)) {
        console.log('  ❌  Cédula inválida.');
        return;
    }

    // Lee las tareas actuales
    const tasks = readTasksFromFile();
    const tarea = tasks[cedula];

    // Verifica si el usuario existe
    if (!tarea) {
        console.log('⚠️  No se encontró usuario con esa cédula.');
        return;
    }

    // Muestra la información de la tarea
    console.log(`\nTareas de ${tarea.Usuario} (${cedula}):`);
    console.log(`1. Título: ${tarea.titulo}`);
    console.log(`2.   Descripción: ${tarea.descripcion}`);
    console.log(`3.   Estado: ${tarea.estado}`);
    console.log(`   Creada: ${new Date(tarea.fechaCreacion).toLocaleString()}`);
    if (tarea.fechaActualizacion) {
        console.log(`   Actualizada: ${new Date(tarea.fechaActualizacion).toLocaleString()}`);  // Muestra la fecha de actualización si existe
    }
}

// Lista solo las tareas pendientes de un usuario
function listarTareasPendientes() {
    console.log('\n--- Tareas Pendientes por Usuario ---');
    
    // Solicita la cédula y la valida
    const cedula = readline.question('Ingrese la cédula del usuario: ').trim();
    if (!validateCedula(cedula)) {
        console.log('  ❌  Cédula inválida.');
        return;
    }

    // Lee las tareas actuales
    const tasks = readTasksFromFile();
    const tarea = tasks[cedula];

    // Verifica si el usuario existe
    if (!tarea) {
        console.log('⚠️  No se encontró usuario con esa cédula.');
        return;
    }

    // Verifica si la tarea está pendiente
    if (tarea.estado !== 'pendiente') {
        console.log(`⚠️  El usuario ${tarea.Usuario} no tiene tareas pendientes.`);
        return;
    }

    // Muestra la información de la tarea pendiente
    console.log(`\nTareas pendientes de ${tarea.Usuario} (${cedula}):`);
    console.log(`1. Título: ${tarea.titulo}`);
    console.log(`2. Descripción: ${tarea.descripcion}`);
    console.log(`3. Creada: ${new Date(tarea.fechaCreacion).toLocaleString()}`);
}

// --- Menú principal ---
// Muestra el menú principal de opciones
function mostrarMenu() {
    console.log(`
✨✨ ----------------------------------------------✨✨
--- Bienvenido al sistema de gestion de tareas ---
✨✨ ----------------------------------------------✨✨
[1] ➕   Registrar nuevo usuario
[2] 🖋️   Registrar tarea
[3] 🔎   Listar Tareas
[4] 👀   Listar tareas pendientes
[5] 👣   Salir
✨✨ ----------------------------------------------✨✨
`);

}

// Función principal que ejecuta el menú y las opciones
function main() {
    let opcion;
    
    do {
        mostrarMenu();
        opcion = readline.question('Seleccione una opción: ').trim();

        switch (opcion) {
            case '1':
                registrarUsuario();
                break;
            case '2':
                registrarTarea();
                break;
            case '3':
                listarTareasPorUsuario();
                break;
            case '4':
                listarTareasPendientes();
                break;
            case '5':
                console.log('Saliendo del sistema, Gracias por usar nuestros servicios 😉...');
                break;
            default:
                console.log('Opción no válida. Intente nuevamente.');
        }

        // Espera que el usuario presione Enter antes de continuar
        if (opcion !== '5') {
            readline.question('\nPresione Enter para continuar...');
        }
    } while (opcion !== '5');
}

// Inicia la aplicación
main();