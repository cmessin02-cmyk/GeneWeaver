from src.aligner.scanner import scan_for_targets
from src.scoring.hsu_zhang import calculate_score

def find_best_guide(genome_path, iterations=10):
    candidates = scan_for_targets(genome_path)
    print(f"\n🔬 Analyzing {iterations} candidates for 'Perfect Match' status...")
    
    scored_guides = []
    # Test the first few candidates to find the safest one
    for i in range(min(iterations, len(candidates))):
        target = candidates[i]
        total_risk = 0
        
        for other in candidates:
            if target == other: continue
            score = calculate_score(target, other)
            total_risk += score
            
        scored_guides.append((target, total_risk))
    
    scored_guides.sort(key=lambda x: x[1])
    best = scored_guides[0]
    print(f"\n✅ Safest Guide Found: {best[0]}")
    print(f"Total Cumulative Off-Target Risk: {best[1]}%")

if __name__ == "__main__":
    find_best_guide("data/genomes/mini_genome.fasta")
