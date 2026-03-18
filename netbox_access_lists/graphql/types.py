from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType

from .. import models
from . import filters

if TYPE_CHECKING:
    from ipam.graphql.types import PrefixType


@strawberry_django.type(models.AccessList, fields='__all__', filters=filters.AccessListFilter)
class AccessListType(NetBoxObjectType):
    # Related models
    rules: list[Annotated['AccessListRuleType', strawberry.lazy('netbox_access_lists.graphql.types')]]


@strawberry_django.type(models.AccessListRule, fields='__all__', filters=filters.AccessListRuleFilter)
class AccessListRuleType(NetBoxObjectType):
    # Model fields
    access_list: Annotated['AccessListType', strawberry.lazy('netbox_access_lists.graphql.types')]
    source_prefix: Annotated['PrefixType', strawberry.lazy('ipam.graphql.types')] | None
    destination_prefix: Annotated['PrefixType', strawberry.lazy('ipam.graphql.types')] | None
