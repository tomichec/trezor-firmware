# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeDebugSwipeDirection = Literal[0, 1, 2, 3]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeDebugSwipeDirection = None  # type: ignore


class DebugLinkDecision(p.MessageType):
    MESSAGE_WIRE_TYPE = 100

    def __init__(
        self,
        yes_no: bool = None,
        swipe: EnumTypeDebugSwipeDirection = None,
        input: str = None,
    ) -> None:
        self.yes_no = yes_no
        self.swipe = swipe
        self.input = input

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('yes_no', p.BoolType, 0),
            2: ('swipe', p.EnumType("DebugSwipeDirection", (0, 1, 2, 3)), 0),
            3: ('input', p.UnicodeType, 0),
        }
