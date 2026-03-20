import random
import math
import matplotlib.pyplot as plt
import numpy as np
def simulate_barcode(max_insertion=20):
    #TdT randomly inserts 0 to max_insertion bases at a cut site.
    bases = ['A', 'T', 'G', 'C']
    n_insertions = random.randint(0, max_insertion)
    for i in range(n_insertions):
        a = ''.join(random.choice(bases))
    return a
    
def collision_rate(n_cells, n_simulations=500):
    
    #Simulate n_cells barcodes and check if any two match.
    #Repeat n_simulations times to get average collision probability.
    collisions = 0
    for i in range(n_simulations):
        barcodes = []
        for j in range(n_cells):
            barcodes.append(simulate_barcode())
        unique = len(set(barcodes))  # set() removes duplicates
        if unique < n_cells:        # fewer unique = collision happened
            collisions += 1
    return collisions / n_simulations
def birthday_collision_probability(n_cells, max_insertion=20):
    #Analytical estimate using Birthday Problem approximation.
    #N = total possible unique barcodes for a single TdT site.
    N = sum(4**i for i in range(max_insertion + 1))  # ~1.47 trillion
    return 1 - math.exp(-(n_cells**2) / (2 * N))

cell_counts = [100, 500, 1000, 5000, 10000, 50000,
               100000, 500000, 1000000, 5000000, 10000000]

# Calculate analytical collision probability for each count
analytical_probs = []
for k in cell_counts:
    analytical_probs.append(birthday_collision_probability(k)*100)


# Find the thresholds (1%, 5%, 10% collision)
thresholds = {'1%': None, '5%': None, '10%': None}
for k, p in zip(cell_counts, analytical_probs):
    if thresholds['1%'] is None and p >= 1:
        thresholds['1%'] = k
    if thresholds['5%'] is None and p >= 5:
        thresholds['5%'] = k
    if thresholds['10%'] is None and p >= 10:
        thresholds['10%'] = k
print("=== TdT Barcode Collision Analysis ===")
print(f"Total unique barcodes (1 site): {sum(4**i for i in range(21)):,}")
for t, k in thresholds.items():
    print(f"  {t} collision probability exceeded at: {k:,} cells")

# Plot
plt.figure(figsize=(10, 6))
plt.semilogx(cell_counts, analytical_probs, 'b-o', linewidth=2)
plt.axhline(y=1,  color='orange', linestyle='--', label='1% threshold')
plt.axhline(y=5,  color='red',    linestyle='--', label='5% threshold')
plt.axhline(y=10, color='darkred',linestyle='--', label='10% threshold')
plt.xlabel('Number of cells')
plt.ylabel('Collision probability (%)')
plt.title('TdT barcode collision probability — single hgRNA site')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('barcode_collision.png', dpi=150)
plt.show()
print("Plot saved as barcode_collision.png")
