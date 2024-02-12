package main.java.package1;

import java.util.Scanner;

@SuppressWarnings("resource")
public class AppFinanciera {
    public static void main(String[] args) {
        System.out.println("¡Bienvenido a la aplicación financiera!");

        // Simular un login básico
        Scanner scanner = new Scanner(System.in); // <- Crea un objeto Scanner para leer la entrada del usuario
        System.out.print("Ingrese su nombre de usuario: ");
        String username = scanner.nextLine();
        System.out.println("¡Hola, " + username + "!");

        // Menú de usuario
        int opcion;
        do {
            System.out.println("\nMenú:");
            System.out.println("1. Calcular interés compuesto");
            System.out.println("2. Calcular interés simple");
            System.out.println("3. Calcular tiempo para duplicar el capital");
            System.out.println("4. Tablas de multiplicar");
            System.out.println("0. Salir");
            System.out.print("Ingrese una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    calcularInteresCompuesto();
                    break;
                case 2:
                    calcularInteresSimple();
                    break;
                case 3:
                    calcularTiempoParaDuplicarCapital();
                    break;
                case 4:
                    tablasMultiplicar();
                    break;
                case 0:
                    System.out.println("Saliendo...");
                    System.out.println("Hasta luego...");
                    break;
                default:
                    System.out.println("Opción inválida. Inténtelo de nuevo.");
                    break;
            }
        } while (opcion != 0); // <- Repite el menú hasta que el usuario elija salir

        scanner.close();
    }

    // Función para calcular el tiempo necesario para duplicar el capital
    private static void calcularTiempoParaDuplicarCapital() {
        double capital, tasa;

        Scanner scanner = new Scanner(System.in);
        System.out.println("\nCálculo de tiempo para duplicar el capital");
        System.out.println("=============================");

        System.out.print("Ingrese el capital inicial: ");
        capital = scanner.nextDouble();
        System.out.print("Ingrese la tasa de interés (e.j: 19): ");
        tasa = scanner.nextDouble() / 100;

        // Verifica que la tasa de interés sea mayor que cero
        if (tasa <= 0) {
            System.out.println("La tasa de interés debe ser mayor que cero. Inténtelo de nuevo.");
            return; // <- Sale de la función
        }

        // llamada a la función para calcular el tiempo necesario para duplicar el capital
        double tiempo = calcularTiempoDuplicarCapital(tasa); // <- esta es la función que se va a implementar
        System.out.println("El tiempo necesario para duplicar un capital de " + capital + " es: " + tiempo + " años");
    }

    // Función para imprimir las tablas de multiplicar
    private static void tablasMultiplicar() {
        int valores = 10; // <- Número de valores a imprimir
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el número de la tabla de multiplicar: ");
        int numero = scanner.nextInt();

        // Imprime la tabla de multiplicar
        for (int i = 1; i <= valores; i++) {
            System.out.println(numero + " x " + i + " = " + numero * i);
        }
    }

    // Función para calcular el interés compuesto
    private static void calcularInteresCompuesto() {
        double capital, tasa;
        int tiempo;

        Scanner scanner = new Scanner(System.in);
        System.out.println("\nCálculo de interés compuesto");
        // Imprime la forma de calcular el interés compuesto
        System.out.println("=============================");
        System.out.println("Fórmula: M = C * (1 + i)^n");
        System.out.println("Donde:");
        System.out.println("M = monto final");
        System.out.println("C = capital inicial");
        System.out.println("i = tasa de interés");
        System.out.println("n = tiempo en años");
        System.out.println("=============================");

        System.out.print("Ingrese el capital inicial: ");
        capital = scanner.nextFloat();
        System.out.print("Ingrese la tasa de interés (e.j: 19): ");
        tasa = scanner.nextFloat() / 100;
        System.out.print("Ingrese el tiempo en años: ");
        tiempo = scanner.nextInt();

        // llamada a la función para calcular el monto final con interés compuesto
        calcularMontoFinalCompuesto(capital, tasa, tiempo); // <- esta es la función que se va a implementar
    }

    private static void calcularInteresSimple() {
        double capital, tasa;
        int tiempo;

        Scanner scanner = new Scanner(System.in);
        System.out.println("\nCálculo de interés simple");

        // Imprime la forma de calcular el interés simple
        System.out.println("=============================");
        System.out.println("Fórmula: I = C * i * n");
        System.out.println("Donde:");
        System.out.println("I = interés");
        System.out.println("C = capital inicial");
        System.out.println("i = tasa de interés");
        System.out.println("n = tiempo en años");
        System.out.println("=============================");

        System.out.print("Ingrese el capital inicial: ");
        capital = scanner.nextFloat();
        System.out.print("Ingrese la tasa de interés (e.j: 19): ");
        tasa = scanner.nextFloat() / 100;
        System.out.print("Ingrese el tiempo en años: ");
        tiempo = scanner.nextInt();

        // llamada a la función para calcular el monto final con interés simple
        calcularMontoFinalSimple(capital, tasa, tiempo); // <- esta es la función que se va a implementar
    }

    // Función para calcular el monto final con interés compuesto
    private static void calcularMontoFinalCompuesto(double capitalInicial, double tasaInteresAnual, int tiempoAnios) {
        // Fórmula: M = C * (1 + i)^n
        // pow es una función matemática que representa la potencia
        double montoFinal = capitalInicial * Math.pow(1 + tasaInteresAnual, tiempoAnios);
        System.out.println("El monto final después de " + tiempoAnios + " años es: " + montoFinal);
    }

    // Función para calcular el monto final con interés simple
    private static void calcularMontoFinalSimple(double capitalInicial, double tasaInteresAnual, int tiempoAnios) {
        // Fórmula: M = C * (1 + i * n)
        double montoFinal = capitalInicial * (1 + tasaInteresAnual * tiempoAnios);
        System.out.println("El monto final después de " + tiempoAnios + " años es: " + montoFinal);
    }

    // Función para calcular el tiempo necesario para duplicar el capital
    private static double calcularTiempoDuplicarCapital(double tasaInteresAnual) {
        // Fórmula: n = log(2) / log(1 + i)
        // log es una función matemática que representa el logaritmo
        double tiempo = Math.log(2) / Math.log(1 + tasaInteresAnual);
        return tiempo; // <- Devuelve el tiempo necesario para duplicar el capital
    }
}