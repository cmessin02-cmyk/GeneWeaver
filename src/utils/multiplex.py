def generate_multiplex_construct(guide1, guide2):
    print("\n🔗 ASSEMBLING DUAL-GUIDE MULTIPLEX CONSTRUCT")
    print("-" * 50)
    
    # Standard U6 Promoter sequence for the second guide
    u6_promoter = "GAGGGCCTATTTCCCATGATTCCTTCATATTTGC" 
    linker = "GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGC"
    
    full_construct = f"{guide1}{linker}{u6_promoter}{guide2}"
    
    print(f"Construct Length: {len(full_construct)} bp")
    print(f"Structure: [Guide 1] -> [Scaffold] -> [U6 Promoter] -> [Guide 2]")
    
    with open("multiplex_construct.fasta", "w") as f:
        f.write(">GENE-WEAVER_DUAL_SENTRY_V2\n")
        f.write(full_construct + "\n")
        
    print("💾 EXPORTED: multiplex_construct.fasta")
    return full_construct

if __name__ == "__main__":
    # Using our original guide and a new 'Secondary' target we found earlier
    generate_multiplex_construct("AGAGGTTTGATAACCCTGTC", "GTTTTAGAGCTAGAAATAGC")
