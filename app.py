import xmltodict
import json

def xml_to_json(xml_file):
    with open(xml_file) as xml_file:
        my_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    json_data = json.dumps(my_dict)
    print(json_data)
    return json_data
