def calculate_melting_temp(dna):
    """Basic Wallace Rule for Tm."""
    g = dna.count('G')
    c = dna.count('C')
    a = dna.count('A')
    t = dna.count('T')
    tm = 2 * (a + t) + 4 * (g + c)
    return tm

def apply_gc_clamp(dna):
    """Strategically adds GC pairs to the ends to prevent 'fraying'."""
    clamped_dna = f"GCGC{dna}GCGC"
    return clamped_dna, calculate_melting_temp(clamped_dna)

if __name__ == "__main__":
    print(apply_gc_clamp("ATATATAT"))
