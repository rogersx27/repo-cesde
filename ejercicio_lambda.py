estudiantes = {
    'Juan': [75, 90, 50, 30, 65, 80, 95, 45, 55, 70],
    'Maria': [88, 40, 77, 90, 55, 80, 95, 45, 55, 70],
    'Pedro': [75, 90, 50, 30, 65, 80, 95, 45, 55, 70]
    }

promedio = lambda calificaciones: sum(calificaciones) / len(calificaciones)
print(promedio(estudiantes['Maria']))
