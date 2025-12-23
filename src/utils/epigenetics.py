import random

def get_accessibility_map(genome_length):
    """Simulates regions of open and closed chromatin."""
    # We create 'islands' of accessibility (100-300bp wide)
    accessible_map = [0] * genome_length
    curr = 0
    while curr < genome_length:
        size = random.randint(100, 500)
        state = random.choice([0, 0, 1]) # 1 in 3 chance of being 'Open'
        for i in range(curr, min(curr + size, genome_length)):
            accessible_map[i] = state
        curr += size
    return accessible_map

def calculate_reachability(start_pos, access_map, length=20):
    """Checks what percentage of the target site is in 'Open' DNA."""
    segment = access_map[start_pos : start_pos + length]
    if not segment: return 0.0
    return sum(segment) / len(segment)

if __name__ == "__main__":
    m = get_accessibility_map(1000)
    print(f"Sample Accessibility (First 50bp): {m[:50]}")
