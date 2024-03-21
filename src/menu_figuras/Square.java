package menu_figuras;

import menu_figuras.GeometricShape;

class Square extends GeometricShape {

    private float base;
    private float height;

    public Square(String name, float base, float height) {
        super(name);
        this.base = base;
        this.height = height;
    }

    @Override
    public float calculateArea() {
        return base * height;
    }

    @Override
    public float calculatePerimeter() {
        return 2 * (base + height);
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
