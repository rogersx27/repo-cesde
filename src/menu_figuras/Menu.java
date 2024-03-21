package menu_figuras;

import java.util.Scanner;
public class Menu {

    private Scanner scanner;
    private RegisterInteractions register;

    public Menu() {
    this.scanner = new Scanner(System.in);
    this.register = new RegisterInteractions();
    }

    public void showMenu() {
        System.out.println("1. Calculate the area of a triangle");
        System.out.println("2. Calculate the perimeter of a triangle");
        System.out.println("3. Calculate the hypotenuse of a triangle");
        System.out.println("4. Calculate the area of a square");
        System.out.println("5. Calculate the perimeter of a square");
        System.out.println("6. Show registers");
        System.out.println("0. Exit");
    }

    public void start() {
        int option;
        do {
            System.out.println("Choose an option: ");
            showMenu();
            option = scanner.nextInt();
            switch (option) {
                case 1:
                    calculateAreaOfTriangle();
                    break;
                case 2:
                    calculatePerimeterOfTriangle();
                    break;
                case 3:
                    calculateHypotenuseOfTriangle();
                    break;
                case 4:
                    calculateAreaOfSquare();
                    break;
                case 5:
                    calculatePerimeterOfSquare();
                    break;
                case 6:
                    showRegisters();
                    break;
                case 0:
                    System.out.println("Goodbye!");
                    break;
                default:
                    System.out.println("Invalid option");
            }
        } while (option != 0);
    }

    private void calculateAreaOfTriangle() {
        System.out.println("Enter the name of the triangle: ");
        String name = scanner.next();
        System.out.println("Enter the base of the triangle: ");
        float base = scanner.nextFloat();
        System.out.println("Enter the height of the triangle: ");
        float height = scanner.nextFloat();
        Triangle triangle = new Triangle(name, base, height);
        register.addRegister(name, base, height, triangle.calculateArea(), 0, 0);
        System.out.println("The area of the triangle " + triangle.getName() + " is: " + triangle.calculateArea());
    }

    private void calculatePerimeterOfTriangle() {
        System.out.println("Enter the name of the triangle: ");
        String name = scanner.next();
        System.out.println("Enter the base of the triangle: ");
        float base = scanner.nextFloat();
        System.out.println("Enter the height of the triangle: ");
        float height = scanner.nextFloat();
        Triangle triangle = new Triangle(name, base, height);
        register.addRegister(name, base, height, 0, triangle.calculatePerimeter(), 0);
        System.out.println("The perimeter of the triangle " + triangle.getName() + " is: " + triangle.calculatePerimeter());
    }

    private void calculateHypotenuseOfTriangle() {
        System.out.println("Enter the name of the triangle: ");
        String name = scanner.next();
        System.out.println("Enter the base of the triangle: ");
        float base = scanner.nextFloat();
        System.out.println("Enter the height of the triangle: ");
        float height = scanner.nextFloat();
        Triangle triangle = new Triangle(name, base, height);
        register.addRegister(name, base, height, 0, 0, triangle.calculateHypotenuse());
        System.out.println("The hypotenuse of the triangle " + triangle.getName() + " is: " + triangle.calculateHypotenuse());
    }

    private void calculateAreaOfSquare() {
        System.out.println("Enter the name of the square: ");
        String name = scanner.next();
        System.out.println("Enter the base of the square: ");
        float base = scanner.nextFloat();
        System.out.println("Enter the height of the square: ");
        float height = scanner.nextFloat();
        Square square = new Square(name, base, height);
        register.addRegister(name, base, height, square.calculateArea(), 0, 0);
        System.out.println("The area of the square " + square.getName() + " is: " + square.calculateArea());
    }

    private void calculatePerimeterOfSquare() {
        System.out.println("Enter the name of the square: ");
        String name = scanner.next();
        System.out.println("Enter the base of the square: ");
        float base = scanner.nextFloat();
        System.out.println("Enter the height of the square: ");
        float height = scanner.nextFloat();
        Square square = new Square(name, base, height);
        register.addRegister(name, base, height, 0, square.calculatePerimeter(), 0);
        System.out.println("The perimeter of the square " + square.getName() + " is: " + square.calculatePerimeter());
    }

    private void showRegisters() {
        register.showRegisters();
    }
    public void closeScanner() {
        scanner.close();
    }
}
