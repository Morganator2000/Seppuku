'''
This script is designed to take in another Python script as an input, then it
erases all the comments, refactors all the variable names, and refactors all 
the defined functions. The end result is a script that is still 100% functional,
but is not at all human-readable.
'''

import re
import random
import string

# Generate new names for variables and functions.
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Delete comments
def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'#.*', '', code)
    # Remove multi-line comments
    code = re.sub(r'(\'\'\'(.*?)\'\'\')|(\"\"\"(.*?)\"\"\")', '', code, flags=re.DOTALL)
    return code

def refactor_names(code):
    # Regex pattern for matching variables and functions.
    variable_pattern = r'\b([a-zA-Z_]\w*)\s*(?=\=)'
    function_pattern = r'\bdef\s+([a-zA-Z_]\w*)\s*\('
    
    # Find all variable and function names
    variables = set(re.findall(variable_pattern, code))
    functions = set(re.findall(function_pattern, code))
    
    # Generate random names for variables and functions, then replace them
    mapping = {}
    for var in variables:
        new_name = generate_random_string()
        mapping[var] = new_name
        code = re.sub(r'\b{}\b'.format(re.escape(var)), new_name, code)
    for func in functions:
        new_name = generate_random_string()
        mapping[func] = new_name
        code = re.sub(r'\b{}\b'.format(re.escape(func)), new_name, code)
    
    return code, mapping

def seppuku(input_file, output_file):
    with open(input_file, 'r') as file:
        original_code = file.read()

    # Remove comments
    code_without_comments = remove_comments(original_code)

    # Refactor variable and function names
    modified_code, name_mapping = refactor_names(code_without_comments)

    # Write modified code to the output file
    with open(output_file, 'w') as file:
        file.write(modified_code)

    return name_mapping

#Start of the script.
input_file = "intro_to_coding - Copy.py"
name_mapping = seppuku(input_file, input_file)
#Print new mappings, just in case you need to reverse the changes.
print("Variable and function name mapping:")
for old_name, new_name in name_mapping.items():
    print(f"{old_name} -> {new_name}")
