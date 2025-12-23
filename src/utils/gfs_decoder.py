def dna_to_binary(dna_sequence):
    """Converts a DNA sequence back into digital binary bits."""
    # Mapping: A->00, C->01, G->10, T->11
    mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    binary = "".join(mapping.get(base, '00') for base in dna_sequence)
    return binary

def binary_to_text(binary):
    """Converts binary bits back into readable ASCII text."""
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            text += chr(int(byte, 2))
    return text

def decode_vault_construct(construct):
    """Extracts the data from between the TCG_START and TCG_END primers."""
    print(f"\n📥 DECODING BIO-VAULT CONSTRUCT...")
    
    # Strip the Primers
    try:
        data_part = construct.split("TCG_START_")[1].split("_TCG_END")[0]
        binary = dna_to_binary(data_part)
        text = binary_to_text(binary)
        
        print(f"Decoded Data: {text}")
        return text
    except IndexError:
        print("❌ ERROR: Primer signatures not found. Data corrupted.")
        return None

if __name__ == "__main__":
    test_construct = "TCG_START_CCATCACCCAATCCCCCCAGCACCCCTTCACACAACCCCACAACCCTTATCTATCTATCT_TCG_END"
    decode_vault_construct(test_construct)
