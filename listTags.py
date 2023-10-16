import xml.etree.ElementTree as ET

tree = ET.parse('HeartDisciple.scml')  # Replace 'your_xml_file.xml' with your XML file's path
root = tree.getroot()

unique_tags = set()

def extract_tags(element):
    unique_tags.add(element.tag)
    for child in element:
        extract_tags(child)

extract_tags(root)

for tag in unique_tags:
    print(tag)