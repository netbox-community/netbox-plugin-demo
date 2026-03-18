from netbox.search import SearchIndex, register_search

from .models import AccessList, AccessListRule


@register_search
class AccessListIndex(SearchIndex):
    model = AccessList
    fields = (
        ('name', 100),
        ('comments', 5000),
    )
    display_attrs = ('name', 'default_action')


@register_search
class AccessListRuleIndex(SearchIndex):
    model = AccessListRule
    fields = (
        ('description', 500),
        ('comments', 5000),
    )
    display_attrs = (
        'access_list',
        'index',
        'protocol',
        'source_prefix',
        'source_ports',
        'destination_prefix',
        'destination_ports',
        'action',
        'description',
    )
