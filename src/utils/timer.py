import math

def calculate_data_expiry(temp_celsius, base_stability=100):
    """Calculates how long DNA data lasts before it 'melts' or degrades."""
    # Arrhenius equation-style decay: higher temp = faster decay
    decay_rate = math.exp(temp_celsius / 10) 
    hours_remaining = base_stability / decay_rate
    
    print(f"\n🌡️ THERMAL TELEMETRY: {temp_celsius}°C")
    print(f"Estimated Data Life: {hours_remaining:.2f} hours")
    
    if hours_remaining < 1:
        print("⚠️ ALERT: DATA VOLATILITY CRITICAL. Self-destructing...")
    return hours_remaining

if __name__ == "__main__":
    calculate_data_expiry(37) # Body temp
