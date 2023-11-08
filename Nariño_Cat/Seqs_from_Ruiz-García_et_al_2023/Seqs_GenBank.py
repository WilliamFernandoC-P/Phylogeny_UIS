from Bio import Entrez
from Bio import SeqIO

# Set your email address (required for using NCBI Entrez)
Entrez.email = "williamfernandochaparro@gmail.com"

# Define the list of accession numbers
accession_numbers = ["MG230196.1", "MG230197.1", "MG230198.1", "MG230199.1", "MG230200.1", "MG230201.1", "MG230202.1", "MG230203.1", "MG230204.1", "MG230205.1", "MG230206.1", "MG230207.1", "MG230208.1", "MG230209.1", "MG230210.1", "MG230211.1", "MG230212.1", "MG230213.1", "MG230214.1", "MG230232.1"]
    
# Download and save the sequences in FASTA format
for accession in accession_numbers:
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    
    # Save the sequence in FASTA format
    output_file = f"{accession}.fasta"
    SeqIO.write(record, output_file, "fasta")
    print(f"The sequence {accession} has been downloaded and saved in '{output_file}' in FASTA format.")
