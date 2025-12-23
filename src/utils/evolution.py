import random

def mutate_sequence(sequence, mutation_rate=0.05):
    """Randomly mutates a DNA sequence based on a percentage rate."""
    bases = ['A', 'C', 'G', 'T']
    list_seq = list(sequence)
    mutations_count = 0
    
    for i in range(len(list_seq)):
        if random.random() < mutation_rate:
            original = list_seq[i]
            # Pick a new base that isn't the original
            new_base = random.choice([b for b in bases if b != original])
            list_seq[i] = new_base
            mutations_count += 1
            
    return "".join(list_seq), mutations_count

if __name__ == "__main__":
    test_dna = "ATGTTTGTTTTTCTTGTTTTATTGCCACTA"
    mutated, count = mutate_sequence(test_dna)
    print(f"Original: {test_dna}")
    print(f"Mutated:  {mutated} ({count} mutations)")
