import strawberry
import strawberry_django

from .types import AccessListType, AccessListRuleType


@strawberry.type(name='Query')
class NetBoxAccessListQuery:
    access_list: AccessListType = strawberry_django.field()
    access_list_list: list[AccessListType] = strawberry_django.field()

    access_list_rule: AccessListRuleType = strawberry_django.field()
    access_list_rule_list: list[AccessListRuleType] = strawberry_django.field()
