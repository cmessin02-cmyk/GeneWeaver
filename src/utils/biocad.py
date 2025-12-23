def generate_plasmid_map(guide_seq):
    print("\n🌀 GENERATING 2D PLASMID MAP (GENE-WEAVER-V1)")
    print("-" * 50)
    
    # Visualizing the circular structure
    plasmid = [
        "      [Origin of Rep]      ",
        "    /                 \\    ",
        f" [Cas9]            [gRNA: {guide_seq[:5]}...]",
        "    \\                 /    ",
        "      [Antibiotic Res]     "
    ]
    
    for line in plasmid:
        print(line)
        
    print("\n✅ MAP GENERATED: Ready for synthesis.")

if __name__ == "__main__":
    generate_plasmid_map("AGAGGTTTGATAACCCTGTC")
