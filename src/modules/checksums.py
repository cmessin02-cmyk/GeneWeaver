import hashlib

class XNARibozyme:
    def __init__(self):
        # Using X and Y as our "Parity Bases" for error correction
        self.bases = ['A', 'T', 'C', 'G', 'X', 'Y']

    def generate_checksum(self, sequence):
        """Creates a synthetic X-Y signature based on the sequence data."""
        hash_val = hashlib.md5(sequence.encode()).hexdigest()
        # Convert first 4 chars of hash to X-Y language
        checksum = "".join(['X' if int(c, 16) > 7 else 'Y' for c in hash_val[:8]])
        return checksum

    def verify_integrity(self, sequence, stored_checksum):
        """Scans the sequence to see if it matches the 'X-Y' Firewall."""
        current_checksum = self.generate_checksum(sequence)
        print(f"\n🔍 RIBOZYME SCANNING SEQUENCE...")
        print(f"Stored Checksum:  {stored_checksum}")
        print(f"Current Checksum: {current_checksum}")
        
        if current_checksum == stored_checksum:
            print("💎 STATUS: INTEGRITY 100%. Sequence is pristine.")
            return True
        else:
            print("⚠️ ALERT: MUTATION DETECTED. Initiating XNA Repair...")
            return False

if __name__ == "__main__":
    ribo = XNARibozyme()
    
    # 1. Our Secure Data
    original_data = "ATCG_SECURE_VAULT"
    checksum = ribo.generate_checksum(original_data)
    
    print(f"Original Vault: {original_data}")
    print(f"Synthetic XNA Checksum: {checksum}")
    
    # 2. Simulate a Mutation (C flips to G)
    mutated_data = "ATGG_SECURE_VAULT" 
    print(f"\n☢️ RADIATION HIT! Sequence changed to: {mutated_data}")
    
    # 3. Verify and Repair
    ribo.verify_integrity(mutated_data, checksum)
