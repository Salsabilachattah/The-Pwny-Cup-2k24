import itertools
import re

def replace_digits(hex_string, digit_mapping):
    """Replace digits 1-9 in the hex string according to the digit_mapping."""
    replaced_string = []
    for char in hex_string:
        if char in digit_mapping:
            replaced_string.append(digit_mapping[char])
        else:
            replaced_string.append(char)
    return ''.join(replaced_string)

def hex_to_text(hex_string):
    """Convert hex string to plain text."""
    try:
        bytes_object = bytes.fromhex(hex_string)
        return bytes_object.decode("utf-8", errors="ignore")  # Decode to text ignoring errors
    except ValueError:
        return None

def is_normal_text(text):
    """Check if the text contains only normal characters (alphanumeric, spaces, punctuation)."""
    # Regular expression for allowed characters (alphanumeric, spaces, common punctuation)
    return re.match(r'^[a-zA-Z0-9\s.,!?\'"()-]*$', text) is not None

# Input hex string
# hex_string = "503C3932543965395664313850549538563199"
hex_string = "" #Put the string you get from DTMF decoder here

# List of digits to be permuted (1 through 9)
digits = "123456789"

# Generate all permutations of the digits
permutations = itertools.permutations(digits)

# Try each permutation
for perm in permutations:
    # Create a mapping of original digits to permuted digits
    digit_mapping = {str(i+1): perm[i] for i in range(9)}
    
    # Replace the digits in the hex string
    replaced_hex_string = replace_digits(hex_string, digit_mapping)
    
    # Convert to text
    plain_text = hex_to_text(replaced_hex_string)
    
    # Check if the resulting text is "normal" and print it if so
    if plain_text and is_normal_text(plain_text):
        print(f"Permutation {perm} -> {plain_text}")
