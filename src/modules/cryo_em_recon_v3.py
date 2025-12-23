import numpy as np

class StructuralReconstructor:
    def __init__(self, resolution_angstrom):
        self.res = resolution_angstrom
        print(f"🔬 RECONSTRUCTOR INITIALIZED: {self.res}Å Resolution")

    def simulate_projection(self, structure_data):
        # Adds Gaussian noise to simulate real-world imaging
        noise = np.random.normal(0, 0.1, len(structure_data))
        return structure_data + noise

if __name__ == "__main__":
    recon = StructuralReconstructor(2.5)
    data = np.array([1, 0, 1, 1, 0])
    print(f"Reconstructed Map: {recon.simulate_projection(data)}")
