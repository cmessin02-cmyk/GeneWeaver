import random

def generate_mini_genome(length=1000000, filename="mini_genome.fasta"):
    bases = ['A', 'C', 'G', 'T']
    # Generate random DNA sequence
    sequence = ''.join(random.choices(bases, k=length))
    
    # Save in FASTA format (Standard bioinformatics format)
    with open(f"data/genomes/{filename}", "w") as f:
        f.write(">Synthetic_Mini_Genome_v1\n")
        # Write 80 characters per line for readability
        for i in range(0, length, 80):
            f.write(sequence[i:i+80] + "\n")
            
    print(f"✅ Created genome: {filename} ({length} base pairs)")

if __name__ == "__main__":
    generate_mini_genome()
