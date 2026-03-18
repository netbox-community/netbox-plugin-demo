import strawberry

from ..choices import ActionChoices, ProtocolChoices


ActionEnum = strawberry.enum(ActionChoices.as_enum())
ProtocolEnum = strawberry.enum(ProtocolChoices.as_enum())
