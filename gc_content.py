def Analyse_DNA(DNA_String):
    Total_lenght = len(DNA_String)
    g = DNA_String.count("G")
    c = DNA_String.count("C")
    gc_percent = (g + c)/Total_lenght*100
    return gc_percent
    
Sample1 = "ATTAAAGGTTTATACCCG"
Result = Analyse_DNA(Sample1)print(f"The GC percent is {Result}%")
