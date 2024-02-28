package main.java.package1;

import java.util.Objects;
import java.util.Scanner;

public class figuras {
    public static void main(String[] args) {
        // Simular un login básico
        String username = (String) input("Ingrese su nombre: ");
        System.out.println("¡Hola, " + username + "!");

        // Menú de usuario
        int opcion;
        do {
            System.out.println("\nMenú:");
            System.out.println("1. Calcular área del rectángulo");
            System.out.println("2. Calcular radio de una circunferencia");
            System.out.println("3. Analiza un string");
            System.out.println("4. Calculo de vacaciones");
            System.out.println("0. Salir");
            opcion = (int) input("Ingrese una opción: ");

            switch (opcion) {
                case 1:
                    calcularArea();
                    break;
                case 2:
                    calcularCircunferencia();
                    break;
                case 3:
                    String text =(String) input("Ingrese la palabra a analizar: ");
                    boolean result = analisisString(text);
                    System.out.println(result);
                    break;
                case 4:
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
    }

    private static Object input(String mensaje) {
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.println(mensaje);
        if (scanner.hasNextInt()) {
            return scanner.nextInt();
        } else if (scanner.hasNextDouble()) {
            return scanner.nextDouble();
        } else if (scanner.hasNextBoolean()) {
            return scanner.nextBoolean();
        } else {
            return scanner.nextLine(); // Leer una línea como String por defecto
        }
    }

    private static void calcularArea() {
        // Submenú
        int opcion;
        do {
            System.out.println("\nMenú:");
            System.out.println("1. Triángulo");
            System.out.println("2. Rectángulo");
            System.out.println("3. Cuadrado");
            System.out.println("4. Círculo");
            System.out.println("0. Salir");
            opcion = (int) input("Ingrese una opción: ");

            switch (opcion) {
                case 1:
                    System.out.println("Tríángulo");
                    System.out.println("-----------------");
                    System.out.println("| A = b * h / 2 |");
                    System.out.println("-----------------");

                    float base =(float) input("Valor de la base:");
                    float altura =(float) input("Valor de la altura:");

                    float area = (base * altura) / 2;

                    System.out.println("El área es: " + area);
                    break;
                case 2:
                    area("Rectángulo");
                    break;
                case 3:
                    area("Cuadrado");
                    break;
                case 4:
                    System.out.println("Círculo");
                    System.out.println("-----------------");
                    System.out.println("| A = PI * r^2 |");
                    System.out.println("-----------------");

                    float radio =(float) input("Valor del radio:");

                    double areaC = ( (Math.PI) * Math.pow(radio, 2) );

                    System.out.println("El área es: " + areaC);
                    break;
                case 0:
                    System.out.println("Saliendo...");
                    break;
                default:
                    System.out.println("Opción inválida. Inténtelo de nuevo.");
                    break;
            }
        } while (opcion != 0); // <- Repite el menú hasta que el usuario elija salir
    }

    private static void area(String tipo) {
        System.out.println(tipo);
        System.out.println("-----------------");
        System.out.println("|   A = a * b   |");
        System.out.println("-----------------");

        float lado1 =(float) input("Valor de la base:");
        float lado2 =(float) input("Valor de la altura:");

        float area = (lado1 * lado2);

        System.out.println("El área es: " + area);
    }

    private static  void calcularCircunferencia() {
        System.out.println("Círculo");
        System.out.println("------------------");
        System.out.println("| L = 2 * PI * r |");
        System.out.println("------------------");

        float radio =(float) input("Valor del radio:");

        double circunferencia = ( 2 * (Math.PI) * radio );

        System.out.println("La circunferencia es: " + circunferencia);
    }

    private static boolean analisisString(String text) {
        String copy = text;
        boolean result = false;

        boolean containsAt = copy.contains("@");

        if (containsAt) {
            result = true;
        }

        return result;
    }
}

