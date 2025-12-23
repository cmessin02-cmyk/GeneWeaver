import math

# Hsu-Zhang Weight Matrix (Penalty for each of the 20 positions)
# Positions near PAM (19, 20) have higher weights (more impact)
WEIGHTS = [
    0.0, 0.0, 0.014, 0.0, 0.0, 0.059, 0.0, 0.058, 
    0.105, 0.155, 0.159, 0.21, 0.225, 0.225, 0.787, 
    0.366, 0.199, 0.524, 0.475, 0.982
]

def calculate_score(target, candidate):
    if len(target) != len(candidate):
        return 0
    
    mismatches = []
    for i in range(len(target)):
        if target[i] != candidate[i]:
            mismatches.append(i)
    
    n = len(mismatches)
    if n == 0:
        return 100.0  # Perfect match
    
    # 1. Position-based weight product
    product = 1.0
    for m in mismatches:
        product *= (1.0 - WEIGHTS[m])
        
    # 2. Distance factor
    if n > 1:
        avg_dist = (mismatches[-1] - mismatches[0]) / (n - 1)
        dist_factor = 1.0 / (((19 - avg_dist) / 19) * 4 + 1)
    else:
        dist_factor = 1.0
        
    # 3. Mismatch count factor
    count_factor = 1.0 / (n**2)
    
    final_score = product * dist_factor * count_factor * 100
    return round(final_score, 4)

if __name__ == "__main__":
    # Test: Comparison between a perfect match and a 1-bp mismatch
    test_target = "GGTTCACTGACTGACTGACT"
    test_near   = "GGTTCACTGACTGACTGACT" # Perfect
    test_far    = "AGTTCACTGACTGACTGACT" # Mismatch at pos 0 (Far from PAM)
    test_seed   = "GGTTCACTGACTGACTGACA" # Mismatch at pos 19 (Near PAM)
    
    print(f"Score (Perfect): {calculate_score(test_target, test_near)}")
    print(f"Score (Far Mismatch): {calculate_score(test_target, test_far)}")
    print(f"Score (Seed Mismatch): {calculate_score(test_target, test_seed)}")
