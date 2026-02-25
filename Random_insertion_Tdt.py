import random

def chyron_recorder(tape, cycles):
    bases = ['A', 'T', 'C', 'G']
    
    print(f"Starting Tape: {tape}")
    
    for i in range(cycles):
        num_to_add = random.randint(1, 3) 
        insertion = "".join(random.choices(bases, k=num_to_add))
        
        tape = tape + insertion
        print(f"Cycle {i+1} (+{insertion}): {tape}")
        
    return tape
final_record = chyron_recorder("TARGET_SITE_", 15)