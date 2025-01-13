from netbox.search import SearchIndex, register_search
from .models import AccessList, AccessListRule


@register_search
class AccessListIndex(SearchIndex):
    model = AccessList
    fields = (
        ('name', 100),
        ('comments', 5000),
    )


@register_search
class AccessListRuleIndex(SearchIndex):
    model = AccessListRule
    fields = (
        ('description', 500),
    )
