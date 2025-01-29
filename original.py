# Author: Ben Imbriaco
# This program's goal is to output anagrams based off of user input.
# I plan to incorporate a GUI and maybe even host this as a website.
# Inspiration for this was Hannibal Lecter's anagrams in Silence of the Lambs

# The word list provided on macOS located at /usr/share/dict/words
file_path = '/usr/share/dict/words'

# Small function for creating a string out of a list
def list_to_word(list):
    # Calling .join on '' will result in concatenting the list's elements with no spaces
    return "".join(list)

# Helper function for formatting list
def list_to_string(list):
    # String variable
    str = ''
    # Counter variable
    count = 1
    for word in list:
        str += (f"{count}: {word}\n")
        count += 1
    return str

# Function for finding anagrams
def anagrams():
    # First step is to gather user input
    # Note that inout() always returns a string 
    unsorted_input = (input("Enter your unscrambled word: "))
    # Change the word to sorted format 
    sorted_input = sorted(unsorted_input)
    # Convert to string
    input_string = list_to_word(sorted_input)

    # Successful matches will be added into this list
    anagrams = []

    # Check the sorted input against the word list
    with open(file_path, 'r') as file:
        # The word list only contains one word on each line
        for line in file:
            # Remove whitespace and sort
            word = line.strip()
            sorted_word = sorted(word)
            # Change into word
            output_string = list_to_word(sorted_word)
            # If words aren't the same, then compare
            if word != unsorted_input: 
                # Compare using .lower() for case 
                if input_string.lower() == (output_string.lower()):
                    # If equal, add the word unsorted to the anagrams list
                    anagrams.append(word)
    
    # Finally, return the list
    print(f"Anagrams of {unsorted_input}: \n" + list_to_string(anagrams))
   

# Program executing
if __name__ == "__main__":
    # Call to anagrams function
    anagrams()


