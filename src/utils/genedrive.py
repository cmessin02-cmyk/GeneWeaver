def simulate_gene_drive(initial_population, release_count, generations):
    """Simulates the spread of a Gene Drive through a population."""
    pop = initial_population
    drive_carriers = release_count
    
    print(f"\n🌍 GENE DRIVE PROPAGATION: {generations} GENERATIONS")
    print("-" * 50)
    print(f"{'GEN':<5} | {'CARRIERS':<12} | {'WILD-TYPE':<12} | {'DRIVE %'}")
    
    for gen in range(generations + 1):
        total = pop + drive_carriers
        percentage = (drive_carriers / total) * 100
        print(f"{gen:<5} | {int(drive_carriers):<12} | {int(pop):<12} | {percentage:.2f}%")
        
        # Gene Drive Logic: Carriers mate with Wild-Type and convert offspring
        # In a Gene Drive, offspring of (Carrier x Wild) are 100% Carriers
        new_carriers = drive_carriers + (pop * (drive_carriers / total))
        pop = pop - (pop * (drive_carriers / total))
        
        # Natural population growth
        drive_carriers = new_carriers * 1.05 
        pop = pop * 1.05
        
        if percentage > 99.9:
            print(f"\n✅ FIXATION ACHIEVED at Generation {gen}")
            break

if __name__ == "__main__":
    simulate_gene_drive(10000, 100, 20)
