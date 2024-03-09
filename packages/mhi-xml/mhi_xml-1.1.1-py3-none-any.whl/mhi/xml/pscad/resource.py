# Imports
#===============================================================================

from __future__ import annotations

from lxml import etree as ET

from typing import cast

from mhi.xml.node import *
from mhi.xml.pscad.types import ResourceType
from mhi.xml.pscad._project import project_lookup, ProjectMixin


#===============================================================================
# Exports
#===============================================================================


__all__ = ['Resource', 'ResourceMapping',]


#===============================================================================
# Resources
#===============================================================================

@project_lookup.tag('Resource')
class Resource(XmlNode):
    """
    A `<Resource/>` node
    """

    _SOURCE = """<Resource classid="SourceResource" id="0" url="">
      <paramlist>
        <param name="filepath" value="" />
        <param name="copy_file" value="false" />
        <param name="include" value="false" />
      </paramlist>
    </Resource>"""

    _STATIC = """<Resource classid="StaticResource" id="0" url="">
      <paramlist>
        <param name="filepath" value="" />
        <param name="copy_file" value="false" />
        <param name="type" value="2" />
        <param name="include" value="false" />
      </paramlist>
    </Resource>"""


    @staticmethod
    def _create(container: XmlNode, fmt: str, filepath: str,
                copy_file: bool = False, include: bool = True) -> Resource:
        resource = cast(Resource, container._parse(fmt))
        resource.filepath = filepath
        resource.copy_file = copy_file
        resource.include = include
        return resource


    def _param(self, key) -> ParamNode:
        node = self.find(f'paramlist/param[@name="{key}"]')
        if node is None:
            raise KeyError(f"Resource: No such key: {key!r}")
        return cast(ParamNode, node)

    @property
    def filepath(self) -> str:
        return self._param('filepath').value

    @filepath.setter
    def filepath(self, value: str):
        self._param('filepath').value = value
        self.set('url', str(value))

    @property
    def copy_file(self) -> bool:
        return bool(self._param('copy_file'))

    @copy_file.setter
    def copy_file(self, value: bool):
        self._param('copy_file').set_value(value)

    @property
    def include(self) -> bool:
        return bool(self._param('include'))

    @include.setter
    def include(self, value: bool):
        self._param('include').set_value(value)

    @property
    def type(self) -> ResourceType:
        return ResourceType(self._param('type').value)

    @include.setter
    def type(self, value: ResourceType):
        self._param('type').set_value(ResourceType(value))


class ResourceMapping(KeyMapping[Resource]):
    """
    The project's :class:`.Definition` dictionary.
    """

    def __init__(self, resources: XmlNode):

        super().__init__(resources, 'Resource', 'url')


    def __setitem__(self, url: str, resource: Resource):

        project = cast(ProjectMixin, self._container).project
        resource.set('id', str(project.make_id()))
        super().__setitem__(url, resource)


    def create_source(self, filepath: str, copy_file: bool = False,
                      include: bool = True) -> Resource:

        if filepath in self:
            raise KeyError("Resource already exists")
        resource = Resource._create(self._container, Resource._SOURCE,
                                    filepath, copy_file, include)
        self[filepath] = resource
        return resource


    def create_static(self, filepath: str, copy_file: bool = False,
                      include: bool = True,
                      type_: ResourceType | str | int = ResourceType.BINARY
                      ) -> Resource:

        if filepath in self:
            raise KeyError("Resource already exists")
        resource = Resource._create(self._container, Resource._STATIC,
                                    filepath, copy_file, include)
        resource.type = ResourceType(type_)
        self[filepath] = resource
        return resource
