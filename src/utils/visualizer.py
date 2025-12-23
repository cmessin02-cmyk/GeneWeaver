def draw_alignment(target, candidate, score):
    """Creates a visual DNA ladder showing mismatches."""
    match_line = ""
    for t, c in zip(target, candidate):
        if t == c:
            match_line += "|"
        else:
            match_line += "."
    
    color = "\033[92m" # Green (Safe)
    if score > 5.0: color = "\033[93m" # Yellow (Warning)
    if score > 20.0: color = "\033[91m" # Red (Danger)
    reset = "\033[0m"

    print(f"\n{color}Risk Score: {score}%{reset}")
    print(f"Target:    {target}")
    print(f"           {match_line}")
    print(f"Off-Target: {candidate}")

def generate_report(results, target_rna):
    print("\n" + "="*40)
    print("🧬 GENE-WEAVER: BIO-SAFETY REPORT")
    print("="*40)
    print(f"GUIDE RNA: {target_rna}")
    
    if not results:
        print("✅ No significant off-target risks detected.")
        return

    # Only show the top 5 most dangerous
    for seq, score in results[:5]:
        draw_alignment(target_rna, seq, score)
