package menu_figuras;

import java.util.*;


public class RegisterInteractions {
    private List<Map<String, Object>> registers;

    public RegisterInteractions() {
        this.registers = new ArrayList<>();
    }

    public void addRegister(String name, float base, float height, float area, float perimeter, float hypotenuse) {
        Map<String, Object> registro = new HashMap<>();
        registro.put("nombreFigura", name);
        registro.put("base", base);
        registro.put("altura", height);
        registro.put("area", area == 0 ? "none" : area);
        registro.put("perimetro", perimeter == 0 ? "none" : perimeter);
        registro.put("hipotenusa", hypotenuse == 0 ? "none" : hypotenuse);
        registers.add(registro);
    }

    public void showRegisters() {
        if (registers.isEmpty()) {
            System.out.println("No hay registros aún ...");
            return;
        }

        for (int i = 0; i < registers.size(); i++) {
            Map<String, Object> registro = registers.get(i);
            System.out.println("Registro " + (i + 1) + "-->" +
                    " Nombre: " + registro.get("nombreFigura") + "|" +
                    " Base: " + registro.get("base") + "|" +
                    " Altura: " + registro.get("altura") + "|" +
                    " Perimetro: " + registro.get("perimetro") + "|" +
                    " Area: " + registro.get("area") + "|" +
                    " Hipotenusa: " + registro.get("hipotenusa"));
        }
    }


}
