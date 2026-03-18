import django_tables2 as tables
from netbox.tables import ChoiceFieldColumn, NetBoxTable, columns

from .models import AccessList, AccessListRule


class AccessListTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column(
        verbose_name='Rules',
    )

    class Meta(NetBoxTable.Meta):
        model = AccessList
        fields = (
            'pk',
            'id',
            'name',
            'default_action',
            'rule_count',
            'comments',
            'actions',
        )
        default_columns = ('name', 'default_action', 'rule_count', 'actions')


class AccessListRuleTable(NetBoxTable):
    access_list = tables.Column(
        linkify=True,
    )
    index = tables.Column(
        linkify=True,
    )
    source_prefix = tables.Column(
        linkify=True,
    )
    source_ports = columns.ArrayColumn()
    destination_prefix = tables.Column(
        linkify=True,
    )
    destination_ports = columns.ArrayColumn()
    protocol = ChoiceFieldColumn()
    action = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = AccessListRule
        fields = (
            'pk',
            'id',
            'access_list',
            'index',
            'source_prefix',
            'source_ports',
            'destination_prefix',
            'destination_ports',
            'protocol',
            'action',
            'description',
            'comments',
            'actions',
        )
        default_columns = (
            'access_list',
            'index',
            'source_prefix',
            'source_ports',
            'destination_prefix',
            'destination_ports',
            'protocol',
            'action',
            'actions',
        )
