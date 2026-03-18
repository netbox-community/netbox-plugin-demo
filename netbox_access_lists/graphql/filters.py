from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from netbox.graphql.filters import NetBoxModelFilter
from strawberry import ID
from strawberry_django import FilterLookup

from .. import models

if TYPE_CHECKING:
    from ipam.graphql.filters import PrefixFilter
    from netbox.graphql.filter_lookups import IntegerArrayLookup, IntegerLookup

    from .enums import ActionEnum, ProtocolEnum


@strawberry_django.filter_type(models.AccessList, lookups=True)
class AccessListFilter(NetBoxModelFilter):
    name: FilterLookup[str] | None = strawberry_django.filter_field()
    default_action: Annotated['ActionEnum', strawberry.lazy('netbox_access_lists.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )


@strawberry_django.filter_type(models.AccessListRule, lookups=True)
class AccessListRuleFilter(NetBoxModelFilter):
    access_list: Annotated['AccessListFilter', strawberry.lazy('netbox_access_lists.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    access_list_id: ID | None = strawberry_django.filter_field()
    index: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    protocol: Annotated['ProtocolEnum', strawberry.lazy('netbox_access_lists.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    source_prefix: Annotated['PrefixFilter', strawberry.lazy('ipam.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    source_prefix_id: ID | None = strawberry_django.filter_field()
    source_ports: Annotated['IntegerArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    destination_prefix: Annotated['PrefixFilter', strawberry.lazy('ipam.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    destination_prefix_id: ID | None = strawberry_django.filter_field()
    destination_ports: Annotated['IntegerArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    action: Annotated['ActionEnum', strawberry.lazy('netbox_access_lists.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
