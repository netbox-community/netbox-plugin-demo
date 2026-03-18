from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

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
            'comments',
            'tags',
        )


class AccessListRuleFilterForm(NetBoxModelFilterSetForm):
    model = AccessListRule
    access_list = forms.ModelMultipleChoiceField(
        queryset=AccessList.objects.all(),
        required=False
    )
    index = forms.IntegerField(
        required=False
    )
    protocol = forms.MultipleChoiceField(
        choices=ProtocolChoices,
        required=False
    )
    action = forms.MultipleChoiceField(
        choices=ActionChoices,
        required=False
    )
