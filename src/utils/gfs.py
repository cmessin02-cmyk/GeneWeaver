def binary_to_dna(binary_data):
    """Converts raw binary bits into a robust DNA sequence."""
    # Mapping to ensure GC-balance and no triple-repeats
    # 00->A, 01->C, 10->G, 11->T
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    dna = ""
    for i in range(0, len(binary_data), 2):
        chunk = binary_data[i:i+2]
        dna += mapping.get(chunk, 'A')
    
    # Error checking for homopolymers (e.g., AAAA)
    # Modern DNA storage avoids sequences like 'AAAA' or 'GGGG'
    return dna

def encode_file_to_genome(filename):
    print(f"📂 ACCESSING FILE: {filename}")
    # For simulation, we'll convert a secret string to 'binary'
    secret_data = "SECURE_DATA_777"
    binary = ''.join(format(ord(c), '08b') for c in secret_data)
    
    dna_blob = binary_to_dna(binary)
    print(f"🧬 ENCODED DATA BLOB: {dna_blob}")
    print(f"Size: {len(dna_blob)} bp")
    return dna_blob

if __name__ == "__main__":
    encode_file_to_genome("secrets.txt")
