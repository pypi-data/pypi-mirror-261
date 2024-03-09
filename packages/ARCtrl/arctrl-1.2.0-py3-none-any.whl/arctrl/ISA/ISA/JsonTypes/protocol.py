from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
from ....fable_modules.fable_library.array_ import map2
from ....fable_modules.fable_library.list import (FSharpList, try_find, exists, append, singleton, map, filter, empty)
from ....fable_modules.fable_library.option import (map as map_1, default_arg)
from ....fable_modules.fable_library.reflection import (TypeInfo, string_type, option_type, list_type, record_type, make_record, get_record_fields)
from ....fable_modules.fable_library.types import Record
from ....fable_modules.fable_library.util import equals
from ..helper import (Update_updateAppend, Update_updateOnlyByExisting, Update_updateOnlyByExistingAppend)
from ..helper import Update_UpdateOptions
from .comment import (Comment, Comment_reflection)
from .component import (Component, Component_reflection)
from .ontology_annotation import (OntologyAnnotation, OntologyAnnotation_reflection)
from .protocol_parameter import (ProtocolParameter, ProtocolParameter_reflection)

def _expr346() -> TypeInfo:
    return record_type("ARCtrl.ISA.Protocol", [], Protocol, lambda: [("ID", option_type(string_type)), ("Name", option_type(string_type)), ("ProtocolType", option_type(OntologyAnnotation_reflection())), ("Description", option_type(string_type)), ("Uri", option_type(string_type)), ("Version", option_type(string_type)), ("Parameters", option_type(list_type(ProtocolParameter_reflection()))), ("Components", option_type(list_type(Component_reflection()))), ("Comments", option_type(list_type(Comment_reflection())))])


@dataclass(eq = False, repr = False, slots = True)
class Protocol(Record):
    ID: str | None
    Name: str | None
    ProtocolType: OntologyAnnotation | None
    Description: str | None
    Uri: str | None
    Version: str | None
    Parameters: FSharpList[ProtocolParameter] | None
    Components: FSharpList[Component] | None
    Comments: FSharpList[Comment] | None

Protocol_reflection = _expr346

def Protocol_make(id: str | None=None, name: str | None=None, protocol_type: OntologyAnnotation | None=None, description: str | None=None, uri: str | None=None, version: str | None=None, parameters: FSharpList[ProtocolParameter] | None=None, components: FSharpList[Component] | None=None, comments: FSharpList[Comment] | None=None) -> Protocol:
    return Protocol(id, name, protocol_type, description, uri, version, parameters, components, comments)


def Protocol_create_Z7DFD6E67(Id: str | None=None, Name: str | None=None, ProtocolType: OntologyAnnotation | None=None, Description: str | None=None, Uri: str | None=None, Version: str | None=None, Parameters: FSharpList[ProtocolParameter] | None=None, Components: FSharpList[Component] | None=None, Comments: FSharpList[Comment] | None=None) -> Protocol:
    return Protocol_make(Id, Name, ProtocolType, Description, Uri, Version, Parameters, Components, Comments)


def Protocol_get_empty(__unit: None=None) -> Protocol:
    return Protocol_create_Z7DFD6E67()


def Protocol_tryGetByName(name: str, protocols: FSharpList[Protocol]) -> Protocol | None:
    def _arrow347(p: Protocol, name: Any=name, protocols: Any=protocols) -> bool:
        return equals(p.Name, name)

    return try_find(_arrow347, protocols)


def Protocol_existsByName(name: str, protocols: FSharpList[Protocol]) -> bool:
    def _arrow348(p: Protocol, name: Any=name, protocols: Any=protocols) -> bool:
        return equals(p.Name, name)

    return exists(_arrow348, protocols)


def Protocol_add(protocols: FSharpList[Protocol], protocol: Protocol) -> FSharpList[Protocol]:
    return append(protocols, singleton(protocol))


