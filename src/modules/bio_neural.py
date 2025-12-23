import numpy as np

class BioNeuron:
    def __init__(self, weight_concentration):
        # In God Mode, weights are chemical concentrations (0.0 to 1.0)
        self.weights = np.array(weight_concentration)
        self.threshold_strand = 0.5 # The 'Inhibitor' concentration

    def activate(self, inputs):
        """Simulates DNA Strand Displacement sum and threshold logic."""
        # Weighted sum: Concentration of Input Strands x Binding Affinity (Weights)
        total_signal = np.dot(inputs, self.weights)
        
        print(f"🧬 SIGNAL ANALYSIS: {total_signal:.4f} vs Threshold {self.threshold_strand}")
        
        # Winner-Take-All / Heaviside Step Function
        if total_signal > self.threshold_strand:
            print("🚀 NEURON FIRE: Output strand released. ACCESS GRANTED.")
            return 1
        else:
            print("🛑 NEURON SILENT: Signal quenched by Threshold strands.")
            return 0

if __name__ == "__main__":
    # Define weights for 3 inputs: [Pathogen_Presence, Key_Alpha, Key_Beta]
    # Pathogen has a negative (inhibitory) effect on unlocking
    vault_brain = BioNeuron(weight_concentration=[-0.8, 0.6, 0.7])
    
    # Scenario: High Pathogen detected, but both keys are present
    test_inputs = np.array([1.0, 1.0, 1.0]) 
    
    print("🧠 INITIATING BIO-NEURAL DECISION...")
    vault_brain.activate(test_inputs)
