def simulate_daisy_chain(generations, initial_fuel=1.0):
    """Simulates a self-limiting Daisy-Chain Gene Drive."""
    fuel = initial_fuel
    print("\n🔋 DAISY-CHAIN FUEL TELEMETRY")
    print("-" * 45)
    print(f"{'GEN':<5} | {'FUEL LEVEL':<12} | {'DRIVE STATUS'}")
    
    for gen in range(generations + 1):
        status = "🟢 ACTIVE" if fuel > 0.1 else "🔴 EXHAUSTED (Safe)"
        print(f"{gen:<5} | {fuel:.4f}     | {status}")
        
        # Fuel is consumed/diluted by 50% each generation
        fuel *= 0.5
        
        if status == "🔴 EXHAUSTED (Safe)":
            print(f"\n🛑 Drive automatically halted at Generation {gen}.")
            break

if __name__ == "__main__":
    simulate_daisy_chain(10)
