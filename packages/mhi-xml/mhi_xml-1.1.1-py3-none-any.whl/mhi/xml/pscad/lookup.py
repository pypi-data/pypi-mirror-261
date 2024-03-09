from lxml import etree as ET
from mhi.xml.node import TagLookup, XmlNode

class Lookup:
    _tag: TagLookup
    _map: dict[str, XmlNode]

    def __init__(self, base_tag_lookup):
        self._tag = TagLookup(base_tag_lookup)
        self._map = {}

    @property
    def tag(self):
        return self._tag

    def classid(self, class_id: str):
        def wrapper(cls):
            if class_id in self._map:
                raise KeyError(f"Duplicate classid {class_id!r}")
            self._map[class_id] = cls
            return cls

        return wrapper

    def parser(self, **kwargs) -> ET.XMLParser:

        parser = ET.XMLParser(**kwargs)

        lookup = ET.AttributeBasedElementClassLookup(
            'classid', self._map, self._tag)
        parser.set_element_class_lookup(lookup)

        return parser
