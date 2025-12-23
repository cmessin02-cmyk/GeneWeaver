import re

def scan_for_targets(genome_path, target_seq="GGTTCACTGACTGACTGACT"):
    with open(genome_path, 'r') as f:
        # Skip the header line and join the rest
        genome = "".join(line.strip() for line in f if not line.startswith(">"))
    
    # Regex to find any 20 bases followed by NGG
    # Format: (?=(.{20}.GG)) is a lookahead to handle overlapping sites
    pattern = re.compile(r'(?=([ACGT]{20}.GG))')
    
    matches = pattern.finditer(genome)
    results = []
    
    for match in matches:
        site = match.group(1)
        # We only care about the 20bp guide, not the PAM itself
        guide_area = site[:20] 
        results.append(guide_area)
        
    print(f"🔍 Found {len(results)} potential target sites in genome.")
    return results

if __name__ == "__main__":
    # Test run
    scan_for_targets("data/genomes/mini_genome.fasta")
