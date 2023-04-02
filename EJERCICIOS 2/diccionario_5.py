# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

subjects = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

total_creditos = 0

for key,value in subjects.items():
    print(f"{key} tiene {value} creditos")
    total_creditos += value
print(f"Numero total de creditos es {total_creditos}")