from django.db.models import Count
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import forms, models, tables


#
# AccessList views
#


@register_model_view(models.AccessList)
class AccessListView(generic.ObjectView):
    queryset = models.AccessList.objects.all()

    def get_extra_context(self, request, instance):
        """Add rules table to access list view context."""
        rules = instance.rules.restrict(request.user, 'view')
        rules_table = tables.AccessListRuleTable(rules)
        rules_table.columns.hide('access_list')  # Hide AccessList column
        rules_table.configure(request)

        return {
            'rules_table': rules_table,
        }


@register_model_view(models.AccessList, 'rules')
class AccessListRulesView(generic.ObjectChildrenView):
    queryset = models.AccessList.objects.all()
    child_model = models.AccessListRule
    table = tables.AccessListRuleTable
    tab = ViewTab(
        label='Rules',
        badge=lambda obj: obj.rules.count(),
        permission='netbox_access_lists.view_accesslistrule',
        weight=500,
    )

    def get_children(self, request, parent):
        return parent.rules.restrict(request.user, 'view').all()

    def get_table(self, *args, **kwargs):
        rules_table = super().get_table(*args, **kwargs)
        rules_table.columns.hide('access_list')  # Hide AccessList column
        return rules_table


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
