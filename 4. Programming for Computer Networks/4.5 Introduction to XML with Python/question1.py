import xml.etree.ElementTree as ET

# Create the root element
tag1 = ET.Element("tag1")

# Create sub-elements and assign text values
tag2 = ET.SubElement(tag1, "tag2")
tag2.text = "Animal"

tag3 = ET.SubElement(tag1, "tag3")
tag3.text = "Domestic"

tag4 = ET.SubElement(tag1, "tag4")

tag4_1 = ET.SubElement(tag4, "tag4.1")
tag4_1.text = "Cat"

tag4_2 = ET.SubElement(tag4, "tag4.2")
tag4_2.text = "Persian"

tag5 = ET.SubElement(tag1, "tag5")
tag5.text = "Iran"

tag6 = ET.SubElement(tag1, "tag6")
tag6.text = "Male"

tag7 = ET.SubElement(tag1, "tag7")
tag7.text = "2021.05.04"

# Print the XML structure
ET.dump(tag1)
