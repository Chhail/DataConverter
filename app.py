import json
import xmltodict

def xml_to_json(xml_file):
    with open(xml_file) as xml_file:
        my_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    json_data = json.dumps(my_dict)
    print(json_data)
    return json_data

def json_to_xml(json_file):
    with open(json_file) as f:
        jsonString = f.read()

    print("JSON input (" + json_file + "): \n" + jsonString)

    xmlString = xmltodict.unparse(json.loads(jsonString), pretty = True)

    print("\nXML output (output.xml): \n" + xmlString)

    with open("output.xml", "w") as f:
        f.write(xmlString)

json_to_xml("my_json.json")
