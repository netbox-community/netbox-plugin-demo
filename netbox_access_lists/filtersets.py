import django_filters

from ipam.models import Prefix
from netbox.filtersets import NetBoxModelFilterSet
from utilities.filters import NumericArrayFilter
from utilities.filtersets import register_filterset

from .models import AccessListRule


@register_filterset
class AccessListRuleFilterSet(NetBoxModelFilterSet):
    source_prefix = django_filters.ModelMultipleChoiceFilter(
        field_name='source_prefix__prefix',
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        label='Source Prefix (value)',
    )
    source_prefix_id = django_filters.ModelMultipleChoiceFilter(
        field_name='source_prefix',
        queryset=Prefix.objects.all(),
        to_field_name='id',
        label='Source Prefix (ID)',
    )
    destination_prefix = django_filters.ModelMultipleChoiceFilter(
        field_name='destination_prefix__prefix',
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        label='Destination Prefix (value)',
    )
    destination_prefix_id = django_filters.ModelMultipleChoiceFilter(
        field_name='destination_prefix',
        queryset=Prefix.objects.all(),
        to_field_name='id',
        label='Destination Prefix (ID)',
    )

    source_port = NumericArrayFilter(
        field_name='source_ports',
        lookup_expr='contains',
        label='Source Port',
    )
    destination_port = NumericArrayFilter(
        field_name='destination_ports',
        lookup_expr='contains',
        label='Destination Port',
    )

    class Meta:
        model = AccessListRule
        fields = ('id', 'access_list', 'index', 'protocol', 'action')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
