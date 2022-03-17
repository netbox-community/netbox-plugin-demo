from django.db.models import Count

from netbox.views import generic
from . import forms, models, tables


#
# AccessList views
#

class AccessListView(generic.ObjectView):
    queryset = models.AccessList.objects.all()


class AccessListListView(generic.ObjectListView):
    queryset = models.AccessList.objects.annotate(
        rule_count=Count('rules')
    )
    table = tables.AccessListTable


class AccessListEditView(generic.ObjectEditView):
    queryset = models.AccessList.objects.all()
    model_form = forms.AccessListForm


class AccessListDeleteView(generic.ObjectDeleteView):
    queryset = models.AccessList.objects.all()


#
# AccessListRule views
#

class AccessListRuleView(generic.ObjectView):
    queryset = models.AccessListRule.objects.all()


class AccessListRuleListView(generic.ObjectListView):
    queryset = models.AccessListRule.objects.all()
    table = tables.AccessListRuleTable


class AccessListRuleEditView(generic.ObjectEditView):
    queryset = models.AccessListRule.objects.all()
    model_form = forms.AccessListRuleForm


class AccessListRuleDeleteView(generic.ObjectDeleteView):
    queryset = models.AccessListRule.objects.all()