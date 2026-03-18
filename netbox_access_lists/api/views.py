from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import AccessListSerializer, AccessListRuleSerializer


class AccessListViewSet(NetBoxModelViewSet):
    queryset = models.AccessList.objects.annotate(rule_count=Count('rules')).prefetch_related('tags')
    serializer_class = AccessListSerializer


class AccessListRuleViewSet(NetBoxModelViewSet):
    queryset = models.AccessListRule.objects.select_related(
        'access_list', 'source_prefix', 'destination_prefix'
    ).prefetch_related('tags')
    serializer_class = AccessListRuleSerializer
    filterset_class = filtersets.AccessListRuleFilterSet
