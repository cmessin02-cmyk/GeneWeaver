import random

def simulate_evolution(p, population_size, generations):
    print(f"🧬 NEET EVOLUTION SIMULATOR: Hardy-Weinberg")
    print("="*50)
    q = 1 - p
    print(f"Initial: p(Dominant)={p}, q(Recessive)={q}")
    
    for gen in range(1, generations + 1):
        # Calculate Genotype Frequencies
        homo_dom = p**2
        hetero = 2 * p * q
        homo_rec = q**2
        
        print(f"Gen {gen}: p^2={homo_dom:.2f}, 2pq={hetero:.2f}, q^2={homo_rec:.2f}")
        
        # Simulate 'Genetic Drift' (Small change for next gen)
        drift = random.uniform(-0.02, 0.02)
        p = max(0, min(1, p + drift))
        q = 1 - p

if __name__ == "__main__":
    # Example: If p = 0.6, calculate frequencies for 5 generations
    simulate_evolution(0.6, 1000, 5)
