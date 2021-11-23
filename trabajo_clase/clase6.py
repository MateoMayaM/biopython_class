from Bio import Entrez

# Primera parte: esearch para buscar primer organismo en taxonomy
Entrez.email = "matteo.mayam@outlook.com"

handle = Entrez.esearch(db="Taxonomy", term="Notoryctes typhlops")
record = Entrez.read(handle)
id_taxo = record["IdList"][0]


handle = Entrez.esearch(db="Taxonomy", term = "Notoryctes typhlops")
record = Entrez.read(handle)
print(record["IdList"])
id_taxo = record["IdList"][0]

# Segunda parte

handle = Entrez.efetch(db="Taxonomy", id=id_taxo, retmode="xml")
Chryso=Entrez.read(handle)
print(Chryso[0]["Lineage"])
