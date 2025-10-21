def divide_string(s, k, fill_char=None):
    groups = [s[i:i+k] for i in range(0, len(s), k)]

    # Pad the last group if needed
    if fill_char and len(groups[-1]) < k:
        groups[-1] += fill_char * (k - len(groups[-1]))

    return groups


# --- Example Usage ---
if __name__ == "__main__":
    s = input("Enter a string: ")
    k = int(input("Enter group size (k): "))
    fill = input("Enter fill character (press Enter to skip): ")

    # Handle empty fill input
    fill = fill if fill else None

    result = divide_string(s, k, fill)
    
    print("\nDivided Groups:")
    for idx, group in enumerate(result, start=1):
        print(f"Group {idx}: {group}")

    # Optional: Show joined format
    print("\nJoined String (with '-'): ", '-'.join(result))
