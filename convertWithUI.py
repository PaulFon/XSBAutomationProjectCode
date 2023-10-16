import xml.etree.ElementTree as ET

# Prompt the user for the input XML file name
input_file = input("Enter the input XML file name: ")

# Prompt the user for the output file name
output_file = input("Enter the output file name for unique tags list: ")

# Parse the XML document using the input file (error handling omitted for brevity)
try:
    tree = ET.parse(input_file)
    root = tree.getroot()
except ET.ParseError:
    print("Error: Invalid XML file.")
    exit(1)

# Initialize a set to store unique tags
unique_tags = set()

# Function to recursively extract unique tags
def extract_unique_tags(element):
    unique_tags.add(element.tag)
    for child in element:
        extract_unique_tags(child)

# Start the extraction from the root element
extract_unique_tags(root)

# Write the unique tags to the output file
with open(output_file, 'w') as file:
    for tag in unique_tags:
        file.write(tag + '\n')

print(f"Unique tags have been extracted and saved to {output_file}.")
