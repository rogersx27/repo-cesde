package menu_figuras;

abstract class GeometricShape {
    private String name;

    public GeometricShape(String name) {
        this.name = name;
    }

    public abstract float calculateArea();
    public abstract float calculatePerimeter();

    public String getName() {
        return name;
    }
}
