def show_mutation_map(original, mutated, start_idx, length=20):
    """Shows exactly where mutations happened in a specific window."""
    orig_segment = original[start_idx:start_idx+length]
    mut_segment = mutated[start_idx:start_idx+length]
    
    diff_line = ""
    change_count = 0
    for o, m in zip(orig_segment, mut_segment):
        if o == m:
            diff_line += " "
        else:
            diff_line += "^" # Mark the mutation
            change_count += 1
            
    print(f"\n📍 Mutation Map (Site {start_idx}):")
    print(f"Original: {orig_segment}")
    print(f"Mutated:  {mut_segment}")
    print(f"Changes:  {diff_line} ({change_count} mutations)")

if __name__ == "__main__":
    show_mutation_map("ACTG" * 5, "ACTG" * 4 + "ATTG", 0)
