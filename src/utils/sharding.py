def shard_data(dna_sequence, num_shards=3):
    """Splits DNA into indexed shards for decentralized storage."""
    shard_size = len(dna_sequence) // num_shards
    shards = []
    
    print(f"\n💎 SHARDING DATA INTO {num_shards} BIOLOGICAL NODES")
    print("-" * 45)
    
    for i in range(num_shards):
        start = i * shard_size
        end = (i + 1) * shard_size if i < num_shards - 1 else len(dna_sequence)
        
        # Add an index tag (e.g., S1, S2, S3) to the sequence
        tag = f"ID{i+1}" 
        shard_content = f"{tag}_{dna_sequence[start:end]}"
        shards.append(shard_content)
        print(f"Node {i+1}: {shard_content}")
        
    return shards

if __name__ == "__main__":
    shard_data("GCGCCCCCGCGC", 3)
