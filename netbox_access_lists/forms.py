from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelFilterSetForm, NetBoxModelForm
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField,
)
from utilities.forms.rendering import FieldSet

from .choices import ActionChoices, ProtocolChoices
from .models import AccessList, AccessListRule


class AccessListForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = AccessList
        fields = ('name', 'default_action', 'comments', 'tags')


class AccessListRuleForm(NetBoxModelForm):
    access_list = DynamicModelChoiceField(
        queryset=AccessList.objects.all(),
    )
    source_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
    )
    destination_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
    )
    comments = CommentField()

    class Meta:
        model = AccessListRule
        fields = (
            'access_list',
            'index',
            'description',
            'source_prefix',
            'source_ports',
            'destination_prefix',
            'destination_ports',
            'protocol',
            'action',
            'tags',
        )


class AccessListRuleFilterForm(NetBoxModelFilterSetForm):
    model = AccessListRule
    fieldsets = (
        FieldSet(
            'q',
            'filter_id',
            'tag',
        ),
        FieldSet(
            'access_list',
            'index',
            'protocol',
            'action',
            name='Attributes',
        ),
        FieldSet(
            'source_prefix_id',
            'source_port',
            name='Source',
        ),
        FieldSet(
            'destination_prefix_id',
            'destination_port',
            name='Destination',
        ),
    )

    access_list = forms.ModelMultipleChoiceField(
        queryset=AccessList.objects.all(),
        required=False,
    )
    index = forms.IntegerField(
        required=False,
    )
    protocol = forms.MultipleChoiceField(
        choices=ProtocolChoices,
        required=False,
    )
    action = forms.MultipleChoiceField(
        choices=ActionChoices,
        required=False,
    )
    source_prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
        label='Source Prefix',
    )
    destination_prefix_id = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False,
        label='Destination Prefix',
    )
    source_port = forms.IntegerField(
        label='Source Port',
        required=False,
    )
    destination_port = forms.IntegerField(
        label='Destination Port',
        required=False,
    )
    tag = TagFilterField(model)
