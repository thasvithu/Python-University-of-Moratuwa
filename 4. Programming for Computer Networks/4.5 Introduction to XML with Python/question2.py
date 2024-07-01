import xml.etree.ElementTree as ET

# The XML data as a string
xml_data = '''<motorvehicles>
    <vehicle>
        <registration_no>CBB1456</registration_no>
        <make>Toyota</make>
        <model>Premio</model>
    </vehicle>
    <vehicle>
        <registration_no>PR2245</registration_no>
        <make>Mazda</make>
        <model>Bongo</model>
    </vehicle>
    <vehicle>
        <registration_no>DE2115</registration_no>
        <make>TATA</make>
        <model>Sumo</model>
    </vehicle>
    <vehicle>
        <registration_no>CAR7785</registration_no>
        <make>Kia</make>
        <model>Optima</model>
    </vehicle>
</motorvehicles>'''

# Parse the XML data
root = ET.fromstring(xml_data)

# Update the details of the vehicle with registration number DE2115
for vehicle in root.findall('vehicle'):
    reg_no = vehicle.find('registration_no').text
    if reg_no == 'DE2115':
        vehicle.find('make').text = 'Nissan'
        vehicle.find('model').text = 'Skyline'
        break

# Print the registration numbers of all Nissan vehicles
for vehicle in root.findall('vehicle'):
    if vehicle.find('make').text == 'Nissan':
        print(vehicle.find('registration_no').text)
