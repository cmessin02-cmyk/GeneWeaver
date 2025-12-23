def calculate_delivery_viability(sequence, modified=True):
    """Calculates viability with Chemical Modification support."""
    length = len(sequence)
    # Modified RNA (Pseudouridine) increases stability by 3x
    half_life = 6 if modified else 2 
    
    return {
        "stability": "💎 REINFORCED" if modified else "🟢 OPTIMAL",
        "half_life": f"{half_life} hours",
        "potency_boost": 2.5 if modified else 1.0
    }
