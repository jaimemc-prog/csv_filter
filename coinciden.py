# Abrir y leer el contenido de los archivos de texto
with open("doc1.txt", "r") as f1, open("doc2.txt", "r") as f2:
    contenido1 = f1.readlines()
    contenido2 = f2.readlines()

# Eliminar los caracteres de nueva línea ("\n")
contenido1 = [linea.strip() for linea in contenido1]
contenido2 = [linea.strip() for linea in contenido2]

# Contar las coincidencias entre los contenidos de los archivos
coincidencias = 0
for linea1 in contenido1:
    for linea2 in contenido2:
        if linea1 == linea2:
            coincidencias += 1

# Mostrar el número de coincidencias
print("Número de coincidencias: ", coincidencias)
