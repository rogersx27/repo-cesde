package menu_figuras;


import java.util.ArrayList;
import java.util.Scanner;

public class InputData {
    private String name;
    private float base;
    private float height;

    public InputData() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the name of the figure: ");
        this.name = scanner.nextLine();
        System.out.println("Enter the base of the figure: ");
        this.base = scanner.nextFloat();
        System.out.println("Enter the height of the figure: ");
        this.height = scanner.nextFloat();
    }

    public ArrayList<Object> getData() {
        ArrayList<Object> data = new ArrayList<>();
        data.add(name);
        data.add(base);
        data.add(height);
        return data;
    }
}
