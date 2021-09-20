'''
NAME
       ResumenGenBank.py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Este programa lee un archivo genbank y  a partir de este y de una lista de genes regresa información contenida
        en el archivo.

CATEGORY
       Secuencias/Formatos.

EXAMPLE:

        Input:
            path = "files/virus.gb"
            genes = ["N"]
        Output:
            Organismo: Isfahan virus
            Versión: 1
            Aislado de: ['Phlebotomus papatasi']
            País: ['Iran:Isfahan province']
            Gen:  ['N']
            DNA:  ATGACTTCTGTAGTA
            RNA:  AUGACUUCUGUAGUA
            Proteína:  MTSVV


LIGA DE GITHUB: [https://github.com/MateoMayaM/biopython_class/blob/master/tareas/ResumenGenBank.py
'''

# Definicion de la funcion
def resumen(path, genes):
#Importacion de librerias
    from Bio import SeqIO

#Obtener la informacion de los metadatos contenida en annotations.
    for record in SeqIO.parse(path, "genbank"):
        print("Organismo:", record.annotations["organism"])
        print("Versión:", record.annotations["sequence_version"])
        print ("Aislado de:", record.features[0].qualifiers["isolation_source"])
        print ("País:", record.features[0].qualifiers["country"])
        print ("-----")

    #Para la lista de genes acceder a los features e imprimir los que se requieren.
    for j in range(0, len(genes)):
        for i in range (2,len (record.features), 2):
            if str(record.features[i].qualifiers["gene"]) == str("['" + genes[j] + "']"):
                print ("Gen: ", record.features[i].qualifiers["gene"])
                print("DNA: ", record.seq[record.features[i].location.nofuzzy_start:record.features[i].location.nofuzzy_start+15])
                print("RNA: ", (record.seq[record.features[i].location.nofuzzy_start:record.features[i].location.nofuzzy_start+15]).transcribe())
                print ("Proteína: ", (record.seq[record.features[i].location.nofuzzy_start:record.features[i].location.nofuzzy_start+15]).translate())
                print ("-----")


#Especificar el archivo con el que vamos a trabajar
path = "files/virus.gb"

#Especificar la lista de genes
genes = ["N", "P", "M", "G", "L"]

#Lloamar a la funcion
resumen(path, genes)



