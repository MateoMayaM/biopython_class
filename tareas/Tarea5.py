'''
NAME
       Abstracts.py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Este programa recibe el nombre de un autor y dos palabras que podríamos encontrar en el título de sus artículos.
        A partir de estos, se encuentran los artículos qwue tengan esta información, se recuperan sus abstracts y se
        obtienen los ids de artículos en los que son citados.

CATEGORY
       Abstracts.

EXAMPLE:
        Input:
            Ingresa el nombre del autor: Giampaolo
            Ingresa la primera palabra que te gustaría encontrar en el título: cancer
            Ingresa la segunda palabra que te gustaría encontrar en el título: heterogeneous
            Elige el nombre del archivo en el que se guardarán los ids de los artículos: ids.txt
            Introduce el nombre del archivo en el que se van a guardar los abstractswtwtwtw: abstracts.txt

        Output:



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
        file.write("Resultados de la búsqueda:\n" + str(ids))
        '''
        for id in ids:
            file.write(id + "\n")
        file.close()
'''

        return file

def abstracts(name_abs, ids_list):
    """
    Esta función recibe el nombre del archivo en el que se van a guardar los abstracts y la lista con los ids de
    loa artículos que nos interesan y escribe un archivo con los abstracts y los ids de los artículos que citan a los
    artículos que nos interesan.
    """
# Obtener los abstracts
    fetch_handle = Entrez.efetch(db="pubmed", id=ids_list, rettype="abstract", retmode="text")
    abst = fetch_handle.read()
    fetch_handle.close()
    file2 = open (name_abs, "w")
    file2.write(abst)

# Obtener las citas
    citas = Entrez.read(Entrez.elink(dbfrom="pubmed", db="pmc", LinkName="pubmed_pmc_refs", from_uid=ids_list))
    for i, j in enumerate (ids_list):
        citation_ids = f'El artículo {j} tiene citas en los artículos: {[link["Id"] for link in citas[i]["LinkSetDb"][0]["Link"]]}'
        file2.write(citation_ids)
        file2.write('\n')
    file2.close()

# Correo
Entrez.email = "matteo.mayam@outlook.com"

# Pedir al usuario el nombre de archivo, el nombre del autor y las palabras que quiere buscar en los títulos.
autor = input("Ingresa el nombre del autor: ")
palabra1 = input("Ingresa la primera palabra que te gustaría encontrar en el título: ")
palabra2 = input("Ingresa la segunda palabra que te gustaría encontrar en el título: ")
name = input("Elige el nombre del archivo en el que se guardarán los ids de los artículos: ")

# Llamada a la función ids.
ids(name, autor, palabra1, palabra2)

# Abrir el archivo donde guardamos los ids.
archivo = open(name, "r")
archivo = archivo.readlines()

# Guardar los ids en una lista.
ids_list = archivo[1]
ids_list = ids_list.replace("[", "")
ids_list = ids_list.replace("]", "")
ids_list = ids_list.replace("'", "")
ids_list = ids_list.split(", ")

# Pedir al usuario el nombre del archivo en el que se van a guardar los abstracts
name_abs = input("Introduce el nombre del archivo en el que se van a guardar los abstracts")

# Llamar a la función abstracts
abstracts(name_abs, ids_list)