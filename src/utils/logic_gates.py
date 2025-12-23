def simulate_genetic_and_gate(sensor_a, sensor_b):
    """A biological AND gate using promoter logic."""
    print(f"\n🧬 ANALYZING BIOMARKERS...")
    print(f"Sensor A (Viral RNA): {'DETECTED' if sensor_a else 'ABSENT'}")
    print(f"Sensor B (Infection Protein): {'DETECTED' if sensor_b else 'ABSENT'}")
    
    # Logic: Promoter A + Promoter B must both be active to express Cas9
    if sensor_a and sensor_b:
        print("✅ LOGIC SATISFIED: Releasing CRISPR Shredder.")
        return True
    else:
        print("❌ LOGIC FAILED: System in Standby Mode.")
        return False

if __name__ == "__main__":
    simulate_genetic_and_gate(True, True)
