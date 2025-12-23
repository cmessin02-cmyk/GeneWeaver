import math

# Nearest-Neighbor Parameters (Enthalpy H in kcal/mol, Entropy S in cal/mol*K)
NN_DATA = {
    'AA': (-7.9, -22.2), 'TT': (-7.9, -22.2), 'AT': (-7.2, -20.4), 'TA': (-7.2, -21.3),
    'CA': (-8.5, -22.7), 'TG': (-8.5, -22.7), 'GT': (-8.4, -22.4), 'AC': (-8.4, -22.4),
    'CT': (-7.8, -21.0), 'AG': (-7.8, -21.0), 'GA': (-8.2, -22.2), 'TC': (-8.2, -22.2),
    'CG': (-10.6, -27.2), 'GC': (-9.8, -24.4), 'GG': (-8.0, -19.9), 'CC': (-8.0, -19.9)
}

def calculate_tm(sequence, salt_conc=0.05, dna_conc=0.0000005):
    """Calculates the Melting Temperature (Tm) of the DNA/RNA duplex."""
    h = 0  # Enthalpy
    s = 0  # Entropy
    r = 1.987 # Gas Constant
    
    # Initiation constants
    h += 0.2
    s += -5.7
    
    # Symmetry correction (if palindromic)
    if sequence == sequence[::-1]:
        s -= 1.4

    # Calculate H and S for each neighbor pair
    for i in range(len(sequence) - 1):
        pair = sequence[i:i+2]
        if pair in NN_DATA:
            h += NN_DATA[pair][0]
            s += NN_DATA[pair][1]

    # Salt correction for Entropy
    s += 0.368 * (len(sequence) - 1) * math.log(salt_conc)
    
    # Tm Calculation (Kelvin to Celsius)
    tm = (1000 * h) / (s + r * math.log(dna_conc/4)) - 273.15
    return round(tm, 2)

if __name__ == "__main__":
    test_seq = "TTCACACGTGGTGTTTATTA"
    print(f"Sequence: {test_seq}")
    print(f"Melting Temperature (Tm): {calculate_tm(test_seq)}°C")
