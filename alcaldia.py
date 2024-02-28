def calcular_bono(estrato, hijos):
    """
    Calcula el bono basado en el estrato y el número de hijos.
    """
    if hijos == 0:
        return 20000 if estrato == 1 else 16500
    elif hijos <= 2:
        return 25000 * hijos if estrato == 1 else 21500 * hijos
    else:
        return 30000 * hijos if estrato == 1 else 26500 * hijos

def obtener_input_entero(mensaje):
    """
    Obtiene una entrada entera del usuario con un mensaje personalizado.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def main():
    cantidad_estrato_1 = 0
    cantidad_estrato_2 = 0
    total_dinero_estrato_1 = 0
    total_dinero_estrato_2 = 0
    cantidad_sin_hijos = 0
    cantidad_1_2_hijos = 0
    cantidad_mas_3_hijos = 0
    total_dinero_sin_hijos = 0
    total_dinero_1_2_hijos = 0
    total_dinero_mas_3_hijos = 0
    total_dinero_bonos = 0
    
    while True:
        opcion = obtener_input_entero("¿Desea ingresar Datos? 1. Sí 2. No: ")
        
        if opcion == 2:
            break
        
        estrato = obtener_input_entero("Ingrese el estrato de la persona (1 o 2): ")
        hijos = obtener_input_entero("Ingrese el número de hijos: ")
        
        bono = calcular_bono(estrato, hijos)
        
        if estrato == 1:
            cantidad_estrato_1 += 1
            total_dinero_estrato_1 += bono
        elif estrato == 2:
            cantidad_estrato_2 += 1
            total_dinero_estrato_2 += bono
            
        if hijos == 0:
            cantidad_sin_hijos += 1
            total_dinero_sin_hijos += bono
        elif hijos <= 2:
            cantidad_1_2_hijos += 1
            total_dinero_1_2_hijos += bono
        else:
            cantidad_mas_3_hijos += 1
            total_dinero_mas_3_hijos += bono
            
        total_dinero_bonos += bono
    
    print("Cantidad de personas del estrato 1:", cantidad_estrato_1)
    print("Cantidad de personas del estrato 2:", cantidad_estrato_2)
    print("Total de dinero entregado al estrato 1:", total_dinero_estrato_1)
    print("Total de dinero entregado al estrato 2:", total_dinero_estrato_2)
    print("Cantidad de personas que no tienen hijos:", cantidad_sin_hijos)
    print("Cantidad de personas que tienen hasta 2 hijos:", cantidad_1_2_hijos)
    print("Cantidad de personas que tienen mayor o igual 3 hijos:", cantidad_mas_3_hijos)
    print("Total de dinero entregado a los beneficiarios que no tienen hijos:", total_dinero_sin_hijos)
    print("Total de dinero entregado a los beneficiarios que tienen hasta 2 hijos:", total_dinero_1_2_hijos)
    print("Total de dinero entregado a los beneficiarios que tienen mayor o igual 3 hijos:", total_dinero_mas_3_hijos)
    print("Total pagado por los bonos:", total_dinero_bonos)

if __name__ == "__main__":
    main()
