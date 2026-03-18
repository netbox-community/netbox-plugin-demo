import django.contrib.postgres.fields
import django.db.models.deletion
import netbox.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('extras', '0134_owner'),
        ('ipam', '0086_gfk_indexes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessList',
            fields=[
                (
                    'id',
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
                ),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                (
                    'custom_field_data',
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder,
                    ),
                ),
                ('name', models.CharField(max_length=100)),
                ('default_action', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                (
                    'tags',
                    taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
                ),
            ],
            options={
                'verbose_name': 'Access List',
                'ordering': ('name',),
            },
            bases=(netbox.models.deletion.DeleteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='AccessListRule',
            fields=[
                (
                    'id',
                    models.BigAutoField(auto_created=True, primary_key=True, serialize=False),
                ),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                (
                    'custom_field_data',
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=utilities.json.CustomFieldJSONEncoder,
                    ),
                ),
                ('index', models.PositiveIntegerField()),
                ('protocol', models.CharField(blank=True, max_length=30)),
                (
                    'source_ports',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.PositiveIntegerField(),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    'destination_ports',
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.PositiveIntegerField(),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                ('action', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                (
                    'access_list',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='rules',
                        to='netbox_access_lists.accesslist',
                    ),
                ),
                (
                    'destination_prefix',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='+',
                        to='ipam.prefix',
                    ),
                ),
                (
                    'source_prefix',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='+',
                        to='ipam.prefix',
                    ),
                ),
                (
                    'tags',
                    taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
                ),
            ],
            options={
                'verbose_name': 'Access List Rule',
                'ordering': ('access_list', 'index'),
                'unique_together': {('access_list', 'index')},
            },
            bases=(netbox.models.deletion.DeleteMixin, models.Model),
        ),
    ]