def Protocol_updateBy(predicate: Callable[[Protocol], bool], update_option: Update_UpdateOptions, protocol: Protocol, protocols: FSharpList[Protocol]) -> FSharpList[Protocol]:
    if exists(predicate, protocols):
        def _arrow349(p: Protocol, predicate: Any=predicate, update_option: Any=update_option, protocol: Any=protocol, protocols: Any=protocols) -> Protocol:
            if predicate(p):
                this: Update_UpdateOptions = update_option
                record_type_1: Protocol = p
                record_type_2: Protocol = protocol
                if this.tag == 2:
                    return make_record(Protocol_reflection(), map2(Update_updateAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 1:
                    return make_record(Protocol_reflection(), map2(Update_updateOnlyByExisting, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                elif this.tag == 3:
                    return make_record(Protocol_reflection(), map2(Update_updateOnlyByExistingAppend, get_record_fields(record_type_1), get_record_fields(record_type_2), None))

                else: 
                    return record_type_2


            else: 
                return p


        return map(_arrow349, protocols)

    else: 
        return protocols



def Protocol_updateByName(update_option: Update_UpdateOptions, protocol: Protocol, protocols: FSharpList[Protocol]) -> FSharpList[Protocol]:
    def predicate(p: Protocol, update_option: Any=update_option, protocol: Any=protocol, protocols: Any=protocols) -> bool:
        return equals(p.Name, protocol.Name)

    return Protocol_updateBy(predicate, update_option, protocol, protocols)


def Protocol_removeByName(name: str, protocols: FSharpList[Protocol]) -> FSharpList[Protocol]:
    def _arrow350(p: Protocol, name: Any=name, protocols: Any=protocols) -> bool:
        return not equals(p.Name, name)

    return filter(_arrow350, protocols)


def Protocol_getComments_Z5F51792E(protocol: Protocol) -> FSharpList[Comment] | None:
    return protocol.Comments


def Protocol_mapComments(f: Callable[[FSharpList[Comment]], FSharpList[Comment]], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, map_1(f, protocol.Comments))


def Protocol_setComments(protocol: Protocol, comments: FSharpList[Comment]) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, comments)


def Protocol_getProtocolType_Z5F51792E(protocol: Protocol) -> OntologyAnnotation | None:
    return protocol.ProtocolType


def Protocol_mapProtocolType(f: Callable[[OntologyAnnotation], OntologyAnnotation], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, map_1(f, protocol.ProtocolType), protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_setProtocolType(protocol: Protocol, protocol_type: OntologyAnnotation) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol_type, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_getVersion_Z5F51792E(protocol: Protocol) -> str | None:
    return protocol.Version


def Protocol_mapVersion(f: Callable[[str], str], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, map_1(f, protocol.Version), protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_setVersion(protocol: Protocol, version: str) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_getName_Z5F51792E(protocol: Protocol) -> str | None:
    return protocol.Name


def Protocol_mapName(f: Callable[[str], str], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, map_1(f, protocol.Name), protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_setName(protocol: Protocol, name: str) -> Protocol:
    return Protocol(protocol.ID, name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_getDescription_Z5F51792E(protocol: Protocol) -> str | None:
    return protocol.Description


def Protocol_mapDescription(f: Callable[[str], str], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, map_1(f, protocol.Description), protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_setDescription(protocol: Protocol, description: str) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, description, protocol.Uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_getUri_Z5F51792E(protocol: Protocol) -> str | None:
    return protocol.Uri


def Protocol_mapUri(f: Callable[[str], str], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, map_1(f, protocol.Uri), protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_setUri(protocol: Protocol, uri: str) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, uri, protocol.Version, protocol.Parameters, protocol.Components, protocol.Comments)


def Protocol_getComponents_Z5F51792E(protocol: Protocol) -> FSharpList[Component] | None:
    return protocol.Components


def Protocol_mapComponents(f: Callable[[FSharpList[Component]], FSharpList[Component]], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, map_1(f, protocol.Components), protocol.Comments)


def Protocol_setComponents(protocol: Protocol, components: FSharpList[Component]) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, protocol.Parameters, components, protocol.Comments)


def Protocol_addComponent(comp: Component, protocol: Protocol) -> Protocol:
    return Protocol_setComponents(protocol, append(default_arg(protocol.Components, empty()), singleton(comp)))


def Protocol_getParameters_Z5F51792E(protocol: Protocol) -> FSharpList[ProtocolParameter] | None:
    return protocol.Parameters


def Protocol_mapParameters(f: Callable[[FSharpList[ProtocolParameter]], FSharpList[ProtocolParameter]], protocol: Protocol) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, map_1(f, protocol.Parameters), protocol.Components, protocol.Comments)


def Protocol_setParameters(protocol: Protocol, parameters: FSharpList[ProtocolParameter]) -> Protocol:
    return Protocol(protocol.ID, protocol.Name, protocol.ProtocolType, protocol.Description, protocol.Uri, protocol.Version, parameters, protocol.Components, protocol.Comments)


def Protocol_addParameter(parameter: ProtocolParameter, protocol: Protocol) -> Protocol:
    return Protocol_setParameters(protocol, append(default_arg(protocol.Parameters, empty()), singleton(parameter)))


__all__ = ["Protocol_reflection", "Protocol_make", "Protocol_create_Z7DFD6E67", "Protocol_get_empty", "Protocol_tryGetByName", "Protocol_existsByName", "Protocol_add", "Protocol_updateBy", "Protocol_updateByName", "Protocol_removeByName", "Protocol_getComments_Z5F51792E", "Protocol_mapComments", "Protocol_setComments", "Protocol_getProtocolType_Z5F51792E", "Protocol_mapProtocolType", "Protocol_setProtocolType", "Protocol_getVersion_Z5F51792E", "Protocol_mapVersion", "Protocol_setVersion", "Protocol_getName_Z5F51792E", "Protocol_mapName", "Protocol_setName", "Protocol_getDescription_Z5F51792E", "Protocol_mapDescription", "Protocol_setDescription", "Protocol_getUri_Z5F51792E", "Protocol_mapUri", "Protocol_setUri", "Protocol_getComponents_Z5F51792E", "Protocol_mapComponents", "Protocol_setComponents", "Protocol_addComponent", "Protocol_getParameters_Z5F51792E", "Protocol_mapParameters", "Protocol_setParameters", "Protocol_addParameter"]

