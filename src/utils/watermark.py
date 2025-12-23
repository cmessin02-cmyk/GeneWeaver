def text_to_dna(text):
    """Encodes ASCII text into a DNA sequence."""
    binary = ''.join(format(ord(c), '08b') for c in text)
    # Map 00->A, 01->C, 10->G, 11->T
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    dna_signature = "".join(mapping[binary[i:i+2]] for i in range(0, len(binary), 2))
    return dna_signature

def embed_watermark(genome, message, position):
    """Injects a digital signature into a non-coding region."""
    signature = text_to_dna(message)
    print(f"🖋️ GENERATING BIO-SIGNATURE: {message}")
    print(f"DNA ENCODED: {signature}")
    
    new_genome = genome[:position] + f"<{signature}>" + genome[position:]
    return new_genome

if __name__ == "__main__":
    msg = "GOAT:MESSI"
    dna_msg = text_to_dna(msg)
    print(f"Message: {msg} | DNA: {dna_msg}")
