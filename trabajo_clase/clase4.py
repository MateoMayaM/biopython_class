# Notas PDB. Clase 4.
'''
from Bio import PDB

parser = PDB.PDBParser(QUIET=True)

struc = parser.get_structure('prot_1fat', "files/1fat.pdb")

print(struc.child_dict)
print(struc.child_list)

print (struc.header.keys())
print(struc.header['structure_method'])
print (struc.header['resolution'])
'''
#Ejercicio 1

from Bio import PDB
parser = PDB.PDBParser(QUIET=True)
struc = parser.get_structure('prot_1kcw', "files/1kcw.pdb")

print("keys y values")
for key, value in struc.header.items():
    print("key:", key, "value:", value)
    print ("------")

struct_method = struc.header['structure_method']

struc_resolution = struc.header['resolution']

print(struct_method, struc_resolution)


#Notas modelos y cadenas.
'''
for model in struc:
    print(model)

print(model.child_dict)
print(model.child_list)

for chain in model:
    print (chain)

chain = model ['A']
print (chain)

print(chain.child_dict)
print(chain.child_list)

for residue in chain:
    print(residue)

residuo = chain[1]
print(residuo)

print(residuo.get_id()[1])
print(residuo.get_resname())

for residuo in chain:
    if residuo.get_resname()== 'SER':
        residuos_int.append(residuo)

'''

#Ejercicio 2.

cisteinas = []

for modelo in struc:
    for chain in modelo:
        if chain.id == "A":
            for residuo in chain:
                if residuo.get_resname() == "CYS":
                    cisteinas.append(residuo)


print (cisteinas)