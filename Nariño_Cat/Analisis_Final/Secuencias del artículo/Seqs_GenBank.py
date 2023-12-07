from Bio import Entrez
from Bio import SeqIO

# Set your email address (required for using NCBI Entrez)
Entrez.email = "williamfernandochaparro@gmail.com"

# Define the list of accession numbers
accession_numbers = ["MG230196.1", "MG230197.1", "MG230198.1", "MG230199.1", "MG230200.1", "MG230201.1", "MG230202.1", "MG230203.1", "MG230204.1", "MG230205.1", "MG230206.1", "MG230207.1", "MG230208.1", "MG230209.1", "MG230210.1", "MG230211.1", "MG230212.1", "MG230213.1", "MG230214.1", "MG230215.1", "MG230216.1", "MG230217.1", "MG230218.1", "MG230219.1", "MG230220.1", "MG230221.1", "MG230222.1", "MG230223.1", "MG230224.1", "MG230225.1", "MG230226.1", "MG230227.1", "MG230228.1", "MG230229.1", "MG230230.1", "MG230231.1", "MG230232.1", "MG230233.1", "MG230234.1", "MG230235.1", "MG230236.1", "MG230237.1", "MG230238.1", "MG230239.1", "MG230240.1", "MG230241.1", "MG230242.1", "MG230243.1", "MG230244.1", "MG230245.1", "MG230246.1", "MG230247.1", "MG230248.1", "MG230249.1", "MG230250.1", "MG230251.1"
]
    
# Download and save the sequences in FASTA format
for accession in accession_numbers:
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "genbank")
    handle.close()
    
    # Save the sequence in FASTA format
    output_file = f"{accession}.fasta"
    SeqIO.write(record, output_file, "fasta")
    print(f"The sequence {accession} has been downloaded and saved in '{output_file}' in FASTA format.")
