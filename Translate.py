def translate(codon):
    Genetic_code = {
        "ATG": "Methionine (START)",
        "TGG": "Tryptophan",
        "GGC": "Glycine",
        "TAA": "STOP"
    }
    return Genetic_code.get(codon.upper(), "Unknown Amino Acid")
    
Sample5 = "ATG"
Sample6 = "GGG"
print(f"The amino acid for the codon {Sample5} is {translate(Sample5)}")
print(f"The amino acid for the codon {Sample6} is {translate(Sample6)}")