'''
NAME
       PDB.py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        Este programa recibe la ruta de un archivo .pdb y busca en este archivo aminoacidos de un tipo en una cadena. Tanto
        la cadena como el aminoacido son especificados por el usuario.

CATEGORY
       Protein analysis/ Protein Data Bank.

EXAMPLE:

        Input:
            Introduce el nombre que quieres asignar: prot1
            Introduce la ruta en la que se encuentra tu archivo PDB: ../files/1kcw.pdb
            Introduce el nombre de la cadena en la que deseas buscar: a
            Introduce el triple letter code del aminoácido que quieres buscar: cys
        Output:
            [<Residue CYS het=  resseq=155 icode= >, <Residue CYS het=  resseq=181 icode= > ...]


LIGA DE GITHUB: [https://github.com/MateoMayaM/biopython_class/blob/master/tareas/PDB.py
'''

# Importacion de librerias.
from Bio import PDB


def get_residue(file_name, path, chain_name, residue):
    """
Esta funcion un nombre que dará el usuario, la ruta del archivo .pdb, el nombre de la cadena y del residuo y regresa
una lista con los residuos contenidos en la cadena especidicada.
    """

# Crear un objeto parser y obtener el objeto structure.
    parser = PDB.PDBParser(QUIET=True)
    struc = parser.get_structure(file_name, path)
# Crear una lista vacia para guardar los aminoacidos.
    residues= []

# Para cada modelo si la cadena y el aminoacido especificados, se guardan en una lista
    for modelo in struc:
        for chain in modelo:
            if chain.id == chain_name:
                for residuo in chain:
                    if residuo.get_resname() == residue:
                        residues.append(residuo)
# Regresar la lista con los aminoacidos.
    return (residues)

# Pedir al usuario el nombre que quieres asignar.
file_name = input("Introduce el nombre que quieres asignar: ")

# Pedir al usuario la ruta donde se encuentra el archivo .pdb
path = input("Introduce la ruta en la que se encuentra tu archivo PDB: ")

# Pedir el usuario la cadena en la que quiere buscar y convertir el string a mayúsculas.
chain_name = input("Introduce el nombre de la cadena en la que deseas buscar: ")
chain_name = chain_name.upper()

# Pedir el usuario el aminoácido que quiere buscar y convertir el string a mayúsculas.
residue = input("Introduce el triple letter code del aminoácido que quieres buscar: ")
residue = residue.upper()

# Llamar a la funcion.
print(get_residue(file_name, path, chain_name, residue))
