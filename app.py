import xmltodict as x
import xml.etree.cElementTree as e
import json as j

def xml_to_json(xml_file):
    with open(xml_file) as xml_file:
        my_dict = x.parse(xml_file.read())
    xml_file.close()
    json_data = j.dumps(my_dict)
    print(json_data)
    return json_data

def json_to_xml(json_file):
    with open(json_file) as json_file:
        d = j.load(json_file)

