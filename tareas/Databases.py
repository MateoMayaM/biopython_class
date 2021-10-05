'''
NAME
       Databases.py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Este programa tiene dos partes. En la primera empleando Entrez.einfo y Entrez.read, 
        se imprime la descripción de los campos FieldList "ECNO" y LinkList "protein_protein_small_genome" de la base de 
        datos "protein". En la segunda parte se pide al usuario un nombre para el archivo que se va a crear, un autor y 
        palabras que quiera buscar e los títulos y con ellas se crea un archivo que contiene los ids de los artículos que
        cumplen con los requisitos.

CATEGORY
       Data Bases.

EXAMPLE:
        Tarea 1: 
        
        Input: No necesita un input.
            
        Output:
            Primera tarea:
            Descripción ECNO -> EC number for enzyme or CAS registry number
            Descripción protein_protein_small_genome -> All proteins from this genome

        Tarea 2.

        Input:
            Ingresa el nombre del autor: Amaranta Manrique
            Ingresa la primera palabra que te gustaría encontrar en el título: alacranes
            Ingresa la segunda palabra que te gustaría encontrar en el título: etica
            Elige el nombre del archivo en el que se guardarán los ids de los artículos: ids.txt

        Output:
            No se encontraron artículos con esa búsqueda.


LIGA DE GITHUB: [https://github.com/MateoMayaM/biopython_class/blob/master/tareas/Databases.py
'''




# Importación de librerías.
from Bio import Entrez


def ids (name, autor, palabra1, palabra2):

    """
Esta función recibe el nombre del archivo en el que el usuario guardará los ids de los artículos, el autor que quiere
buscar y las palabras que le gustaría encontrar e el título. Con esta información se crea un archivo que contiene los ids
de los artículos que se hayan encontrado.
    """

# Con los inputs del usuario crear el term que usaremos e el handle.
    term = autor + "[AUTH]" + " AND (" + palabra1 + "[Title]" + " OR " + palabra2 + "[Title]" + ")"
# Hadle con esearch
    handle = Entrez.esearch(db="pubmed", term=term)
    resultados = Entrez.read(handle)
# Acceder a los ids.
    ids = resultados["IdList"]
#Si no se encuentra artículos imprimir un mensaje.
    if len(ids) == 0:
        print ("No se encontraron artículos con esa búsqueda.")
    else:
# Crear el archivo en el que escribiremos los ids
        file = open(name, "x")
# Escribir los ids en el archivo de texto.
        file.write("Resultados de la búsqueda:\n")
        for id in ids:
            file.write(id + "\n")
        file.close()
        return file

# Primera tarea.

# Correo
Entrez.email = "matteo.mayam@outlook.com"

# Handle con einfo.
handle = Entrez.einfo(db = "protein")
record = Entrez.read(handle)

print ("Primera tarea:")

# Para cada campo en el record si el campo se llama ECNO, se imprime su descripción.
for field in record["DbInfo"]["FieldList"]:
  if field["Name"] == "ECNO":
      print(f"Descripción ECNO ->", field["Description"])

# Para cada campo en el record si el campo se llama protein_protein_small_genome, se imprime su descripción.
for field in record["DbInfo"]["LinkList"]:
    if field["Name"] == "protein_protein_small_genome":
        print(f"Descripción protein_protein_small_genome ->", field["Description"])

handle.close()


# Segunda tarea.
print ("------------------\nSegunda tarea:")

# Pedir al usuario el nombre de archivo, el ombre del autor y las palabras que quiere buscar e los títulos.
autor = input("Ingresa el nombre del autor: ")
palabra1 = input("Ingresa la primera palabra que te gustaría encontrar en el título: ")
palabra2 = input("Ingresa la segunda palabra que te gustaría encontrar en el título: ")
name = input("Elige el nombre del archivo en el que se guardarán los ids de los artículos: ")

# Llamada a la función ids.
ids(name, autor, palabra1, palabra2)

