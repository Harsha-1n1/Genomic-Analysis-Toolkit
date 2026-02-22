def transcribe(dna):
    dna = dna.upper()
    rna = dna.replace("T", "U")
    return rna
    
Sample2="atgcgtacgt"
print(f"RNA sequence = {transcribe(Sample2)}")