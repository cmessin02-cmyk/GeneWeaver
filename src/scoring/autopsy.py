def run_autopsy(guides, human_off_targets):
    """Detects if multiple guides hit the same region in human DNA."""
    print("\n🚨 BIO-SECURITY AUTOPSY: SCANNING FOR TRANSLOCATION RISK")
    print("-" * 60)
    
    # Check for clusters (hits within 10kb of each other)
    found_risk = False
    sorted_hits = sorted(human_off_targets, key=lambda x: x['pos'])
    
    for i in range(len(sorted_hits) - 1):
        dist = sorted_hits[i+1]['pos'] - sorted_hits[i]['pos']
        if dist < 10000:
            print(f"⚠️ HAZARD: Cluster detected at Human Site {sorted_hits[i]['pos']}")
            print(f"Distance: {dist}bp (High Risk of Chromosomal Swap)")
            found_risk = True
            
    if not found_risk:
        print("✅ CLEAN AUTOPSY: No dangerous clusters found in human decoy.")
    return found_risk

if __name__ == "__main__":
    # Mock data for testing
    mock_hits = [{'pos': 1000}, {'pos': 10500}, {'pos': 11000}]
    run_autopsy(["G1", "G2"], mock_hits)
