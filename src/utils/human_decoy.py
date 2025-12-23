import random

def generate_human_decoy():
    # Generate 5MB of random DNA to represent a "Human Chromosome Fragment"
    # We use a specific GC-content (41%) to mimic human DNA
    bases = ['A', 'C', 'G', 'T']
    weights = [0.295, 0.205, 0.205, 0.295]
    
    print("🧬 Synthesizing 5MB Human Decoy Genome...")
    chunk_size = 100000
    with open("data/genomes/human_decoy.fasta", "w") as f:
        f.write(">Human_Chromosome_Fragment_Decoy\n")
        for _ in range(50): # 50 * 100k = 5MB
            chunk = "".join(random.choices(bases, weights=weights, k=chunk_size))
            f.write(chunk + "\n")
    print("✅ Decoy Genome Ready.")

if __name__ == "__main__":
    generate_human_decoy()
