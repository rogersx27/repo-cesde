package menu_figuras;

import menu_figuras.GeometricShape;

class Triangle extends GeometricShape {
    private float base;
    private float height;

    public Triangle(String name, float base, float height) {
        super(name);
        this.base = base;
        this.height = height;
    }

    @Override
    public float calculateArea() {
        return (base * height) / 2;
    }

    @Override
    public float calculatePerimeter() {
        return base + height + calculateHypotenuse();
    }

    public float calculateHypotenuse() {
        return (float) Math.sqrt(Math.pow(base, 2) + Math.pow(height, 2));
    }

    public float getBase() {
        return base;
    }

    public void setBase(float base) {
        this.base = base;
    }

    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
}
