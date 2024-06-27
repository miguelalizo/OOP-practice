from abc import ABC, abstractmethod
import json
import pprint


class JSONComponent(ABC):
    """The Component interface sets the common method
    for all components in the JSON Parser"""

    @abstractmethod
    def parse(self):
        """The parse method needs to be implemented
        by leaf and component classes"""


class JSONLeaf(JSONComponent):
    """Leaf represents individual elements in JSON structure"""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def parse(self):
        """Parsing method for leaf"""
        return f"parsing JSON Leaf: {self.key}: {self.value}"


class JSONObject(JSONComponent):
    """Object represents JSON Objects that can contain other JSON elements"""

    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        """Method to remove component"""
        self.children.remove(component)

    def parse(self):
        """Parsing method for JSON object"""
        results = []
        for child in self.children:
            results.append(child.parse())
        return "\n".join(results)


def parse_json(json_dict):
    # create root JSON object
    root = JSONObject()

    # create values based on json structure
    for key, value in json_dict.items():
        if isinstance(value, dict):
            obj = JSONObject()
            for k, v in value.items():
                leaf = JSONLeaf(k, v)
                obj.add(leaf)
                root.add(obj)
        else:
            leaf = JSONLeaf(key, value)
            root.add(leaf)
    return root


if __name__ == "__main__":
    # sample json string
    sample_json = (
        '{"name": "John Doe", "age": 30, "address": {"city": "New York", "zip": 10001}}'
    )

    json_str = json.loads(sample_json)
    pprint.pprint(json_str)

    # parsing json string and creating nodes
    json_structure = parse_json(json_str)

    # displaying structure and executing parsing
    print(json_structure.parse())
