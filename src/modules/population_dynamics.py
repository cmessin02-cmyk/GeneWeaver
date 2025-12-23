import random

class StochasticEvolutionEngine:
    def __init__(self, p_frequency, pop_size):
        self.p = p_frequency
        self.q = 1 - p_frequency
        self.pop_size = pop_size

    def run_simulation(self, generations):
        print(f"🧬 ARCHITECTURE: STOCHASTIC GENETIC DRIFT MODEL")
        print("-" * 50)
        
        for gen in range(1, generations + 1):
            # HW Equilibrium Logic
            p_squared = self.p**2
            two_pq = 2 * self.p * self.q
            q_squared = self.q**2
            
            print(f"GEN {gen:02} | Dominant: {p_squared:.3f} | Hetero: {two_pq:.3f} | Recessive: {q_squared:.3f}")
            
            # Simulate Environmental Pressure / Genetic Drift
            drift_coefficient = random.uniform(-0.03, 0.03)
            self.p = max(0, min(1, self.p + drift_coefficient))
            self.q = 1 - self.p

if __name__ == "__main__":
    engine = StochasticEvolutionEngine(p_frequency=0.6, pop_size=10000)
    engine.run_simulation(10)
