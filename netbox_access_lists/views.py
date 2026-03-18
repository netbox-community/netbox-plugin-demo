from django.db.models import Count
from netbox.views import generic
from utilities.views import register_model_view

from . import forms, models, tables


#
# AccessList views
#


@register_model_view(models.AccessList)
class AccessListView(generic.ObjectView):
    queryset = models.AccessList.objects.all()


@register_model_view(models.AccessList, name='list', path='', detail=False)
class AccessListListView(generic.ObjectListView):
    queryset = models.AccessList.objects.annotate(
        rule_count=Count('rules'),
    )
    table = tables.AccessListTable


@register_model_view(models.AccessList, name='add', detail=False)
@register_model_view(models.AccessList, name='edit')
class AccessListEditView(generic.ObjectEditView):
    queryset = models.AccessList.objects.all()
    form = forms.AccessListForm


@register_model_view(models.AccessList, name='delete')
class AccessListDeleteView(generic.ObjectDeleteView):
    queryset = models.AccessList.objects.all()


#
# AccessListRule views
#


@register_model_view(models.AccessListRule)
class AccessListRuleView(generic.ObjectView):
    queryset = models.AccessListRule.objects.all()


@register_model_view(models.AccessListRule, name='list', path='', detail=False)
class AccessListRuleListView(generic.ObjectListView):
    queryset = models.AccessListRule.objects.all()
    table = tables.AccessListRuleTable


@register_model_view(models.AccessListRule, name='add', detail=False)
@register_model_view(models.AccessListRule, name='edit')
class AccessListRuleEditView(generic.ObjectEditView):
    queryset = models.AccessListRule.objects.all()
    form = forms.AccessListRuleForm


@register_model_view(models.AccessListRule, name='delete')
class AccessListRuleDeleteView(generic.ObjectDeleteView):
    queryset = models.AccessListRule.objects.all()
