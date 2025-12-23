import random

def get_fitness(guide, target):
    # Calculates how many bases match (The higher, the better)
    score = sum(1 for a, b in zip(guide, target) if a == b)
    return score / len(target)

def mutate(sequence):
    # 5% chance to mutate a base
    seq_list = list(sequence)
    for i in range(len(seq_list)):
        if random.random() < 0.05:
            seq_list[i] = random.choice('ATCG')
    return "".join(seq_list)

def evolve():
    target_virus = "AGAGGTTTGATAACCCTGTC" # The original viral target
    population = ["".join(random.choice('ATCG') for _ in range(20)) for _ in range(100)]
    
    print("🧬 INITIALIZING DARWIN-X EVOLUTION ENGINE")
    print(f"TARGET VIRAL SIGNATURE: {target_virus}\n")

    for generation in range(1, 51):
        # Sort population by fitness
        population.sort(key=lambda x: get_fitness(x, target_virus), reverse=True)
        best_guide = population[0]
        best_fitness = get_fitness(best_guide, target_virus)

        if generation % 10 == 0 or generation == 1:
            print(f"GEN {generation:02}: Best Fitness: {best_fitness:.2%} | Sequence: {best_guide}")

        # Selection: Keep top 20, mutate them to fill the next 100
        new_population = population[:20]
        while len(new_population) < 100:
            parent = random.choice(population[:20])
            new_population.append(mutate(parent))
        population = new_population
        
        # Viral Escape: The virus mutates every 15 generations!
        if generation % 15 == 0:
            target_virus = mutate(target_virus)
            print(f"\n🌪️ VIRUS MUTATED! New Target: {target_virus}\n")

    print("\n🏆 EVOLUTION COMPLETE.")
    print(f"Final Apex Guide: {population[0]}")

if __name__ == "__main__":
    evolve()
