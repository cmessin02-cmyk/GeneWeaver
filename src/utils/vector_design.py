def design_expression_cassette(guide_seq, cell_type="human"):
    """Assembles the DNA components for the CRISPR delivery vehicle."""
    # Promoters are the 'On Switches'
    promoters = {
        "human": "GAGGGCCTATTTCCCATGATTCCTTCATATTTGC", # U6 Promoter
        "bacterial": "TTGACAATTAATCATCCGGCTCGTATAATGTGT", # Tac Promoter
        "plant": "AAAGGCCACCGTGTGAATCTA" # CaMV35S
    }
    
    promoter = promoters.get(cell_type, promoters["human"])
    cas9_gene = "ATGGACAAGAAGTACTCCATTGGGCTCGATATCGGCACAAACAGCGTCGGC..." # Truncated Cas9
    
    # Assembly: [Promoter] + [Guide] + [Scaffold DNA]
    scaffold = "GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTT"
    
    full_vector = f"{promoter}{guide_seq}{scaffold}"
    
    print(f"🛠️ VECTOR DESIGNED FOR: {cell_type.upper()}")
    print(f"Total Sequence Length: {len(full_vector)} bp")
    print(f"Sequence Preview: {full_vector[:50]}...")
    return full_vector

if __name__ == "__main__":
    design_expression_cassette("AGAGGTTTGATAACCCTGTC")
