from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Something(_message.Message):
    __slots__ = ()
    class House(_message.Message):
        __slots__ = ("height", "width", "depth")
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        DEPTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        width: int
        depth: int
        def __init__(self, height: _Optional[int] = ..., width: _Optional[int] = ..., depth: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
