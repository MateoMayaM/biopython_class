# Bases de datos.

#Ejercicio 1
from Bio import Entrez
from pprint import pprint # para visualizar más bomnito los diccionarios.

# Correo
Entrez.email = "matteo.mayam@outlook.com"

handle = Entrez.einfo(db = "genome")
record = Entrez.read(handle)

i = -1
for field in record["DbInfo"]["FieldList"]:
    i += 1
    if field["Name"] == "ORGN":
        print(field["Name"], field["Description"])

print(record["DbInfo"]["FieldList"][9]["Description"])


## Esearch

handle = Entrez.esearch(db="pubmed", term="biopython")
record = Entrez.read(handle)
print (record["Count"])
print(handle.url)
handle.close()

## Ejemplo buscando autor

handle = Entrez.esearch(db = "pubmed", term = "Valeria Mateo-Estrada[AUTH]")
record = Entrez.read(handle)
handle.close()


