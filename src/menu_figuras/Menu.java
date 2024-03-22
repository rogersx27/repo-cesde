package menu_figuras;

import java.util.ArrayList;
import java.util.Scanner;

public class Menu {

    private final Scanner scanner;
    private final RegisterInteractions register;

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

    private ArrayList<Object> askData() {
        InputData inputData = new InputData();
        ArrayList<Object> data = inputData.getData();
        return data;
    }

    private Triangle createTriangle() {
        ArrayList<Object> data = askData();
        Triangle triangle = new Triangle(data.get(0).toString(), (float) data.get(1), (float) data.get(2));
        return triangle;
    }

    private Square createSquare() {
        ArrayList<Object> data = askData();
        Square square = new Square(data.get(0).toString(), (float) data.get(1), (float) data.get(2));
        return square;
    }

    private void calculateAreaOfTriangle() {
        Triangle triangle = createTriangle();

        String name = triangle.getName();
        float base = triangle.getBase();
        float height = triangle.getHeight();

        register.addRegister(name, base, height, triangle.calculateArea(), 0, 0);
        System.out.println("The area of the triangle " + triangle.getName() + " is: " + triangle.calculateArea());
    }

    private void calculatePerimeterOfTriangle() {
        Triangle triangle = createTriangle();

        String name = triangle.getName();
        float base = triangle.getBase();
        float height = triangle.getHeight();

        register.addRegister(name, base, height, 0, triangle.calculatePerimeter(), 0);
        System.out.println("The perimeter of the triangle " + triangle.getName() + " is: " + triangle.calculatePerimeter());
    }

    private void calculateHypotenuseOfTriangle() {
        Triangle triangle = createTriangle();

        String name = triangle.getName();
        float base = triangle.getBase();
        float height = triangle.getHeight();

        register.addRegister(name, base, height, 0, 0, triangle.calculateHypotenuse());
        System.out.println("The hypotenuse of the triangle " + triangle.getName() + " is: " + triangle.calculateHypotenuse());
    }

    private void calculateAreaOfSquare() {
        Square square = createSquare();

        String name = square.getName();
        float base = square.getBase();
        float height = square.getHeight();

        register.addRegister(name, base, height, square.calculateArea(), 0, 0);
        System.out.println("The area of the square " + square.getName() + " is: " + square.calculateArea());
    }

    private void calculatePerimeterOfSquare() {
        Square square = createSquare();

        String name = square.getName();
        float base = square.getBase();
        float height = square.getHeight();

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
