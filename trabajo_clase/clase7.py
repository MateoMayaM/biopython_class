from Bio import Entrez, SeqIO

Entrez.email = "matteo.mayam@outlook.com"

handle = Entrez.esearch( db="protein", term = "Aedes aegypti[Orgn] AND DEFA[Gene]")
record = Entrez.read(handle)

record["Count"]
print(record["IdList"])

handle = Entrez.efetch(db="protein", id=record["IdList"][0],
                       rettype="gb", retmode="text")

record = SeqIO.read(handle, "genbank")

print(record.annotations["db_source"])

DEFA_prot = record.annotations['accessions']

db_source = record.annotations["db_source"]

from Bio import ExPASy
from Bio import SwissProt

handle = ExPASy.get_sprot_raw('P91793')

record = SwissProt.read(handle)

# Fecha de creacion, actualización de la anotación, id de taxonomía

print(record.created)
print(record.annotation_update)
print(record.taxonomy_id)


#

import Bio.SeqRecord, Bio.Seq

objeto_SeqRecord = Bio.SeqRecord.SeqRecord(seq = Bio.Seq.Seq(record.sequence), id = record.entry_name, name= record.organism, description=record.description)
print (objeto_SeqRecord.format("fasta"))

### Se puede leer con SeqIO pero hay pérdida de información ya que creamos un objeto SeqRecord

handle = ExPASy.get_sprot_raw('P91793')

record = SeqIO.read(handle, 'swiss')


from Bio import ExPASy
from Bio.ExPASy import Prosite
handle = ExPASy.get_prosite_raw("PS00785")
record = Prosite.read(handle)
print (record.name)

print(record.__dict__.keys())

print(record.pdoc)
