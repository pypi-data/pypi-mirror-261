# import os
# import re

# import sys
# # Path to the file containing data to be checked
# # file_path = "/home/user1/Desktop/pkgLavanya/pkgLavanya/data.txt"
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# script_directory = os.path.dirname(os.path.abspath(__file__))
# from config import patterns
# # Specify the file name
# file_name = "data.txt"

# # Create the absolute file path
# file_path = os.path.join(script_directory, file_name)

#print("Generated File Path:", file_path)

# import os
# import re
# from .config import patterns

# # Assuming data.txt is in the same directory as detect_info.py
# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

# def find_pattern(input_string):
#     # ... (your existing code)

# # Open the file and read its content
# with open(file_path) as file:
#     content = file.read()

# # Print the result of pattern matching
# def op_gen():
#     print(find_pattern(content))

# op_gen()

# 

# import os
# import re
# from pkgLavanya import config as c  # Adjust the import path

# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")
# import os
# import re
# import sys

# # Add the parent directory to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from pkgLavanya import config as c

# file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

# # Rest of your code

# def find_pattern(input_string):
#     """
#     Check if any pattern from the list 'patterns' is matched in the input string.

#     Args:
#         input_string (str): The input string to be checked for patterns.

#     Returns:
#         bool: True if any pattern is matched, False otherwise.
#     """
#     matched = False
#     for line in input_string.split("\n"):
#         # Iterate through each pattern to check for a match
#         for pattern in c.patterns:
#             if re.match(pattern, line):
#                 matched = True
#                 break
#         if matched:
#             break  # Break if any pattern is matched
#     return matched

# # Open the file and read its content
# with open(file_path) as file:
#     content = file.read()

# # Print the result of pattern matching
# def op_gen():
#     print(find_pattern(content))

# op_gen()


# import os
# import re
# import sys

# # Add the parent directory to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from pkgLavanya import config as c
# def find_pattern(input_string):
#     """
#     Check if any pattern from the list 'patterns' is matched in the input string.

#     Args:
#         input_string (str): The input string to be checked for patterns.

#     Returns:
#         bool: True if any pattern is matched, False otherwise.
#     """
#     matched = False
#     for line in input_string.split("\n"):
#         # Iterate through each pattern to check for a match
#         for pattern in c.patterns:
#             if re.match(pattern, line):
#                 matched = True
#                 break
#         if matched:
#             break  # Break if any pattern is matched
#     return matched

# # Open the file and read its content
# with open(data_file_path) as file:
#     content = file.read()

# # Print the result of pattern matching
# def op_gen():
#     print(find_pattern(content))

# op_gen()


# import os
# import re
# import pkg_resources

# # Dynamically locate the data.txt file
# data_file_path = pkg_resources.resource_filename(__name__, "data.txt")

# # Import patterns from the config module
# try:
#     from pkgLavanya import config as c
# except ImportError:
#     # If running as a script, adjust the import path
#     import sys
#     sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
#     from pkgLavanya import config as c

# def find_pattern(input_string):
#     """
#     Check if any pattern from the list 'patterns' is matched in the input string.

#     Args:
#         input_string (str): The input string to be checked for patterns.

#     Returns:
#         bool: True if any pattern is matched, False otherwise.
#     """
#     matched = False
#     for line in input_string.split("\n"):
#         # Iterate through each pattern to check for a match
#         for pattern in c.patterns:
#             if re.match(pattern, line):
#                 matched = True
#                 break
#         if matched:
#             break  # Break if any pattern is matched
#     return matched

# # Open the file and read its content
# with open(data_file_path) as file:
#     content = file.read()

# # Print the result of pattern matching
# def op_gen():
#     print(find_pattern(content))

# # If running as a script, execute op_gen
# if __name__ == "__main__":
#     op_gen()


import os
import re
import pkg_resources

# Determine if running as a script or imported as a module
running_as_script = __name__ == "__main__"

# Define the relative path to data.txt when running as a script
script_data_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.txt")

# Import patterns from the config module
try:
    from pkgLavanya import config as c
except ImportError:
    # If running as a script, adjust the import path
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from pkgLavanya import config as c

def find_pattern(input_string):
    """
    Check if any pattern from the list 'patterns' is matched in the input string.

    Args:
        input_string (str): The input string to be checked for patterns.

    Returns:
        bool: True if any pattern is matched, False otherwise.
    """
    matched = False
    for line in input_string.split("\n"):
        # Iterate through each pattern to check for a match
        for pattern in c.patterns:
            if re.match(pattern, line):
                matched = True
                break
        if matched:
            break  # Break if any pattern is matched
    return matched

# Use the appropriate file path based on the context
data_file_path = script_data_file_path if running_as_script else pkg_resources.resource_filename(__name__, "data.txt")

# Open the file and read its content
with open(data_file_path) as file:
    content = file.read()

# Print the result of pattern matching
def op_gen():
    print(find_pattern(content))

# If running as a script, execute op_gen
if running_as_script:
    op_gen()
