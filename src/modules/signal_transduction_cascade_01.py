class SignalCascade:
    def __init__(self, amplification_factor):
        self.factor = amplification_factor

    def propagate_signal(self, input_moles):
        output = input_moles * self.factor
        print(f"📡 SIGNAL AMPLIFIED: {input_moles} -> {output} units")
        return output

if __name__ == "__main__":
    cascade = SignalCascade(10**3)
    cascade.propagate_signal(0.005)
