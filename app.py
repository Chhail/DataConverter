import json
import xmltodict
import yaml

def xml_to_json(xml_file):
    with open(xml_file) as f:
        xml_data = f.read()
    print("XML input (" + xml_file + "): \n" + xml_data)
    json_data = json.dumps(xmltodict.parse(xml_data), indent=4)
    print("\nJSON output (xml_to_json.json): \n" + json_data)
    with open("xml_to_json.json","w") as f:
        f.write(json_data)

def json_to_xml(json_file):
    with open(json_file,"r") as f:
        jsonString = f.read()
    print("JSON input (" + json_file + "):\n" + jsonString)
    xmlString = xmltodict.unparse(json.loads(jsonString), pretty=True)
    print("\nXML output(json_to_xml.xml):\n" + xmlString)
    with open("json_to_xml.xml", 'w') as f:
        f.write(xmlString)

def xml_to_yaml(xml_file):
    with open(xml_file) as f:
        xml_data = f.read()
    print("XML input (" + xml_file + "): \n" + xml_data)
    json_data = json.dumps(xmltodict.parse(xml_data), indent=4)
    yaml_data = yaml.dump(json.loads(json_data))
    print("\nYAML output (xml_to_yaml.yaml): \n" + yaml_data)
    with open("xml_to_yaml.yaml","w") as f:
        f.write(yaml_data)

def yaml_to_xml(yaml_file):
    with open(yaml_file) as f:
        yaml_data = f.read()
    print("YAML input (" + yaml_file + "):\n" + yaml_data)
    xml_data = xmltodict.unparse(yaml.load(yaml_data), pretty=True)
    print("\nXML output (yaml_to_xml.xml):\n" + xml_data)
    with open("yaml_to_xml.xml","w") as f:
        f.write(xml_data)

def json_to_yaml(json_file):
    with open(json_file) as f:
        json_data = f.read()
    print("JSON input (" + json_file + "): \n" + json_data)
    yaml_data = yaml.dump(json.loads(json_data), indent = 4)
    print("\nYAML output (json_to_yaml.yaml): \n" + yaml_data)
    with open("json_to_yaml.yaml","w") as f:
        f.write(yaml_data)

def yaml_to_json(yaml_file):
    with open(yaml_file) as f:
        yaml_data = f.read()
    print("YAML input (" + yaml_file + "):\n" + yaml_data)
    json_data = json.dumps(yaml.load(yaml_data), indent=4)
    print("\nJSON output (yaml_to_json.json):\n" + json_data)
    with open("yaml_to_json.json","w") as f:
        f.write(json_data)


