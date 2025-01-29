# Author: Ben Imbriaco
# This program's goal is to output anagrams based off of user input.
# I plan to incorporate a GUI and maybe even host this as a website.
# Inspiration for this was Hannibal Lecter's anagrams in Silence of the Lambs

# Importing flask, a python web applidation framework. 
# request helps handle all data sent from client to server. 
# render template is used to render HTML templates
from flask import Flask, request, render_template

# The word list provided on macOS located at /usr/share/dict/words
file_path = '/usr/share/dict/words'
propernames_path = '/usr/share/dict/propernames'

# Small function for creating a string out of a list
def list_to_word(list):
    # Calling .join on '' will result in concatenting the list's elements with no spaces
    return "".join(list)

# Function for loading the names and entering them into a set
def load_names():
    # Empty set, set is used to avoid repeats
    my_set = set()
    try:
        # Open in read mode
        with open(propernames_path, 'r') as file:
            # One name is on each line
            for line in file:
                my_set.add(line.strip().lower())
    except Exception as e:
        print(f"Error: {e}")
    return my_set

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

def find_anagrams(unsorted_input, include_names):
     # Change the word to sorted format 
    sorted_input = sorted(unsorted_input)
    # Convert to string
    input_string = list_to_word(sorted_input)

    # Successful matches will be added into this list
    anagrams = []

    # If the user wants names included...
    proper_names_set = load_names()

    # Check the sorted input against the word list
    with open(file_path, 'r') as file:
        # The word list only contains one word on each line
        for line in file:
            # Remove whitespace and sort
            word = line.strip().lower()
            sorted_word = sorted(word)
            # Change into word
            output_string = list_to_word(sorted_word)
            # If words aren't the same, then compare
            if word != unsorted_input: 
                # If the anagram matches 
                if input_string == output_string:
                    # If equal, add the word unsorted to the anagrams list
                    anagrams.append(word)
    # If names are checked
    if include_names:
        # Iterate through set
        for name in proper_names_set:
            # Sort name
            sorted_name = sorted(name)
            if sorted_name == input_string:
                # Append the name
                anagrams.append("Name: " + name)
    
    # Finally, return the list
    return anagrams 

# Flask constructor takes current module as an argument
app = Flask(__name__)

# The .route() call is telling the application which maps a 
# URL to a specific function. The 'GET' and 'POST" methods
# allows the route to handle GET and POST HTTP requests.
# GET is used to request data from a certain source.
# POST is used to send data to a server for the purpose of 
# either creating or updating a resource

@app.route('/', methods=['GET', 'POST'])
# The '\' URL is now bound to the anagrams() function 
def anagrams():
    # Initiallly set the result to None
    result = None
    # If there is a post request
    if request.method == "POST":
        # Word variable is created
        word = request.form.get('word').lower()
        # Does the user want proper names?
        include_proper_names = 'include_proper_names' in request.form
        # Call the find_anagrams function on the provided word, 
        # store in result variable, and include whether or not 
        # they want names
        result = find_anagrams(word, include_proper_names)
    # Render the HTML template, and pass result in as a variable called anagrmas
    return render_template('index.html', anagrams=result)

   
   
# Main driver function
if __name__ == "__main__":
    app.run(debug=True)