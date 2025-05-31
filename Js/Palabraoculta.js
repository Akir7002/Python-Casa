// Función para mostrar la palabra con espacios
function mostrarPalabra(palabra) {
    console.log(palabra.join(' '));
}

// Función para dibujar el ahorcado
function dibujarAhorcado(intentosRestantes, totalIntentos) {
    const errores = totalIntentos - intentosRestantes;
    
    console.log("  ______");
    console.log("  |    |");
    
    // Cabeza
    if(errores >= 1) console.log("  O    |");
    else console.log("       |");
    
    // Torso y brazos
    if(errores >= 4) console.log(" /|\\   |");
    else if(errores >= 3) console.log(" /|    |");
    else if(errores >= 2) console.log("  |    |");
    else console.log("       |");
    
    // Piernas
    if(errores >= 6) console.log(" / \\   |");
    else if(errores >= 5) console.log(" /     |");
    else console.log("       |");
    
    console.log("     _|_");
    console.log("    |   |______");
    console.log("    |__________|");
}

// Función principal del juego
function jugarPalabraOculta() {
    const readline = require('readline-sync');
    
    console.log("================================");
    console.log("    JUEGO DE LA PALABRA OCULTA  ");
    console.log("================================");
    
    // Usuario 1 ingresa la palabra
    console.log("\nJugador 1, escribe la palabra secreta:");
    const palabraSecreta = readline.question().toLowerCase();
    
    // Preparar variables
    const palabraAdivinada = Array(palabraSecreta.length).fill('_');
    let intentos = palabraSecreta.length;
    let adivinado = false;
    
    // Limpiar pantalla (forma simple)
    console.log('\n'.repeat(20));
    
    console.log("================================");
    console.log("    JUEGO DE LA PALABRA OCULTA  ");
    console.log("================================");
    
    console.log("\nJugador 2, adivina la palabra!");
    console.log("Tienes " + intentos + " intentos.");
    console.log("Palabra: ");
    mostrarPalabra(palabraAdivinada);
    
    // Juego principal
    while(intentos > 0 && !adivinado) {
        console.log("\n------------------------");
        console.log("Intento #" + (palabraSecreta.length - intentos + 1));
        console.log("Adivina una letra o escribe la palabra completa:");
        const intento = readline.question().toLowerCase();
        
        if(intento.length === 1) {
            const letra = intento[0];
            let acerto = false;
            
            for(let i = 0; i < palabraSecreta.length; i++) {
                if(palabraSecreta[i] === letra) {
                    palabraAdivinada[i] = letra;
                    acerto = true;
                }
            }
            
            if(acerto) {
                console.log("¡Bien! La letra '" + letra + "' está en la palabra.");
            } else {
                console.log("La letra '" + letra + "' no está. Pierdes un intento.");
                intentos--;
            }
            
            console.log("Palabra: ");
            mostrarPalabra(palabraAdivinada);
            
            // Verificar si se adivinó toda la palabra
            if(palabraAdivinada.join('') === palabraSecreta) {
                adivinado = true;
            }
        } else {
            if(intento === palabraSecreta) {
                adivinado = true;
            } else {
                console.log("Esa no es la palabra correcta. Pierdes un intento.");
                intentos--;
            }
        }
        
        console.log("Intentos restantes: " + intentos);
        dibujarAhorcado(intentos, palabraSecreta.length);
    }
    
    // Resultado final
    console.log("\n------------------------");
    if(adivinado) {
        console.log("¡FELICIDADES! Adivinaste la palabra: " + palabraSecreta);
        console.log("  ___________");
        console.log(" |           |");
        console.log(" |  GANASTE  |");
        console.log(" |___________|");
    } else {
        console.log("¡PERDISTE! La palabra era: " + palabraSecreta);
        console.log("  ___________");
        console.log(" |           |");
        console.log(" | PERDISTE  |");
        console.log(" |___________|");
    }
}

// Iniciar el juego
jugarPalabraOculta();