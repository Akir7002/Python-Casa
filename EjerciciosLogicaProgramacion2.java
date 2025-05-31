import java.util.Scanner;

public class EjerciciosLogicaProgramacion2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // ------------------------- CICLOS WHILE -------------------------
        System.out.println("\n--- Ejercicios con ciclos while ---\n");

        // Ejercicio 1: Ciclo que nunca se ejecuta
        System.out.println("Ejercicio 1:");
        int i = 10;
        while (i < 5) { // Condición falsa
            System.out.println("Este mensaje no se imprimirá.");
        }

    // Ejercicio 2: Ciclo infinito (descomentar para probar)
    // System.out.println("Ejercicio 2:");
    // while (true) {
    //     System.out.println("Bucle infinito.");
    // }

        // Ejercicio 3: Validar código ASCII de mayúsculas
        System.out.println("\nEjercicio 3:");
        int valor;
        do {
            System.out.print("Ingrese un entero (no ASCII de mayúscula): ");
            valor = scanner.nextInt();
        } while (valor >= 65 && valor <= 90);
        System.out.println("Valor válido.\n");

        // Ejercicio 4: Números del 1-100 con sus cuadrados
        System.out.println("Ejercicio 4:");
        int contador = 1;
        while (contador <= 100) {
            System.out.println(contador + "² = " + (contador * contador));
            contador++;
        }

        // Ejercicio 5: Impares (1-999) y Pares (2-1000)
        System.out.println("\nEjercicio 5:");
        System.out.println("Impares:");
        int num = 1;
        while (num <= 999) {
            System.out.print(num + " ");
            num += 2;
        }
        System.out.println("\nPares:");
        num = 2;
        while (num <= 1000) {
            System.out.print(num + " ");
            num += 2;
        }

        // Ejercicio 6: Pares descendentes desde n
        System.out.println("\n\nEjercicio 6:");
        System.out.print("Ingrese n (≥2): ");
        int n = scanner.nextInt();
        while (n >= 2) {
            if (n % 2 == 0) System.out.print(n + " ");
            n--;
        }

        // Ejercicio 7: Población país B supera a A
        System.out.println("\n\nEjercicio 7:");
        int año = 2022;
        double poblacionA = 25_000_000;
        double poblacionB = 18_900_000;
        while (poblacionB <= poblacionA) {
            poblacionA *= 1.02;
            poblacionB *= 1.03;
            año++;
        }
        System.out.println("Año: " + año);

        // ------------------------- CICLOS FOR -------------------------
        System.out.println("\n\n--- Ejercicios con ciclos for ---\n");

        // Ejercicio 8: 1-100 con cuadrados
        System.out.println("Ejercicio 8:");
        for (int j = 1; j <= 100; j++) {
            System.out.println(j + "² = " + (j * j));
        }

        // Ejercicio 9: Impares y Pares
        System.out.println("\nEjercicio 9:");
        System.out.println("Impares:");
        for (int j = 1; j <= 999; j += 2) {
            System.out.print(j + " ");
        }
        System.out.println("\nPares:");
        for (int j = 2; j <= 1000; j += 2) {
            System.out.print(j + " ");
        }

        // Ejercicio 10: Pares descendentes desde n
        System.out.println("\n\nEjercicio 10:");
        System.out.print("Ingrese n (≥2): ");
        n = scanner.nextInt();
        for (int j = n; j >= 2; j--) {
            if (j % 2 == 0) System.out.print(j + " ");
        }

        // Ejercicio 11: Factoriales hasta n
        System.out.println("\n\nEjercicio 11:");
        System.out.print("Ingrese n: ");
        n = scanner.nextInt();
        for (int j = 1; j <= n; j++) {
            long factorial = 1;
            for (int k = 1; k <= j; k++) factorial *= k;
            System.out.println(j + "! = " + factorial);
        }

        // Ejercicio 12: 2^n
        System.out.println("\nEjercicio 12:");
        System.out.print("Ingrese n: ");
        n = scanner.nextInt();
        long potencia = 1;
        for (int j = 0; j < n; j++) potencia *= 2;
        System.out.println("2^" + n + " = " + potencia);

        // Ejercicio 13: x^n
        System.out.println("\nEjercicio 13:");
        System.out.print("Ingrese x (real): ");
        double x = scanner.nextDouble();
        System.out.print("Ingrese n (natural): ");
        n = scanner.nextInt();
        double resultado = 1;
        for (int j = 0; j < n; j++) resultado *= x;
        System.out.println(x + "^" + n + " = " + resultado);

        // Ejercicio 14: Tablas de multiplicar
        System.out.println("\nEjercicio 14:");
        for (int j = 1; j <= 9; j++) {
            System.out.println("\nTabla del " + j + ":");
            for (int k = 1; k <= 10; k++) {
                System.out.println(j + " x " + k + " = " + (j * k));
            }
        }

        scanner.close();
    }
}