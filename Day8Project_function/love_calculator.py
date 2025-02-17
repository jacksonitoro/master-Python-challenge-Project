def calculate_love_score(name1, name2):
    """
    Calculate the love score between two names based on the frequency of certain letters.
    """
    # Combine names and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Calculate TRUE score
    true_score = sum(combined_names.count(char) for char in "true")

    # Calculate LOVE score
    love_score = sum(combined_names.count(char) for char in "love")

    # Combine scores
    total_score = int(f"{true_score}{love_score}")

    # Print the result
    print(total_score)

# Example usage:
calculate_love_score("Jackson Itoro", "Keboh Enebimoere")
