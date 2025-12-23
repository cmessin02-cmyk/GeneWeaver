def save_as_fasta(header, sequence, filename="target_dna.fasta"):
    """Exports the DNA to a standard FASTA file format."""
    with open(filename, "w") as f:
        f.write(f">{header}\n")
        # Standard FASTA formatting: 60 characters per line
        for i in range(0, len(sequence), 60):
            f.write(sequence[i:i+60] + "\n")
    print(f"💾 SUCCESS: Sequence saved to {filename}")

if __name__ == "__main__":
    # Your Armored Bio-Vault sequence from the last run
    final_dna = "GCGCCCCCGCGC" 
    save_as_fasta("GENE-WEAVER_ARMORED_VAULT_V1", final_dna)
