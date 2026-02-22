def get_reverse_complement(dna):
    dna = dna.upper()
    DNA_rule = str.maketrans("ATCG","TAGC")
    complement = dna.translate(DNA_rule)
    reverse_complement = complement[::-1]
    return reverse_complement

Sample3= "atgccgcgcgct"
print(f"DNA sequence is {Sample3.upper()}")
print(f"reverse complement is {get_reverse_complement(Sample3)}")
