import random

def generate_bio_key():
    """Generates a secret mapping for DNA encoding."""
    bases = ['A', 'C', 'G', 'T']
    pairs = ['00', '01', '10', '11']
    random.shuffle(bases)
    return dict(zip(pairs, bases))

def encrypt_data(binary, key):
    """Encodes binary to DNA using the secret key."""
    return "".join(key[binary[i:i+2]] for i in range(0, len(binary), 2))

if __name__ == "__main__":
    key = generate_bio_key()
    print(f"Secret Bio-Key: {key}")
