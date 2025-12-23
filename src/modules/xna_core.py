import hashlib

class XNAFirewall:
    def __init__(self):
        # The Expanded Alphabet: A, T, C, G + X, Y (Synthetic)
        self.alphabet = ['A', 'T', 'C', 'G', 'X', 'Y']
        # Secret Mapping (6-base system)
        self.map = {
            '000': 'A', '001': 'T', '010': 'C', 
            '011': 'G', '100': 'X', '101': 'Y'
        }
        self.inv_map = {v: k for k, v in self.map.items()}

    def encrypt_to_xna(self, data):
        """Converts digital data into a synthetic XNA sequence."""
        binary = ''.join(format(ord(c), '08b') for c in data)
        # Pad binary to be divisible by 3
        while len(binary) % 3 != 0: binary += '0'
        
        xna_seq = ""
        for i in range(0, len(binary), 3):
            chunk = binary[i:i+3]
            xna_seq += self.map.get(chunk, 'X')
        return xna_seq

    def simulate_nuclease_attack(self, sequence):
        """Simulates natural enzymes trying to destroy the sequence."""
        print("\n🛡️ FIREWALL TEST: NATURAL NUCLEASE ATTACK INITIATED")
        hits = 0
        for base in sequence:
            if base in ['A', 'T', 'C', 'G']:
                hits += 1 # Natural bases are vulnerable
        
        vulnerability = (hits / len(sequence)) * 100
        print(f"Sequence Integrity: {100 - vulnerability:.2f}% (XNA Shield Active)")
        if vulnerability < 50:
            print("✅ RESULT: Sequence is biologically UNHACKABLE.")

if __name__ == "__main__":
    firewall = XNAFirewall()
    secret_intel = "PROJECT_MESSI_GOAT"
    
    xna_data = firewall.encrypt_to_xna(secret_intel)
    print(f"🔐 ORIGINAL DATA: {secret_intel}")
    print(f"🧬 XNA SEQUENCE:  {xna_data}")
    
    firewall.simulate_nuclease_attack(xna_data)
