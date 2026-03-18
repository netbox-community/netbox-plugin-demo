from ipam.api.serializers import PrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ..models import AccessList, AccessListRule


class AccessListSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_access_lists-api:accesslist-detail',
    )
    rule_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = AccessList
        fields = (
            'id',
            'url',
            'display',
            'name',
            'default_action',
            'rule_count',
            'comments',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'name')


class AccessListRuleSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_access_lists-api:accesslistrule-detail',
    )
    access_list = AccessListSerializer(nested=True)
    source_prefix = PrefixSerializer(nested=True, required=False, allow_null=True)
    destination_prefix = PrefixSerializer(nested=True, required=False, allow_null=True)

    class Meta:
        model = AccessListRule
        fields = (
            'id',
            'url',
            'display',
            'access_list',
            'index',
            'protocol',
            'source_prefix',
            'source_ports',
            'destination_prefix',
            'destination_ports',
            'action',
            'description',
            'comments',
            'tags',
            'custom_fields',
            'created',
            'last_updated',
        )
        brief_fields = ('id', 'url', 'display', 'index')
