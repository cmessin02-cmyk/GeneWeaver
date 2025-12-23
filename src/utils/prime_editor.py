def design_pegrna(target_seq, desired_edit):
    """Designs a Prime Editing guide RNA (pegRNA) for high-precision rewriting."""
    # A pegRNA has: [Spacer] + [Scaffold] + [RT Template] + [PBS]
    spacer = target_seq[:20]
    scaffold = "GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCG"
    
    # The PBS needs to be about 13bp and the RT Template about 10-15bp
    pbs = target_seq[-13:]
    rt_template = desired_edit + target_seq[len(desired_edit):len(desired_edit)+10]
    
    pegrna = f"{spacer}[SC]{rt_template}{pbs}"
    
    print("\n✍️ PRIME EDITING pegRNA ASSEMBLED")
    print("-" * 45)
    print(f"Spacer:  {spacer}")
    print(f"Edit:    {desired_edit}")
    print(f"PBS:     {pbs}")
    print(f"Full pegRNA Construct Ready.")
    return pegrna

if __name__ == "__main__":
    design_pegrna("AGAGGTTTGATAACCCTGTC", "GCTC")
