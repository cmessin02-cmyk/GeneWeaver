def get_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in sequence)

def calculate_self_homology(sequence):
    """Checks if the guide sticks to itself (Secondary Structure Risk)."""
    rev_comp = get_complement(sequence)[::-1]
    max_bond = 0
    
    # We look for the longest continuous stretch where the guide matches its own reverse
    for shift in range(-len(sequence) + 1, len(sequence)):
        current_bonds = 0
        for i in range(len(sequence)):
            j = i + shift
            if 0 <= j < len(sequence):
                if sequence[i] == rev_comp[j]:
                    current_bonds += 1
                else:
                    max_bond = max(max_bond, current_bonds)
                    current_bonds = 0
        max_bond = max(max_bond, current_bonds)
    
    # Return percentage of sequence that could self-bind
    return round((max_bond / len(sequence)) * 100, 2)

if __name__ == "__main__":
    # Test a "Bad" guide that folds on itself (Palindromic)
    bad_guide = "GGGGCCCCAAAAGGGGCCCC"
    # Test a "Good" guide with low self-binding
    good_guide = "AGAGGTTTGATAACCCTGTC"
    
    print(f"Self-Binding (Bad): {calculate_self_homology(bad_guide)}%")
    print(f"Self-Binding (Good): {calculate_self_homology(good_guide)}%")
