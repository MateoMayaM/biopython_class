# Ejercicio 3

from Bio.Seq import Seq
from Bio import SeqIO

path = "files/sample.fastq"
# lista para guardar ids de los record que no cumplen con el umbral.
mala_calidad = []
umbral = 40


for record in SeqIO.parse(path, "fastq"):
    promedio = sum(record.letter_annotations["phred_quality"])/len(record.letter_annotations["phred_quality"])
    if (promedio < umbral):
        mala_calidad.append(((promedio, record.id)))


# GenBank

from Bio import SeqIO

for i in SeqIO.parse("files/aichi.gb", "genbank"):
    print("ID", i.id)
    print ("Secuencia", str(i.seq)[0:30], "...")
    print ("Longitud", len(i))


for j, k in i.annotations.items():
    print(j, k)

#Ejercicio genbank.

from Bio import SeqIO

path = "files/virus.gb"

for record in SeqIO.parse(path, "genbank"):
    print("ID", record.id)

print(record.annotations)

'''
for key, value in record.annotations:
    print (key, value)
'''
version = record.annotations["sequence_version"]
organismo = record.annotations["organism"]


f_source = (record.features[0].qualifiers
f_cds = (record.features[1])

print (f_source.location)
