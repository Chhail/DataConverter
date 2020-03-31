import json
import xmltodict

def xml_to_json(xml_file):
    with open(xml_file) as f:
        xmlString = f.read()

    print("XML input (" + xml_file + "): \n" + xmlString)

    jsonString = json.dumps(xmltodict.parse(xmlString), indent = 4)

    print("\nJSON output (output.json): \n" + jsonString)

    with open("output.json","w") as f:
        f.write(jsonString)

def json_to_xml(json_file):
    with open(json_file) as json_file:
        json_data = json_file.read()
    print("JSON input (" + json_file + "): \n" + json_data)
    xmlString = xmltodict.unparse(json.loads(json_data), pretty = True)
    print("\nXML output (output.xml): \n" + xmlString)
    with open("output.xml", "w") as xml_file:
        xml_file.write(xmlString)
