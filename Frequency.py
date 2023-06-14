def most_frequent(string):
    # Create an empty dictionary to store the frequency of each letter
    frequency_dict = {}

    # Count the frequency of each letter in the string
    for letter in string:
        if letter in frequency_dict:
            frequency_dict[letter] += 1
        else:
            frequency_dict[letter] = 1

    # Sort the dictionary based on the frequency values in descending order
    sorted_dict = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for letter, frequency in sorted_dict:
        print(letter, ":", frequency)


# Example usage
most_frequent(str(input("Enter a string")).replace(" ",""))
